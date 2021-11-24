s=input("Enter The input: ")
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)        