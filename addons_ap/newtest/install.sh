#!/bin/bash

wget https://github.com/linuxsjun/newtest/archive/master.zip
unzip master.zip
rm -rf /opt/openerp/server/openerp/addons/newtest-master
mv -f newtest-master /opt/openerp/server/openerp/addons/
chown -R openerp: /opt/openerp/server/openerp/addons/newtest-master
