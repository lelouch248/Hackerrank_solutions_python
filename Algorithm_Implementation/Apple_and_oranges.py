def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_length = len(apples)
    oranges_length = len(oranges)
    a_count,o_count = 0,0
    
    for i in range(apple_length):
        if a+apples[i] >= s and a+apples[i]<=t:
            a_count+=1 
    for i in range(oranges_length):
        if b+oranges[i]>=s and b+oranges[i]<=t:
            o_count+=1
