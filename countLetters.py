s = input()
s = s.lower()
s = list(s)
counter = [0]*26

for t in s:
    if ord(t)>=ord('a') and ord(t)<=ord('z'):
        counter[ord(t)-97] += 1

hi = max(counter)

for t in range(26):
    if counter[t] == hi:
        print(chr(t+97))
        break
        