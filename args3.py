l = [1, 2, 3, 4, 5]
*head, tail =l
print("head",head)
print("tail",tail)
head, *tail =l
print("head",head)
print("tail",tail)

string = "Hello!"
*start, last = string
print("start",start)
print("last",last)

# You can have more than two variable names on the left, but only one asterisk.
a, b, *c, d = range(5)
print("a : ", a)
print("b : ", b)
print("c : ", c)
print("d : ", d)