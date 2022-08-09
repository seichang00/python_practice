#

def sockMerchant(n, ar):
    socks = dict()
    pairNum = 0
    for sock in ar:
        if sock in socks.keys():
            socks[sock] += 1
        else:
            socks[sock] = 1
    for key in socks.keys():
        pairNum += socks[key]//2
    return pairNum