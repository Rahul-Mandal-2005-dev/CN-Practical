def SlidingWindow():
    n = int(input("Enter No of frames: "))
    w = int(input("Window Size: "))
    lost = int(input("Lost frame: "))

    print("\n1.Go Back N")
    i = 1
    while i<=n:
        end = min(i+w-1,n)
        print("Sliding Window - ",list(range(i,end+1)))

        if i<=lost<=end:
            print("Loss Frame: ",lost)
            print("Receiver Discared this Window data frame")
            print(f"Retransmission frames: {lost} to {end}")
            print("ACK received: ",list(range(lost,end+1)))
            i = end+1
        else:
            print("ACK received: ",list(range(i,end+1)))
            i = end+1

    print("\n2.Selective Repeat")
    i = 1
    while i<=n:
        end = min(i+w-1,n)
        print("Sliding Window - ",list(range(i,end+1)))
        for frame in range(i,end+1):
            if frame == lost:
                print(f"Frame {frame} is lost Retransmit only this frame")
                print("ACK received for this frame")
            else:
                print(f"Frame {frame} received ACK received") 
        i = end + 1   
SlidingWindow()
     