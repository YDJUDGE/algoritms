class ValidBrackets:
    def __init__(self, s: str):
        self.s = s

    def valid_brackets(self):
        open_br = "[{("
        arr = []

        for i in self.s:
            if i in open_br:
                arr.append(i)
            else:
                if len(arr) == 0:
                    print(False)
                    return False
                if arr[-1] == "{" and i == "}" or arr[-1] == "[" and i == "]" or arr[-1] == "(" and i == ")":
                    arr.pop()
                else:
                    print(False)
                    return False
        if len(arr) == 0:
            print(True)
            return True
        else:
            print(False)
            return False

