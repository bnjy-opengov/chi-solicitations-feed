chi-solicitations-feed
======================

The City of Chicago publishes [vendor, contract, and payment information](https://webapps1.cityofchicago.org/VCSearchWeb/org/cityofchicago/vcsearch/controller/agencySelection/begin.do?agencyId=city) but the data is hidden behind a search form and formatted in a human-readable format. We are interested in liberating this data in a machine-readable format such as JSON so that it can be consumed by other applications.

* [Solicitations](https://webapps1.cityofchicago.org/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/begin.do?agencyId=city) - This website distinguishes solicitations into several types: bids, construction, demolition, proposal, and salvage

Technology
==========

* [Web Automation and Capture](https://github.com/bnjy-opengov/chi-solicitations-feed/wiki/Web-Automation-and-Capture)
* [HTML Scraping](https://github.com/bnjy-opengov/chi-solicitations-feed/wiki/HTML-Scraping)
* [Setup on Amazon EC2](https://github.com/bnjy-opengov/chi-solicitations-feed/wiki/Setup-on-Amazon-EC2)

Initial Setup
=============

Install Firefox - http://www.mozilla.org/en-US/firefox/new/

Mac OS X & Ubuntu
-----------------
Libraries for this app will be managed with pip and virtualenv.  If they aren't installed open a command prompt and run the following:

```
sudo easy_install pip
sudo pip install virtualenv
```

After you clone the repo, create/enable the virtualenv and install all the dependencies.  Running:

```
source use_virtual_env.sh
```

will do both.  You should see (vEnv) at the beginning of your command prompt.

To run the application from the command line run:

```
python driver.py
```


Windows
--------
There is a very easy to follow guide to installing Python and [Selenium](http://docs.seleniumhq.org/) for Windows at the [Selenium Python Bindings documentation site](http://selenium-python.readthedocs.org/en/latest/installation.html#detailed-instructions-for-windows-users).






