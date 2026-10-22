def solving(data):
    if len(data) == 3:
        d3,d2,d1 = data
        p1 = d1 ^ d2
        p2 = d1 ^ d3
        p3 = d2 ^ d3
        result = [d3,d2,p3,d1,p2,p1]

        byte = str(p3) + str(p2) + str(p1)
        return result,byte 
    
    elif len(data) == 4:
        d4,d3,d2,d1 = data
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4
        result = [d4,d3,d2,p3,d1,p2,p1]

        byte = str(p3) + str(p2) + str(p1)
        return result,byte 
    
    elif len(data) == 5:
        d5,d4,d3,d2,d1 = data
        p1 = d1 ^ d2 ^ d4 ^ d5
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4
        p4 = d5
        result = [d5,p4,d4,d3,d2,p3,d1,p2,p1]

        byte = str(p4) + str(p3) + str(p2) + str(p1)
        return result,byte 


data = list(map(int,input("Enter data: ")))
print(f"Actual Data - {data}")
res, byt = solving(data)
print(f"Hamming Code - {res}")
print(f"Parity Code - {byt}")
