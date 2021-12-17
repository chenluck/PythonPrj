'''def sum(x):
    if x > 99:
        return 0
    else:
        count = sum(x + 2)
        return x + count
print(sum(1))'''
import turtle
i = 1
turtle.fillcolor('red')
turtle.color('red')
turtle.begin_fill()
while i <= 5:
    turtle.fd(100)
    turtle.right(144)
    i += 1
turtle.end_fill()
turtle.done()
