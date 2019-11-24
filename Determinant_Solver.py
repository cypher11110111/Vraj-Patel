# "4 by 4 Determinant Solver"
Numbers = {}
for i in range(0,16):
    Numbers[i] = int(input("Enter the " + str(i) + "th number:"))
a = Numbers[5] * (Numbers[10] * Numbers[15] - Numbers[14] * Numbers[11])
b = Numbers[6] * (Numbers[9] * Numbers[15] - Numbers[11] * Numbers[13])
c = Numbers[7] * (Numbers[9] * Numbers[14] - Numbers[10] * Numbers[13])
d = Numbers[0]
e = d*(a-b+c)

f = Numbers[4] * (Numbers[10] * Numbers[15] - Numbers[14] * Numbers[11])
g = Numbers[6] * (Numbers[8] * Numbers[15] - Numbers[11] * Numbers[12])
h = Numbers[7] * (Numbers[8] * Numbers[14] - Numbers[10] * Numbers[12])
i = Numbers[1]
j = i*(f-g+h)

k = Numbers[4] * (Numbers[9] * Numbers[15] - Numbers[13] * Numbers[11])
l = Numbers[5] * (Numbers[8] * Numbers[15] - Numbers[11] * Numbers[12])
m = Numbers[7] * (Numbers[8] * Numbers[13] - Numbers[9] * Numbers[12])
n = Numbers[2]
o = n*(k-l+m)

p = Numbers[4] * (Numbers[9] * Numbers[14] - Numbers[13] * Numbers[10])
q = Numbers[5] * (Numbers[8] * Numbers[14] - Numbers[10] * Numbers[12])
r = Numbers[6] * (Numbers[8] * Numbers[13] - Numbers[9] * Numbers[12])
s = Numbers[3]
t = s*(p-q+r)

u = e-j+o-t

print(str(Numbers[0]) + ' ' + str(Numbers[1]) + ' ' + str(Numbers[2]) + ' ' + str(Numbers[3]))
print(str(Numbers[4]) + ' ' + str(Numbers[5]) + ' ' + str(Numbers[6]) + ' ' + str(Numbers[7]))
print(str(Numbers[8]) + ' ' + str(Numbers[9]) + ' ' + str(Numbers[10]) + ' ' + str(Numbers[11]))
print(str(Numbers[12]) + ' ' + str(Numbers[13]) + ' ' + str(Numbers[14]) + ' ' + str(Numbers[15]))

print("""
Your answer is:""",u)







