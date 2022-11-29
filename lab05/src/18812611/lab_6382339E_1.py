FILE = "lab05/src/test.txt"
def answer():
    fileh = open(FILE, "r")
    content = fileh.read()  
    fileh.close()
    return content

def answer2(num_char):
    fileh = open(FILE, "r")
    content = fileh.read(num_char)
    fileh.close()
    return content

def answer3():
    fileh = open(FILE, "r")
    content = fileh.read()  
    fileh.close()
    return content
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

    return content

def main():
    print(answer())
    num = 20
    print(answer2(num))
    print(answer3())

if __name__ == "__main__":
    main()
