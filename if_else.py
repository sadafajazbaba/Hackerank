
if __name__ == '__main__':
    n = int(input())
    if n %2 != 0 and 1<=n<=100:
        print("Weird")
    elif n %2 == 0 and 2<=n<=5:
        print("Not Weird")
    elif n %2 == 0 and 6<=n<=20:
        print("Weird")
    elif n %2 == 0 and 21<=n<=100:
        print("Not Weird")