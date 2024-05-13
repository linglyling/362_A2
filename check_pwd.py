def check_pwd(pwd):
    if len(pwd) <= 7:
        return False
    if len(pwd) >= 21:
        return False
    return True
