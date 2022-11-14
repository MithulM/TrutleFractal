from turtle import *


def recLgrammar(t, axiom, angle, gen, size, states=[], **Lgrammar):
    for command in axiom:
        if gen:
            match command:
                case "X" | "Y" | "U" | "V" | "F" | "f":
                    recLgrammar(t, Lgrammar[command], angle,
                                gen - 1, size, states, ** Lgrammar)
                case "[":
                    states.append((*t.pos(), t.heading()))
                case "]":
                    x, y, h = states.pop()
                    t.penup()
                    t.setpos(x, y)
                    t.setheading(h)
                    t.pendown()
                case "+":
                    t.right(angle)
                case "-":
                    t.left(angle)
                case _:
                    pass
        else:
            match command:
                case "F":
                    t.forward(size)
                case "f":
                    t.penup()
                    t.forward(size)
                    t.pendown()
                case "[":
                    states.append((*t.pos(), t.heading()))
                case "]":
                    x, y, h = states.pop()
                    t.penup()
                    t.setpos(x, y)
                    t.setheading(h)
                    t.pendown()
                case "+":
                    t.right(angle)
                case "-":
                    t.left(angle)
                case _:
                    pass


def iterLgrammar(t, axiom, angle, gen, size, **Lgrammar):
    for _ in range(gen):
        temp = ""
        for command in axiom:
            temp += Lgrammar[command] if command in Lgrammar else command
        axiom = temp
    states = []
    for command in axiom:
        match command:
            case "X" | "Y" | "U" | "V":
                pass
            case "F":
                t.forward(size)
            case "f":
                t.penup()
                t.forward(size)
                t.pendown()
            case "[":
                states.append((*t.pos(), t.heading()))
            case "]":
                x, y, h = states.pop()
                t.penup()
                t.setpos(x, y)
                t.setheading(h)
                t.pendown()
            case "+":
                t.right(angle)
            case "-":
                t.left(angle)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    t = Turtle()
    t.speed(0)
    t.pencolor('red')
    t.hideturtle()
    initialHeading = 0

    # Lgrammar values
    gen = 4
    scale = 1 / 3
    windowSize = 500
    size = windowSize * scale ** (gen)
    axiom = "F++F++F"
    Lgrammar = {
        "F": "F-F++F-F",
        "f": "",
        "X": "",
        "Y": "",
        "U": "",
        "V": "",
    }
    angle = 60

    # Test recursive call for Lgrammar
    t.setheading(initialHeading)
    t.penup()
    t.setpos(-windowSize, 0)
    t.pendown()
    iterLgrammar(t, axiom, angle, gen, size, **Lgrammar)

    # Test recursive call for Lgrammar
    t.setheading(initialHeading)
    t.penup()
    t.setpos(windowSize, 0)
    t.pendown()
    recLgrammar(t, axiom, angle, gen, size, **Lgrammar)

    done()
