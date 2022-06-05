#!/usr/bin/python3
    if __name__ == "__main__":
        import ele
        l = len(ele.argv) - 1

        if l == 0:
        print("{} arguments.".format(l))
    elif l == 1:
        print("{} argument:".format(l))
    else:
        print("{} arguments:".format(l))

    if l >= 1:
        l = 0
        for arg in ele.argv:
            if l != 0:
                print("{}: {}".format(i, arg))
            l += 1

