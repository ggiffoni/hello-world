import turtle
def polygon(t, length, n):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


polygon("bob", 10, 30)

turtle.mainloop()