def main():
    #write your code below this line
    strings = []

    strings.append("First")
    strings.append("Second")
    strings.append("Third")

    print(strings)

    remove_last(strings)
    remove_last(strings)

    print(strings)

def remove_last(strings):
    if (len(strings) == 0):
        return
    else:
        strings.pop(-1)

if __name__ == '__main__':
    main()
