#!/usr/bin/env bash

set -ex

env

# ls -alhR
# # ls opencv-3.2.0 -alh
# # ls opencv-3.2.0/build -alh
#
if [true]
then
	wget https://github.com/opencv/opencv/archive/3.2.0.tar.gz

	ls -alh
	mv 3.2.0.tar.gz opencv-3.2.0.tar.gz
	tar -xzf opencv-3.2.0.tar.gz
	mkdir opencv-3.2.0/build
	cd opencv-3.2.0/build && cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=$HOME/.local .. && make -j7 && make install
elif [true]
then
	ls -aR $HOME/.local
	pip install -U --user pyserial
else
	ls -aR $HOME/.local
fi
# # ldconfig
#
# cd $HOME

# cp $HOME/save $HOME/.local
# pip install -U --user pyserial
# ls -alhR $HOME/.local

# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/save/lib
# export PYTHONPATH=$PYTHONPATH:$HOME/save/lib:$HOME/save/lib/python2.7:$HOME/save/lib/python2.7/site-packages
