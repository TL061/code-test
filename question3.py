# Question 3
# Time: 35mins

# N: an interger indicating a certain amount (N)
# denominations: a list of denominations
#output: Boolean value indicating whether the given denominations could be used
#        to make up N, assuming infinite number of coins in each denomination.

def question3(N, denominations):
    if (type(N)!=int) or (type(denominations)!=list):
        return "Invalid Type Exception"
    
    if N < 0 or not denominations:
        return False
    
    listComb = [0 for x in range(N+1)] 
    listComb[0]=1
    
    for denomination in denominations:
        
        for i in range(denomination,N+1):
            
                listComb[i]+=listComb[i-denomination]
                #print(str(coin) + " " + str(i) + " " + str(combinations))
    return bool(listComb[N])

# Sample Test Cases:
# question3(11,[1,2,5])
# question3(100,[3,77])
