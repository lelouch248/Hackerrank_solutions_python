def kangaroo(x1, v1, x2, v2):
    # Write your code here
    willMeet = False
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0:
        willMeet = True
    return "YES" if willMeet else "NO"
