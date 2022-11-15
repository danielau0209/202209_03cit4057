def answer():
    ret = ""
    STACK = "Hello world" 
    def answer (needle):
     found = False 

    # START: You code here
    stack_lower = stack_lower()
    needle = needle. lower() 
    for lettle in stack_lower:
        if lettle == needle:
            found = True
            break

    # END: You code here
    return found 

# Please don't change the code below!!!
def main():
    letter = input("Please enter a letter")
    if answer (letter):
     print("Found." )
    else:
     print ("not found.")


if __name__ == "__main__":
    main()
# Please don't change the code above!!!