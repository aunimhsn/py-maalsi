from sty import fg, FgRegister
from random import randint

def generate_rgb() -> tuple[int, int, int]:
    return randint(0, 255), randint(0, 255), randint(0, 255)


def generate_color(red:int, green:int, blue:int) -> FgRegister:
    color = fg(red, green, blue)
    return color

text = "Hello World!"
print(generate_color(*generate_rgb()), text, fg.rs)
