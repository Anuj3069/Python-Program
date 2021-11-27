s=input("Enter some string: ")
a=set(s)
for ch in sorted(a):
    print("{} occurs {} times".format(ch,s.count(ch)))