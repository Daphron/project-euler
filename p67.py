def p67():
    file = open("triangle.txt")
    sTriangle = ""
    for line in file.readlines():
        sTriangle += " " + line.strip()

    triangle = sTriangle.split()

    #print triangle

    maxRow = [0 for i in range(101)]
    for i in range(100):
        for j in range(100-i):
            #print str(i) + "  " + str(j)
            value = int(triangle.pop())
            maxRow[j] = max(maxRow[j], maxRow[j+1]) + value

    print maxRow[0]


if __name__ == "__main__":
    p67()
