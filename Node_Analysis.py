Numbers = {}
for i in range(0,12):
    Numbers[i] = int(input("Enter the " + str(i) + "th number:"))
x = Numbers[1] * (Numbers[6] * Numbers[11] - Numbers[7] * Numbers[10])
y = Numbers[2] * (Numbers[5] * Numbers[11] - Numbers[7] * Numbers[9])
z = Numbers[3] * (Numbers[5] * Numbers[10] - Numbers[6] * Numbers[9])
a = x - y + z

q = Numbers[0] * (Numbers[6] * Numbers[11] - Numbers[7] * Numbers[10])
w = Numbers[2] * (Numbers[4] * Numbers[11] - Numbers[7] * Numbers[8])
e = Numbers[3] * (Numbers[4] * Numbers[10] - Numbers[6] * Numbers[8])
b = q - w + e

j = Numbers[0] * (Numbers[5] * Numbers[11] - Numbers[7] * Numbers[9])
k = Numbers[1] * (Numbers[4] * Numbers[11] - Numbers[7] * Numbers[8])
l = Numbers[3] * (Numbers[4] * Numbers[9] - Numbers[5] * Numbers[8])
c = j - k + l

m = Numbers[0] * (Numbers[5] * Numbers[10] - Numbers[6] * Numbers[9])
n = Numbers[1] * (Numbers[4] * Numbers[10] - Numbers[6] * Numbers[8])
o = Numbers[2] * (Numbers[4] * Numbers[9] - Numbers[5] * Numbers[8])
d = m - n + o

Va = b/a
Vb = c/a
Vc = d/a

print("Voltage Va =", Va)
print("Voltage Vb =", Vb)
print("Voltage Vc =", Vc)

