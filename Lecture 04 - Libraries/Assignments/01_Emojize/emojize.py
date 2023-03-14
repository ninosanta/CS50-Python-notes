import emoji
import sys


def emojize(str):
    return emoji.emojize(str, language="alias", variant="emoji_type")


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python {sys.argv[0]} <:emoji_str:>")

    print(f"Output: {emojize(sys.argv[1])}")


if __name__ == "__main__":
    main()
