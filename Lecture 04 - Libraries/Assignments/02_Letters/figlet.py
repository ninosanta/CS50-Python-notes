import random
from pyfiglet import Figlet
import sys

figlet = Figlet()


def get_input():
    return input("Input: ")


def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} [-f | --font] [font_name]")
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (
            sys.argv[2] not in figlet.getFonts()
        ):
            sys.exit(
                f"Usage: {sys.argv[0]} [-f | --font] [font_name]"
                + "with `font_name` picked among the following fonts:\n"
                + f"{figlet.getFonts()}"
            )
        else:
            f = sys.argv[2]
    else:
        f = random.choice(figlet.getFonts())

    print(f"Using font: {f}")
    figlet.setFont(font=f)
    print(f"Output:\n{figlet.renderText(get_input())}")


if __name__ == "__main__":
    main()
