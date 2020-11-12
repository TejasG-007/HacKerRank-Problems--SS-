def isPrime(num):#check weather number is prime or not
    if num<=1:
        return False
    for itr in range(2,num):
        if num%itr == 0:
            return False
    return True
"""
===Output===
case:1
5
1 2 3 4 5
Not Prime
-----------
case:2
6
6 4 3 2 1
Not Prime
"""
length = int(input())
array = list(map(int,input().split()))[:length]
temp = 0#sum of odd number
for itr in array:
    if itr%2!=0:
        temp+=itr
#passing temp as arg to the isPrime function on printing the output
if(isPrime(temp)):
    print("Prime")
else:
    print("Not Prime")
#code written by TejasG
