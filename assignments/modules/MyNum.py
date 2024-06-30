
def CheckPrime(numbers):
    ans = []
    for i in range(len(numbers)):
        for j in range(2,(numbers[i])):
            if((numbers[i]%j ) != 0):
                ans.append(numbers[i])
    return ans