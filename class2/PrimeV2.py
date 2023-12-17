def is_prime(n):
    total=0
    for i in range(n):
        if n%(i+1)==0:
            total+=1
            print(total)
    if total ==2:
        return True
    else:
        return False
n=int(input("pls type a num: "))
print(is_prime(n))     


# the bigO is O(n)