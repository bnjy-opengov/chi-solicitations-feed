# Standard Library Imports
import contextlib
import json
# Third Party Module Imports
from selenium import webdriver


def get_business_bids():
    browser_engine = webdriver.Firefox

    with contextlib.closing(browser_engine()) as browser:
        browser.get('https://webapps1.cityofchicago.org/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/begin.do?agencyId=city')
        bid_option = browser.find_element_by_xpath('//option[@value="Bid"]')
        bid_option.click()

        to_date = browser.find_element_by_id('toDateId')
        to_date.send_keys('12/03/2013')

        from_date = browser.find_element_by_id('fromDateId')
        from_date.send_keys('12/03/2012')

        search_button = browser.find_element_by_xpath('//input[@alt="search button"]')
        search_button.click()

        print_version_button = browser.find_element_by_xpath('//img[@src="/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/../../../../../resources/images/print_version.gif"]')
        print_version_button.click()

        # The "Print Version" button opens a new Firefox window
        # We need to find the handle of the new window and switch to it
        other_window_handles = [handle for handle in browser.window_handles if handle != browser.current_window_handle]
        # We're assuming there's only one other window
        new_window_handle = other_window_handles[0]

        browser.switch_to_window(new_window_handle)

        results_tbody = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody')
        header_row = results_tbody.find_elements_by_tag_name('tr')[0]
        result_rows = results_tbody.find_elements_by_tag_name('tr')[1:]

        data = []
        header = [cell.text for cell in header_row.find_elements_by_tag_name('th')]
        for result_row in result_rows:
            results = [cell.text for cell in result_row.find_elements_by_tag_name('td')]
            data.append(dict(zip(header, results)))
    return json.dumps(data)


if __name__ == "__main__":
    print get_business_bids()
