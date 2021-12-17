def num_neq(a,b,c):
      if a!=b and a!=c and b!=c:
            flag=True
      else:
            flag=False
      return flag

for x in range(1,4):
      for z in range(1,10):
            for y in range(1,10):
                  a1=x*100+y*10+z
                  a2=a1*2
                  a3=a1*3
                  #if (200<a2<700) and (300<a3<1000):
                        #print(a1,a2,a3)
                  a2_1=a2%10
                  a2_2=int(a2/10)%10
                  a2_3=int(a2/100)%10
                  a3_1=a3%10
                  a3_2=int(a3/10)%10
                  a3_3=int(a3/100)%10
                  multi_v=int(x*y*z*a2_1*a2_2*a2_3*a3_1*a3_2*a3_3)
                  if (multi_v == 362880):
                        print(a1, a2, a3, multi_v)
