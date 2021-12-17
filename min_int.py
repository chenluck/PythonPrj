'''import math
def sum(k):
      s=0
      for i in range(1,int(math.sqrt(k))+1):
            if k%i==0:
                  s=s+2
            if k==i*i:
                  s=s-1
      return s
k=int(input("please input k:"))
for i in range(1,50001):
      if sum(i)==k:
            print(i)
            exit()'''

import math
def sum(k):
      s=0
      for i in range(1,k+1):
            if k%i==0:
                  s=s+1
      return s

k=int(input("please input k:"))
for i in range(1,50001):
      if sum(i)==k:
            print(i)
            break
