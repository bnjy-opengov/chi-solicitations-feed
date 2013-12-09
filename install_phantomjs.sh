#!/bin/sh
wget https://phantomjs.googlecode.com/files/phantomjs-1.9.1-linux-x86_64.tar.bz2 -O ~/phantomjs-1.9.1-linux-x86_64.tar.bz2
cd ~
tar -xjvf ~/phantomjs-1.9.1-linux-x86_64.tar.bz2
sudo cp ~/phantomjs-1.9.1-linux-x86_64/bin/phantomjs /usr/bin/
rm -rf ~/phantomjs-1.9.1-linux-x86_64*
