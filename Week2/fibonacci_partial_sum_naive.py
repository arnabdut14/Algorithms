#uses python3
def fibpsum_last_digit(m, n):
    fib_list =[0,1]
    for i in range (2, n+3):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    result = ((fib_list[n+2]-1) - (fib_list[m+1] -1)) % 10
    return result

if __name__ == "__main__":
    m, n = input().split()
    print(fibpsum_last_digit(int(m), int(n)))