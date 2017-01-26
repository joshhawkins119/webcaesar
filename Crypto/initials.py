
def get_initials(fullname):          
    """ Given a person's name, return the person's initials (uppercase) """
    initials = ""
    for i in fullname.upper().split():
        initials += i[0]
    return initials

def main():
    userinput = input("What's your full name?")
    answer = get_initials(userinput)
    print("The initials of", userinput, "are", answer)

if __name__ == '__main__':
    main()
