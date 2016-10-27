def pow(A, B, C):
        result = 1
        base = A % C
        while B > 0:
            if B % 2 == 1:
                result = (result*base) % C
            print B, result, base, A
            B = B >> 1
            base = (base*base)%C
        return result%C

print pow(2,5,3)
