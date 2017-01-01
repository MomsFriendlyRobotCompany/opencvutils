#!/bin/sh

set -ex

ls -alh

wget https://github.com/opencv/opencv/archive/3.2.0.tar.gz

ls -alh
mv 3.2.0.tar.gz opencv-3.2.0.tar.gz
tar -xzvf opencv-3.2.0.tar.gz
mkdir opencv-3.2.0/build
cd opencv-3.2.0/build && cmake .. && make && make install
