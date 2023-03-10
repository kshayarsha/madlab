import random


class Password:
    def makepass(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        s3=''
        y = 4
        sym = 4
        n =4
        s1 = ''
        for g in range(0, y + 1):
            l = random.choice(letters)
            s1 = s1 + l
        for t in range(0, sym + 1):
            r = random.choice(symbols)
            s1 = s1 + r
        for o in range(0, n + 1):
            r = random.choice(numbers)
            s1 = s1 + r
        s2 = list(s1)
        for p in range(0, 9):
            a = random.randint(0, len(s1) - 1)
            b = random.randint(0, len(s1) - 1)
            s2[a], s2[b] = s2[b], s2[a]
        for x in s2:
            s3=s3+x
        return s3
