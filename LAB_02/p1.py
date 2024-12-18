def get_first_last_digits(number, m):
    num_str = str(number)
    if len(num_str) <= m:
        return num_str, num_str
    else:
        return num_str[:m], num_str[-m:]
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
    try:
        m = int(input("Enter the value of m: "))
        n = int(input("Enter the value of n: "))
        k = int(input("Enter the value of k: "))

        if m <= 0:
            print("The value of m should be greater than 0.")
            return

        result = power(n,k)
        first_m, last_m = get_first_last_digits(result, m)

        print(f"First {m} digits: {first_m}")
        print(f"Last {m} digits: {last_m}")

    except ValueError:
        print("Please enter valid integers for m, n, and k.")

if __name__ == "__main__":
    main()