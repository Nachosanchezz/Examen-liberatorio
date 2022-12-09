s=input("Enter string: ")
k=int(input("Enter key: "))
enc=[[" " for i in range(len(s))] for j in range(k)]
print(enc)
enc = [
    ["D", ".",".", ".", "N", ".", ".", ".", "E", ".", ".", ".", "T", ".", ".", ".", "L", ".", "."],
    [".", "E", ".", "E", ".", "D", ".", "H", ".", "E", ".", "S", ".", "W", ".", "L", ".", "X", "."],
    [".", ".", "F", ".", ".", ".", "T", ".", ".", ".", "A", ".", ".", ".", "A", ".", ".", "X", "."],
]

flag = 0
row = 0

for i in range(len(s)):
    if flag == 0:
        enc[row][i] = s[i]
        row += 1
        if row == k:
            flag = 1
            row -= 2
    else:
        enc[row][i] = s[i]
        row -= 1
        if row == -1:
            flag = 0
            row += 2
for i in range (k):
    for j in range(len(s)):
        print(enc[i][j], end="")
    print()
ct=[]
for i in range(k):
    for j in range(len(s)):
        if enc[i][j]!=' ':
            ct.append(enc[i][j])
cipher="".join(ct)
print("Cipher Text: ",cipher)











