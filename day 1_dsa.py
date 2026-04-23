#sum
def solveMeFirst(a,b):
    r=a+b
    return r
	# Hint: Type return a+b below
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#sum of array
def simpleArraySum(ar):
    r = 0
    for i in ar:
        r+=i
    return r    


#compare the triplets
def compareTriplets(a, b):
    # Write your code here
    A=0
    B=0
    for i in range(0,3):
        if a[i]>b[i]:
            A+=1
        elif a[i]<b[i]:
            B+=1         
    return [A,B]

#diagonal difference
def diagonalDifference(arr):
    n=len(arr)
    r1=0
    r2=0
    for i in range(0,n):
        for j in range(0,n):
            
            if i==j:
                r1+=arr[i][j]
            if i+j == n-1:
                r2+=arr[i][j]
    return abs(r1-r2)

#plus minus
def plusMinus(arr):
    n = len(arr)
    ne=0
    p=0
    z=0
    for i in arr:
        if i<0:
            ne+=1
        elif i>0:
            p+=1
        else:
            z+=1
    print(p/n)
    print(ne/n)
    print(z/n)

    #staircase
    def staircase(n):
    for i in range(1, n+1):
        for k in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print("#",end="")
        print()

        #a very big sum
        def aVeryBigSum(ar):
    r=0
    for i in ar:
        r+=i
    return r
    
    
    

