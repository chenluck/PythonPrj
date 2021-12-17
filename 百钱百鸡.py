n=0
for x in range(34):
      for y in range(101):
            z=100-x-y
            if z>0 and x*3+y/2+z/3==100:
                  print(f'Big {x}, Avg {y}, Small {z}')
                  n+=1
print(f'{ n } method')
