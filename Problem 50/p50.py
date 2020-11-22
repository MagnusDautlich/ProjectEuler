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


primes = load_primes()
longest_sum = [0, 0]

for counter, i in enumerate(primes):
    psum = 0
    len_psum = 0
    if i > 100000:
        break
    for j in range(counter, len(primes)):
        psum += primes[j]
        len_psum += 1
        if psum > 10**6:
            break
        if len_psum > longest_sum[1]:
            if psum in primes:
                if len_psum > longest_sum[1]:
                    longest_sum = [psum, len_psum]
                    print(psum, i)

print(longest_sum)

