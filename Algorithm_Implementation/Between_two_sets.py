def getTotalX(a, b):
    # we use result to store the count of integers
    result = 0
    # we iterate through the maximum element of a to the minimum b + 1
    for i in range(max(a),min(b)+1):
        # a bool value to keep track of if it is a multiple
        isFactorMutiple = True  
        # for every element in a array 
        for ele in a:
            # if i mod ele is not equal to zero 
            if i%ele != 0:
                isFactorMutiple = False
                break
        # for every element in array b if ele mod i is not equal to 0 then it is not a factormultiple
        for ele in b:
            if ele % i!=0:
                isFactorMutiple = False
                break
        
        if isFactorMutiple == True:
            result += 1
    
    return(result)
  
  #    ************************************************************************  #
  
  
#explanation 
2 , 6 
24,36 


loop 1: 

i = 6  ------ 25 

	inner loop 1: 
	for ele in [2,6]  [in array a]
		6%2
		6%6 if not equal to zero will set the bit to false
	
	inner loop 2: 
	for ele in [24,36]
		24%6 == 0
		36%6 == 0
	






