h = [0]*7
for i in range(4):
    h[i] = int(input(f"Data bits {i+1}: "))
h[0] = h[2]^h[4]^h[6]
h[1] = h[2]^h[5]^h[6]
h[3] = h[4]^h[5]^h[6]

print(h)

print("Received data: ")
r = [0]*7
for i in range(7):
    r[i] = int(input(f"Enter actual data{i+1}: "))

p1 = r[0]^r[2]^r[4]^r[6]
p2 = r[1]^r[2]^r[5]^r[6]
p4 = r[3]^r[4]^r[5]^r[6]

error = p1 + (2*p2) + (4*p4)
if error == 0:
    print("No error")
else:
    print(error)
    r[error - 1]^=1
print(h)     
print(r)     