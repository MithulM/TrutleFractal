from turtle import *

if __name__ == "__main__":
    t = Turtle()
    t.speed(0)
    t.pencolor('red')
    t.hideturtle()
    gen = 4
    scale = 0.5
    windowSize = 500
    size = windowSize * scale ** (gen - 1)
    commands = "[Y]++[Y]++[Y]++[Y]++[Y]"
    Lgrammar = {
        "F": "",
        "f": "",
        "X": "UF++VF----YF[-UF----XF]++",
        "Y": "+UF--VF[---XF--YF]+",
        "U": "-XF++YF[+++UF++VF]-",
        "V": "--UF++++XF[+VF++++YF]--YF",
    }
    rot = 36
    for a in range(gen-1):
        temp = ""
        for command in commands:
            temp += Lgrammar[command] if command in Lgrammar else command
        commands = temp
        print(commands)
    states = []
    t.penup()
    t.setpos(250, 0)
    t.pendown()
    for command in commands:
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
                t.right(rot)
            case "-":
                t.left(rot)
            case _:
                print("Invalid command.")
    done()
