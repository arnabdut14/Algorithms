# Uses python3
def fib_sum_last_digit(m, n):
    fib_list =[0,1]
    index = 60
    right = n % index
    left = m % index 
    result = 0
    if right < left:
        right += index
    for i in range (index -2):
        fib_list.append((fib_list[-1]+fib_list[-2])% 10)
    for i in range (left, right +1):
        result += fib_list[i % index]
    return result % 10
    

if __name__ == "__main__":
    m,n =input().split()
    print(fib_sum_last_digit(int(m), int(n)))