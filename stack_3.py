from LinkedStack import LinkedStack

class sentenceChecker:
    def __init__(self):
        self.__stack = LinkedStack()

    def is_included(self, s):
        idx = s.find('$')

        for i in range(idx):
            self.__stack.push(s[i])

        for i in range(idx+1, len(s)):
            prev = self.__stack.pop()
            curr = s[i]

            if prev != curr:
                return False

        return True

if __name__ == "__main__":
    s = 'abc$abc'
    checker = sentenceChecker()
    rv = checker.is_included(s)
    if rv == True:
        print("include")
    else:
        print("Nor included")