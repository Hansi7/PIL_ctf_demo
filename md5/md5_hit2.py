import hashlib
import string


def md5(sss):
    m = hashlib.md5()
    m.update(sss.encode('utf8'))
    return m.hexdigest().upper()


charsList = string.ascii_uppercase + string.digits

s1 = "{}{}{}{}"

for x1 in charsList:
    for x2 in charsList:
        for x3 in charsList:
            for x4 in charsList:
                sx = s1.format(x1, x2, x3, x4)
                if md5(sx)[:10] == 'c2979c7124'.upper():
                    print(sx, md5(sx))
