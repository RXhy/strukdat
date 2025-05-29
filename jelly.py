n, s = map(int,input().split())
total = 0 
for i in range(s):
    temp = int(input())
    total += temp

if total <= s:
    print("Yeyy")
else:
    print("Bleh")