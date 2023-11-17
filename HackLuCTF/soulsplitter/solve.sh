#!/bin/sh

# As per https://stackoverflow.com/a/73688799/15272584
if brew list | grep zbar > /dev/null; then
	ZBAR_EXISTS=1
else
	echo "Installing zbar..."
	brew install zbar
fi
if [ -d '~/lib' ]; then
	LIB_EXISTS=1
else
	mkdir -p ~/lib
fi
if [ -L '~/lib/libzbar.dylib' ]; then
	ZBAR_LIB_EXISTS=1
else
	ln -sf $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
fi

# Create venv
python3 -m venv venv
mkdir venv/home
cp files/* venv/home
cd venv/home
source ../bin/activate
pip3 install -r requirements.txt

# Solve (might take a few tries)
while ! python3 solve.py; do :; done

# Clean up
cd ../..
rm -r venv
if [ -z "$ZBAR_LIB_EXISTS" ]; then rm ~/lib/libzbar.dylib; fi
if [ -z "$LIB_EXISTS" ]; then rm -r ~/lib; fi
if [ -z "$ZBAR_EXISTS" ]; then brew uninstall zbar; fi
