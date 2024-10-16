# Name: Parsa Hajipour
# UID: 605966253


# this recursive function outputs the nth padovan number
# the base case checks if N is 0,1 or 2 to return the default value of 1
# otherwise, the function calls itself again to add the n-2 padovan number and n-3 padovan number and returns their sum
def PAD(N):
    if N == 0 or N == 1 or N == 2:
        return 1
    return PAD(N-2) + PAD(N-3)


# this recursive function outputs the number of plus operations that were conducted
# the base case checks if N is 0,1, or 2 to return the default value of 0 since no additions were made
# otherwise the function returns one plus the number of addition operations for n-2 and n-3
def SUMS(N):
    if N == 0 or N == 1 or N == 2:
        return 0
    return 1 + SUMS(N-2) + SUMS(N-3)

# this recursive function outputs every item within potentially nested tuples as "?"
# the base case is if the input is not a tuple, then just return a "?"
# otherwise go through the tuple, and if you find another tuple, call the function again on the sub-tuple or switch the item to a "?"
def ANON(str_list):
    if type(str_list) is not tuple:
            return "?"
    return tuple(ANON(i) if type(i) is tuple else "?" for i in str_list)

