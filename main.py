a = [3,5,6,9,1,8,]
k = sorted(a)
b = 0
c = len(a)
g = 0
for i in a:
    b = b + i
g = b / c
print(g)
if  c % 2 == 0:
    k1 = True
else:
    k1 = False
if not k1:
    j = c // 2
    print(k[j])
if k1:
  io =  c // 2
  ia = io - 1
  j = (k[io] + k[ia]) / 2
  print(j)



