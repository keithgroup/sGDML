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
from sgdml.utils.descriptors import Pdist
from sgdml.utils.descriptors import Pdist_alpha





class Desc(object):
    def __init__(self, descriptor, n_atoms = None, max_processes=None):
        if (descriptor == 'pdist'):
            pdist(n_atoms,max_processes)
        if (descriptor == 'pdist_alpha'):
            pdist_alpha(n_atoms,max_processes)
            
    def pdist(self, n_atoms, max_processes=None):
        desc = Pdist(n_atoms,max_processes)
        return desc

    def pdist_alpha(self, n_atoms, alpha, max_processes=None):
        desc = Pdist_alpha(n_atoms,max_processes)
        return desc

        


        
        
        








