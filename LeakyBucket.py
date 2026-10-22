size = int(input("Enter the bucket size: "))
rate = int(input("Enter the Output rate: "))
n = int(input("Enter the Time interval: "))

bucket = 0
for i in range(n):
    incoming = int(input("incoming packets: "))
    if incoming + bucket > size:
        dropped = (incoming + bucket) - size
        bucket = size
    else:
        dropped = 0
        bucket += incoming
    sent = min(bucket,rate)    
    bucket -= sent
    print("time: ",i+1)
    print("spent: ",sent)
    print("dropped",dropped)
    print("remaining",bucket)