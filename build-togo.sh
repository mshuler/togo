#!/bin/bash

./root/usr/local/bin/togomake
./root/usr/local/bin/togobuild

mv `find rpmbuild -name *.rpm` `pwd`
