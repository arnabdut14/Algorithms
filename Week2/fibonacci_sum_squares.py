#uses python3
def fib_sum_squares(n):
    fib_list =[0,1]
    for i in range (2, n+2):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return (fib_list[-1] * fib_list[-2])%10

if __name__ == "__main__":
    n=int(input())
    print(fib_sum_squares(n))