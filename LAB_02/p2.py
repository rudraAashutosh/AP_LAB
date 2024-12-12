def fun(x,k,y):
    return (power(x,k))%y

def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x

    hp = power(x, y // 2)
    
    
    if y % 2 == 0:
        return hp * hp
    else:
        return hp * hp * x


def main():
    x=int(input("ENter value of x"))
    y=int(input("ENter value of y"))
    k=int(input("Enter value of k"))
    
    print("VALue is ",fun(x,k,y))

if __name__ == "__main__":
    main()