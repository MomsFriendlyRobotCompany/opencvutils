#!/bin/sh

set -ex

env

# ls -alhR
# # ls opencv-3.2.0 -alh
# # ls opencv-3.2.0/build -alh
#
# OPENCV_VERSION=3.2.0

if [  ! -d "$OPENCV_INSTALL_DIR/lib"  ];then
	wget https://github.com/opencv/opencv/archive/$OPENCV_VERSION.tar.gz

	# ls -alh
	mv $OPENCV_VERSION.tar.gz opencv-$OPENCV_VERSION.tar.gz
	tar -xzf opencv-$OPENCV_VERSION.tar.gz
	mkdir opencv-$OPENCV_VERSION/build
	cd opencv-$OPENCV_VERSION/build
	cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX="$OPENCV_INSTALL_DIR" .. && make -j2 && make install
# elif [ false ]
# then
# 	ls -aR $HOME/.local
# 	pip install -U --user pyserial
else
	# ls -aR $HOME/.local
	echo  "Using cached opencv $OPENCV_VERSION install."
fi
# # ldconfig
#
# cd $HOME

# cp $HOME/save $HOME/.local
# pip install -U --user pyserial
# ls -alhR $HOME/.local

# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/save/lib
# export PYTHONPATH=$PYTHONPATH:$HOME/save/lib:$HOME/save/lib/python2.7:$HOME/save/lib/python2.7/site-packages
