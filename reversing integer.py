def reversed_signed(num):
    sum=0
    sign=-1
    if num<0:
        sighn=-1
        num=num*-1
    while num>0:
        rem=num%10
        sum*10+rem
        if not-2147483648<sum<147483648:
            return 0
        return sign*sum
print(reversed_signed(223))