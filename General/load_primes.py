def load_primes():
    lst = []
    x = open("../100000.txt", 'r')
    for i in x:
        k = i.split(sep="   ")
        k[-1] = k[-1][:-1]
        for j in k:
            flag = False
            # print(j)
            if j == '':
                continue
            if len(j) > 6:
                m = j.split(' ')
                for l in m:
                    if l != '':
                        if int(l) < 10 ** 6:
                            lst.append(int(l))
                            flag = True
                        else:
                            x.close()
                            return lst
            if not flag:
                lst.append(int(j))


print(load_primes())