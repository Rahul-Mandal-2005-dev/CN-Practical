
print("Hamming Code Error Detection for 4 bit")
d4,d3,d2,p3,d1,p2,p1 = list(map(int,input("Enter 7 bit data: ")))
Received = [d4,d3,d2,p3,d1,p2,p1]
print("Recevied data: ",Received)

P1 = d1 ^ d2 ^ d4 ^ p1
P2 = d1 ^ d3 ^ d4 ^ p2
P3 = d2 ^ d3 ^ d4 ^ p3


byte = str(P3) + str(P2) + str(P1)
byte_no = int(byte,2)
print(f"Error Position {byte_no} - {byte}")

Correct = Received.copy()
idx = 7 - byte_no

if byte_no != 0:
    Correct[idx] ^=1

print("Correct",Correct)