key = [int(x) for x in input().split()]
if len(key) == 0 or len(key) == 1:
    print(True)
else:
    skey = sorted(key)
    step = skey[0]-skey[1]
    count = 1
    for i in range(1, len(skey)-1):
        if skey[i] - skey[i+1] == step:
            count += 1

    if count == len(skey)-1:
        print(True)
    else:
        print(False)
