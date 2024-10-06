# CS161 Fundamentals of AI HW 1
## Name: Parsa Hajipour
## UID: 605966253

### Question 1
Here is the following code for the python function.

```
def PAD(num):
    # pad(n) = pad(n-2) + pad(n-3) for n >= 3
    # pad(0) = pad(1) = pad(2) = 1
    if num == 0 or num == 1 or num == 2:
        return 1
    return PAD(num-2) + PAD(num-3)
```

### Question 2
Here is the following code for the python function.

```
def SUMS(num):
    if num == 0:
        return 0
    return 1 + SUMS(num-1)
```

### Question 3
Here is the following code for the python function.

```
def ANON(str_list):
    if type(str_list) is not tuple:
            return "?"
    return tuple(ANON(i) if type(i) is tuple else "?" for i in str_list)
```