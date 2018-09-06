#uses python3
def fib_sum_last_digit(n):
    fib_list =[0,1]
    for i in range (2, n+3):
        fib_list.append((fib_list[i-1] + fib_list[i-2])% 10)
    result = fib_list[-1] -1
    return result

if __name__ == "__main__":
    n=int(input())
    print(fib_sum_last_digit(n))
