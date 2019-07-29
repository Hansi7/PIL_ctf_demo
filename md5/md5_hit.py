import hashlib
import string

m = hashlib.md5()


def md5(sss):
    m.update(sss.encode('utf8'))
    return m.hexdigest().upper()


charsList = string.ascii_uppercase + string.digits

s1 = "TASC{}O3RJMV{}WDJKX{}ZM"
md5_var = "E903???4DAB????08?????51?80??8A?"

for x1 in charsList:
    for x2 in charsList:
        for x3 in charsList:
            sx = s1.format(x1, x2, x3)
            # print(sx, md5(sx))
            if md5(sx)[:4] == 'E903':
                print(sx, md5(sx))
