#!/usr/bin/python

# MIT License
#
# Copyright (c) 2018-2020 Stefan Chmiela, Luis Galvez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import scipy as sp
import multiprocessing as mp
from functools import partial
from scipy import spatial
import timeit
import os
import sys


def create_descriptor(use_descriptor, max_processes=None, *args, **kwargs):

    if use_descriptor == 'Pdist':
        from .descriptors.pdist import Pdist
        desc = Pdist(args['n_atoms'], max_processes, *args)
    elif use_descriptor  == 'Pdist_alpha':
        from .descriptors.pdist_alpha import Pdist_alpha
        desc = Pdist_alpha(args['n_atoms'], max_processes, *args)
    else:
        raise ValueError('This module does not exist in the library')

    return desc


class Desc():

    def __init__(self):
        pass


        


        
        
        








