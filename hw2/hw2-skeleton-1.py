##############
# Homework 2 #
##############

##############
# Question 1 #
##############

# TODO: comment code
def BFS(FRINGE):
    if not isinstance(FRINGE, tuple):
        return (FRINGE,)
    queue = [FRINGE]
    res = ()
    while queue:
        current = queue.pop(0)
        for i in current:
            if isinstance(i, tuple):
                queue.append(i)
            else:
                res += (i,)
    return res

##############
# Question 2 #
##############


# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS returns [].
# To call DFS to solve the original problem, one would call
# DFS((False, False, False, False), [])
# However, it should be possible to call DFS with a different initial
# state or with an initial path.

# First, we define the helper functions of DFS.

# FINAL-STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    if S == (True, True, True, True):
        return True
    return False


# NEXT-STATE returns the state that results from applying an operator to the
# current state. It takes three arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns None.
# NOTE that next-state returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].
def NEXT_STATE(S, A):
    new_state = list(S)

    if A == "h":
        new_state[0] = not new_state[0]  # Move Homer
    elif A == "b":
        new_state[0] = not new_state[0]  # Move Homer
        new_state[1] = not new_state[1]  # Move baby
    elif A == "d":
        new_state[0] = not new_state[0]  # Move Homer
        new_state[2] = not new_state[2]  # Move dog
    elif A == "p":
        new_state[0] = not new_state[0]  # Move Homer
        new_state[3] = not new_state[3]  # Move poison
    else:
        return None  # Invalid entity

    # Check for invalid state conditions
    if (new_state[1] == new_state[2] and new_state[0] != new_state[1]):
       return None
    if (new_state[1] == new_state[3] and new_state[0] != new_state[1]):
       return None

    return [(tuple(new_state))]


# SUCC-FN returns all of the possible legal successor states to the current
# state. It takes a single argument (s), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    res = []
    actions = ["h", "b", "d", "p"]

    for a in actions:
        temp = NEXT_STATE(S, a)
        if temp is not None:
            res += temp
    
    return res


# ON-PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if s is a member of
# states and False otherwise.
def ON_PATH(S, STATES):
    return S in STATES


# MULT-DFS is a helper function for DFS. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT-DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT-DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    for state in STATES:
        if FINAL_STATE(state):  # Check if the current state is the goal
            return PATH + [state]  # Return the complete path to the goal
        
        if not ON_PATH(state, PATH):  # Check if the state has already been visited
            new_path = PATH + [state]  # Create a new path including the current state
            # Get the successor states for the current state
            successor_states = SUCC_FN(state)
            # Recursive call to continue the DFS
            result = MULT_DFS(successor_states, new_path)
            if result:  # If the result is not empty, a path to the goal was found
                return result  # Return the successful path

    return []


# DFS does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path.
def DFS(S, PATH):
    if FINAL_STATE(S):
        return PATH + [S]  # Return the path including the goal state

    # Check if the current state is already on the path to avoid cycles
    if ON_PATH(S, PATH):
        return []  # Return an empty list to indicate no path found

    # Add the current state to the path
    new_path = PATH + [S]

    # Get the successor states for the current state
    successor_states = SUCC_FN(S)

    # Iterate through each successor state
    for state in successor_states:
        # Perform DFS on the successor state
        result = DFS(state, new_path)
        if result:  # If a path to the goal was found, return it
            return result

    return []
