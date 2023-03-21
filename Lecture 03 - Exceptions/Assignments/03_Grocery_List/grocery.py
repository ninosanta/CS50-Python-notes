def main():
    items = {}
    while True:
        try:
            item = get_item()
        except EOFError:  # Ctrl-D
            print("  ")  # otherwise the prompt is on Item: ^D
            break
        if item == "":
            continue
        items[item] = items.get(item, 0) + 1

    for item in sorted(items):
        print(items[item], item)



def get_item():
    return input("Item: ").strip().upper()


if __name__ == "__main__":
    main()