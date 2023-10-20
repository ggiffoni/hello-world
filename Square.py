
import turtle
def square(t, length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)


square("bob", 300)

turtle.mainloop()


