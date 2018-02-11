# test list:
#a = [12, -30, 23, -43, 51]
# input...
a = []
for n in range(20):
    y = input()
    a.append(y)
# initialize variables...
n = 0
m = 0
mm = 0
allMin = 0
# evaluating average...
for b in a:
    if b < 0:
        allMin += b
        n += 1
    print(b)
mm = float(allMin) / n
# modifiyng list...
b = 0
while b < len(a):
    a[b] -= mm
    b += 1
# result:
print "allMin =", allMin
print "arithmetic mean =", mm
print(a)
