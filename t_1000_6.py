x0=0
x1=0
x2=0
count=0
number=0

for x2 in range(10):
      for x1 in range(10):
            for x0 in range(10):
                  number=x2*100 + x1*10 + x0
                  if x2!=6 and x1!=6 and x0!=6:
                        count=count+1
                  else:
                        print(number)
count=1000-count
print(count)
