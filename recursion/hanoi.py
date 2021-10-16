def move(S, T):
    print('Move from {} to {}'.format(S, T))

def hanoi(n, S, H, T):

    if(n>0):
        hanoi(n-1, S, T, H)
        move(S, T)
        hanoi(n-1, H, S, T)

hanoi(2, 'A', 'B', 'C')