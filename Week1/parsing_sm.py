

def state_zero(c):
    if c == 'a':
        return state_one
    return state_zero

def state_one(c):
    if c == 'b':
        return state_two
    elif c == 'a':
        return state_one
    return state_zero

def state_two(c):
    if c == 'c':
        return state_three
    if c == 'a':
        return state_one
    return state_zero

def state_three(c):
    if c == 'd':
        print("Found abcd!")
        return state_four
    if c =='a':
        return state_one
    return state_zero

def state_four(c):
    if c == 'a':
        return state_one
    return state_zero

if __name__ == '__main__':
    text = str(raw_input("Please Enter some Text:\n"))
    state = state_zero
    for c in text:
        state = state(c)
    

