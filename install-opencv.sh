#!/bin/sh

set -ex

ls -alhR
# ls opencv-3.2.0 -alh
# ls opencv-3.2.0/build -alh

wget https://github.com/opencv/opencv/archive/3.2.0.tar.gz

ls -alh
mv 3.2.0.tar.gz opencv-3.2.0.tar.gz
tar -xzf opencv-3.2.0.tar.gz
mkdir opencv-3.2.0/build
cd opencv-3.2.0/build && cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=$HOME/save .. && make -j7 && make install
# ldconfig

cd $HOME

ls -alh -R $HOME/save

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/save/lib
export PYTHONPATH=$PYTHONPATH:$HOME/save/lib/
