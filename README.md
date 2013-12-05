chi-solicitations-feed
======================

Wrapping the City of Chicago's publishing of solicitations in a machine-readable way.

Please see this repo's [wiki](https://github.com/bnjy-opengov/chi-solicitations-feed/wiki/Background) for more information.

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
There is a very easy to follow guide to installing Python and Selenium for Windows at the [Selenium Python Bindings documentation site](http://selenium-python.readthedocs.org/en/latest/installation.html#detailed-instructions-for-windows-users).






