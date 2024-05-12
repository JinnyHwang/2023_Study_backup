

def cmp(marble):
    _, _, _, w, num = marble
    return(-w, -num)

marbles.sort(key=cmp)





