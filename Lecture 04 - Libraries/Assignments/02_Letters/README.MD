# Frank, Ian and Glen’s Letters

[FIGlet](https://en.wikipedia.org/wiki/FIGlet), named after [Frank, Ian, and Glen’s letters](http://www.figlet.org/faq.html), is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:
```ascii
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).

In a file called `figlet.py`, implement a program that:

* Expects zero or two command-line arguments:
    * Zero if the user would like to output text in a *random* font.
    * Two if the user would like to output text in a *specific* font, in which case the first of the two should be `-f` or `--font`, and the second of the two should be the name of the font.
* Prompts the user for a `str` of text.
* Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via `sys.exit` with an error message.