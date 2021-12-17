import sys,matplotlib
import numpy as np, pandas as pd, requests as rq
modules={'Numpy':np,'pandas':pd,'matplotlib':matplotlib,'requests':rq}
print('Python version:%s'%(sys.version))
for i in modules.items():
      print('{} version: {}'.format(i[0], i[1].__version__))
