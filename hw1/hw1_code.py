def PAD(num):
    # pad(n) = pad(n-2) + pad(n-3) for n >= 3
    # pad(0) = pad(1) = pad(2) = 1
    if num == 0 or num == 1 or num == 2:
        return 1
    return PAD(num-2) + PAD(num-3)

def SUMS(num):
    if num == 0 or num == 1 or num == 2:
        return 0
    return 1 + SUMS(num-2) + SUMS(num-3)

def ANON(str_list):
    if type(str_list) is not tuple:
            return "?"
    return tuple(ANON(i) if type(i) is tuple else "?" for i in str_list)

test1 = ((("L", "E"), "F"), "T")
print (ANON(test1))
