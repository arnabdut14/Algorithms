#uses python3
def fib_mod(n,m):
    fib_list =[0,1]
    count = 1
    index = 0
    remainder = 0
    i = 2
    while count < 2:
        fib_list.append((fib_list[i - 1] + fib_list[i - 2]) % m)
        if fib_list[i] == 1 and fib_list[i-1] == 0:
            count += 1
            index = i -1
        i += 1
    if count == 2:
        remainder = n % index
    return fib_list[remainder]

if __name__ == "__main__":
    n,m =input().split()
    print(fib_mod(int(n), int(m)))
