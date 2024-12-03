class ValidBrackets:
    def __init__(self, s: str):
        self.s = s

    def valid_brackets(self):
        """
        Проверяется валидность скобок, на вход принимается строка
        s - строка со скобками
        :return:
        """
        open_br = "[{("
        arr = []

        for i in self.s:
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

