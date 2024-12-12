def fun(x,k,y):
    
    return (x**k)%y

def main():
    x=int(input("ENter value of x"))
    y=int(input("ENter value of y"))
    k=int(input("Enter value of k"))
    
    print("VALue is ",fun(x,k,y))

if __name__ == "__main__":
    main()