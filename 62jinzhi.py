import string
from pathlib import Path

chrzone = string.digits + string.ascii_lowercase + string.ascii_uppercase

def from62to10(target):
    if type(target) is str:
        res = 0
        tmp = target[::-1]
        for i in tmp:
            di = 62 ** tmp.index(i)
            res += chrzone.index(i) * di
        return res
    return None


def loadfrompics():
    store = []
    p = Path('./pics')
    for item in p.iterdir():
        try:
            res = int(item.name[:8],16)
        except:
            res = from62to10(item.name[:8])
        if res not in store:
            store.append(res)
            print('https://weibo.com/' + str(res))
    print(len(store))
    
loadfrompics()