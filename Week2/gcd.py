# Uses python3
def cal_gcd(a,b):
    if b == 0:
        return a
    else:
        r= a%b
        return cal_gcd(b,r)


if __name__ == "__main__":
    a, b = (input().split())
    print(cal_gcd(int(a), int(b)))

