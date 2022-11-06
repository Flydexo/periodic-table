def darker(c):
    c = c.lower()

    c = c.replace("1", "0")
    c = c.replace("2", "1")
    c = c.replace("3", "2")
    c = c.replace("4", "3")
    c = c.replace("5", "4")
    c = c.replace("6", "5")
    c = c.replace("7", "6")
    c = c.replace("8", "7")
    c = c.replace("9", "8")
    c = c.replace("a", "9")
    c = c.replace("b", "a")
    c = c.replace("c", "b")
    c = c.replace("d", "c")
    c = c.replace("e", "d")
    c = c.replace("f", "e")

    return c