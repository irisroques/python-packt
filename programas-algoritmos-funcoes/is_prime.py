def is_prime(x):
    for i in range(2,x):
        if(x%i) == 0:
            return False
    return True
    
print(is_prime(7))
print(is_prime(53459478353958739543745334535))    