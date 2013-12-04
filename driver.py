__author__ = 'bkalantzis'
from selenium import webdriver

to_date_id = 'toDateId'
from_date_id = 'fromDateId'
bid_option_xpath = '//option[@value="Bid"]'
search_button_xpath = '//input[@alt="search button"]'
print_version_image_xpath = '//img[@src="/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/../../../../../resources/images/print_version.gif"]'


browser = webdriver.Firefox()
browser.get('https://webapps1.cityofchicago.org/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/begin.do?agencyId=city')
bid_option = browser.find_element_by_xpath(bid_option_xpath)
bid_option.click()

to_date = browser.find_element_by_id(to_date_id)
to_date.send_keys('12/03/2013')

from_date = browser.find_element_by_id(from_date_id)
from_date.send_keys('12/03/2012')

search_button = browser.find_element_by_xpath(search_button_xpath)
search_button.click()

print_version_button = browser.find_element_by_xpath('//img[@src="/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/../../../../../resources/images/print_version.gif"]')
print_version_button.click()


