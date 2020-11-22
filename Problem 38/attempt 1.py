
highest = 0

for i in range(1, 10000):
    sum = ""
    for j in range(1, 10):
        sum += str(i*j)
        if sum[0] != "9":
            continue
        elif len(sum) == 9:
            flag = False
            for k in range(1, 10):
                if str(k) not in sum:
                    flag = True
                    continue
            if flag:
                continue
            if int(sum) > highest:
                highest = int(sum)
                continue
        elif len(sum) > 9:
            continue


print(highest)