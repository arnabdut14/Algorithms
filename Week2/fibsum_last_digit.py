# Uses python3
def fibsum_ld(n):
    fib_list =[0,1]
    index = 60
    n %= index
    print(n)
    for i in range (n+1):
        fib_list.append((fib_list[-1]+fib_list[-2])% 10)
    return (fib_list[-1] -1) % 10
    

if __name__ == "__main__":
    n =input()
    print(fibsum_ld(int(n)))