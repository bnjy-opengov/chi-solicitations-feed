#!/bin/sh
wget https://phantomjs.googlecode.com/files/phantomjs-1.9.1-linux-x86_64.tar.bz2 -O ~/Downloads/phantomjs-1.9.1-linux-x86_64.tar.bz2
cd ~/Downloads/
tar -xjvf ~/Downloads/phantomjs-1.9.1-linux-x86_64.tar.bz2
sudo cp ~/Downloads/phantomjs-1.9.1-linux-x86_64/bin/phantomjs /usr/bin/
