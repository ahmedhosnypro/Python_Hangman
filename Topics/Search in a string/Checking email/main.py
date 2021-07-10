def check_email(string):
    if string.find(' ') == -1:
        if string.find("@") != -1:
            if string.find("@.") == -1:
                if string.find(".", string.find("@") + 1) != -1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

