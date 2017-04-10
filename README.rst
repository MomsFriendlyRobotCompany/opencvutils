OpenCV Utilities
===================

.. image:: https://travis-ci.org/walchko/opencvutils.svg?branch=master
	:target: https://travis-ci.org/walchko/opencvutils
.. image:: https://api.codacy.com/project/badge/Grade/a5cff64a1fcc4cf78bac1f936073c01e
	:target: https://www.codacy.com/app/kevin-walchko/opencvutils?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=walchko/opencvutils&amp;utm_campaign=Badge_Grade
.. image:: https://img.shields.io/pypi/v/opencvutils.svg
	:target: https://pypi.python.org/pypi/opencvutils/
	:alt: Latest Version
.. image:: https://img.shields.io/pypi/l/opencvutils.svg
	:target: https://pypi.python.org/pypi/opencvutils/
	:alt: License


This is  a set of OpenCV utilities that should make working with OpenCV a little
easier.

**Original Author:** Adrian Rosebrock

**Original Name:** `imutils <https://github.com/jrosebr1/imutils>`_


Install
--------

The preferred way to install is using ``pip``::

	pip install opencvutils

Other Libraries
~~~~~~~~~~~~~~~~~

For ``scipy`` on the RPi also do::

	sudo apt-get install libopenblas-dev libatlas-dev libblas-dev liblapack-dev gfortran

Unfortunately this is not fast, ``numpy`` install involves compiling things, so
go grab a coffee or something while you wait.

Development
------------

To submit git pulls, clone the repository and set it up as follows::

	git clone https://github.com/walchko/opencvutils
	cd opencvutils
	pip install -e .

Documentation
---------------

See the `Jupyter Notebooks <https://github.com/walchko/opencvutils/tree/master/docs>`_
for examples of how to use this library.

ToDo
-----

* histogram matching
* document everything

Change Log
-------------

========== ======= =============================
2017-04-09 0.9.0   initial python 3 support
2017-03-31 0.7.0   refactored and got rid of things I don't need
2017-01-29 0.6.0   added video capture (video and images) program
2016-12-30 0.5.3   typo fix
2016-12-30 0.5.1   refactored
2016-12-11 0.5.0   published to PyPi
========== ======= =============================

MIT License
----------------

Copyright (c) 2016 Kevin J. Walchko

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
