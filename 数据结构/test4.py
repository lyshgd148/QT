# from struct import Stack1
#
# st = Stack1()
# st.push(1)
# st.push("sb")
# st.push(2)
# st.push("hh")
# st.push("s")
# st.pop()
# print(st)


from struct_ import Stack

st = Stack()
st.push("1")
st.push("sb")
st.push("2")
st.push("hh")
st.push("s")
st.pop()
print(st.items)
ls = " ".join(st.items)
print(ls)
