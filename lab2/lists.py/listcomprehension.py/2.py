fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist2 = [x for x in fruits if x != "apple"]
newlist3 = [x for x in fruits]
newlist4 = [x for x in range(10)]
newlist5 = [x for x in range(10) if x < 5]
newlist6 = [x.upper() for x in fruits]
newlist7 = ['hello' for x in fruits]
newlist8 = [x if x != "banana" else "orange" for x in fruits]
