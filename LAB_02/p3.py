def check(a,b):
    count=0
    p = []
    for x in range(1,a+1):
        if(a%x==b):
            count += 1
            p.append(x)
        else:
            continue
    return count,p

def main():
    a=int(input("Enter a number "))
    b=int(input("enter another number "))
    
    k,l=check(a,b)
    
    
    print("Number of values satisfying the condition a%x =b are",k)
    
    for x in l:
        print(x)

if __name__=="__main__":
    main()
        