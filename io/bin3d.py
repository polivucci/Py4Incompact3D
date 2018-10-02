"""
       FILE: bin3d.py
     AUTHOR: Paul Bartholomew <paul.bartholomew08@imperial.ac.uk>
DESCRIPTION: Provides tools to load xcompact3d bindary data into numpy arrays.
"""

import numpy as np
from xcompact3d_tools.tools.fortran import colidx_from_rowijk

def read_i3d_data(filename, nx, ny, nz, dtype=np.float64):
	"""Reads a datafile generated by Incompact3D into a numpy array. """
	
	N = nx * ny * nz

	phi = []
	ctr = 0

	with open(filename, "rb") as bindat:
		fldat = np.fromfile(bindat, dtype)
		assert(len(fldat) == N)
		
		for i in range(nx):
			phi.append([])
			for j in range(ny):
				phi[-1].append([])
				for k in range(nz):
					idx = ctr
					phi[-1][-1].append(fldat[idx])
					ctr += 1

	assert(ctr == N)
		
	return phi