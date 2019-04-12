# Question 1:

# Time: 6 mins 
# N: an integer indicating the number of kids
# Output: the array of the correct responses from kids in order
#
def countingGame(N):
    
    arr = list(range(1,N+1))
    ruleDict = {3:"Fizz", 5:"Buzz", 7:"Woof"}

    for key, value in ruleDict.items():
        
        for i in range(key, N+1, key):
            
            if (type(arr[i-1]) == int):
                arr[i-1] = ruleDict[key]
                
            elif (type(arr[i-1]) == str):
                arr[i-1] = arr[i-1] + " " + ruleDict[key]
                
    return print(arr)
   
#
# Sample Test Cases:
#
# countingGame(5)
# countingGame(15)
