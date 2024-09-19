from struct_ import UnorderedList

test = UnorderedList()

for i in range(1, 101):
    test.add(i)

print(test.size())
print(test.remove(56))
print(test.search(56))
