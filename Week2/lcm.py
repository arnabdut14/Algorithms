# Uses python3
def cal_gcd(a,b):
    if b == 0:
        return a
    else:
        r= a%b
        return int(cal_gcd(b,r))

def cal_lcm(in1, in2):
    product = in1 * in2
    lcm = product/(cal_gcd(in1, in2))
    return int(lcm)

if __name__ == "__main__":
    a, b = (input().split())
    print(cal_lcm(int(a), int(b)))