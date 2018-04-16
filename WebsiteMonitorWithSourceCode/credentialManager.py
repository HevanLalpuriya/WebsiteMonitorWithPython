""" code for managing credentials """

adminuser = "abc"
adminpassword = "abc"

def simplecheckcredential():
    print "welocome to web monitoring tool"
    print "-------------------------------\n"

    username = raw_input(("Enter UserName: "))
    if username == adminuser:
        if raw_input(("Enter Password: ")) == adminpassword:
            print "Access granted"
            return True
        else:
            print "incorrect password."
            return False
    else:
        print "invalid user"
        return False
