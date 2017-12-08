#! /usr/bin/env python2.7
from multiprocessing import Pool
from pylab import linspace, logspace
import subprocess

def RunSingleModel(param):
  pre = param[0]
  nh3 = param[1]
  script = ['./run_rh.ex',
      '-i', 'PJ4_lat_m19.5.inp',
      '-g', '%s %s' % (pre, nh3)
      ]
  fname = '171207/run_rh_p%07.2f_n%05.3f.save' % (pre, nh3)
  with open(fname, 'w') as file:
    subprocess.Popen(script, stdout = file, stderr = file).communicate()
  print script, ' done.'

if __name__ == '__main__':
  nh3_grid = linspace(0.5, 1, 50, endpoint = False)
  pre_grid = logspace(0, 3, 101)
  nthreads = 20
  param = []
  for pre in pre_grid:
    for nh3 in nh3_grid:
      param.append((pre, nh3))
  pool = Pool(nthreads)
  pool.map(RunSingleModel, param)
