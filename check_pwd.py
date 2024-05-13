def check_pwd(pwd):
    if len(pwd) <= 7:
        return False
    if len(pwd) >= 21:
        return False
    if not any(c.islower() for c in pwd):
        return False
    if not any(c.isupper() for c in pwd):
        return False
    return True
