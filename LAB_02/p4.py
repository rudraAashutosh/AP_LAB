

def toggleKthBit(n, k):
    
    binary_representation = bin(n)[2:]
    print(f"Binary representation of {n}: {binary_representation}")
    
  
    m = 1 << (k - 1)
    result = n ^ m
    
   
    t = bin(result)[2:]
    print(f"Binary representation after toggling {k}-th bit: {t}")
    
    return result
    
def main():
    
    n =int(input("Enter a number ")) 
    k = int(input("Enter the bvalue of k postion "))
    print( toggleKthBit(n , k))
    
if __name__=="__main__":
    main()

