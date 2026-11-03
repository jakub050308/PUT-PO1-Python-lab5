key = (-int(input())) % 26
msg = input()
answer = ""

for t in msg:
    temp = ord(t)
    temp = int(temp)
    if temp <= ord('Z') and temp >= ord('A'):
        temp += key
        while temp > ord('Z'):
            temp -= 26
    elif temp <= ord('z') and temp >= ord('a'):
        temp += key
        while temp > ord('z'):
            temp -= 26
    temp = chr(temp)
    answer += str(temp)

print(answer)