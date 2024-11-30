
def valid_brackets(s: str) -> bool:
    open_br = "[{("
    arr = []

    for i in s:
        if i in open_br:
            arr.append(i)
        else:
            if len(arr) == 0:
                return False
            if arr[-1] == "{" and i == "}" or arr[-1] == "[" and i == "]" or arr[-1] == "(" and i == ")":
                arr.pop()
            else:
                return False
    if len(arr) == 0:
        return True
    else:
        return False


print(valid_brackets("[{()}]"))
print(valid_brackets("[{"))
print(valid_brackets("([})"))
