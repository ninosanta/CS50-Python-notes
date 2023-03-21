def main():
    sentence = input("Input: ")
    print(playback(sentence))


def playback(s):
    return s.strip().replace(" ", "...")


if __name__ == "__main__":
    main()