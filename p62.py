
def isPermutation(s, o):
    """ Returns true if s is a permutation of o """
    # print("isPermutation")
    # print(s)
    # print(o)
    if len(s) != len(o):
        # print("len")
        return False
    for i, elem in enumerate(sorted(list(s))):
        # print("i " + str(i) + " elem " + str(elem))
        if elem != sorted(o)[i]:
            return False

    return True

def main():    

    contestants = {}
    s = 1
    found = False

    while found == False:
        num = str(s**3)
        exists = False
        # print(s)
        # print(contestants)
        for key in contestants:
            if isPermutation(num, key):
                exists = True
                contestants[key] += 1
                if contestants[key] >= 5:
                    #not ONLY 5?
                    found = True
                    print("This is it!")
                    print(key)

        if not exists:
            contestants[num] = 1

        s += 1

        # if s > 405:
        #     found = True
        #     print("false alarm")

    print("End")

if __name__ == "__main__":
    main()
    # print(isPermutation(str(41063625), str(56623104)))
    

