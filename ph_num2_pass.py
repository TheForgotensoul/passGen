import re
from itertools import chain
from colored import fg, attr


def ph_num(number, cap, len_pass):
    ph = str(number)
    dic_num = {
        '0': ' ',
        '00': "20's",
        '000': "30's",
        '1': ".",
        '11': "2.'s",
        '111': "3.'s",
        '2': 'a',
        '22': 'b',
        '222': 'c',
        '3': 'd',
        '33': 'e',
        '333': 'f',
        '4': 'g',
        '44': 'h',
        '444': 'i',
        '5': 'j',
        '55': "k",
        '555': 'l',
        '6': 'm',
        '66': 'n',
        '666': 'o',
        '7': 'p',
        '77': 'q',
        '777': 'r',
        '7777': 's',
        '8': 't',
        '88': 'u',
        '888': 'v',
        '9': 'w',
        '99': 'x',
        '999': 'y',
        '9999': 'z'
    }
    if re.match(r"^[6-9]\d{9}$", ph):
        lst = list(map(int, ph))
        lst.append(None)
        mod = []
        x = []
        for i in range(10):
            if lst[i] == lst[i + 1]:
                mod.append(str(lst[i]) * 2)
                if lst[i + 1] == lst[i + 2]:
                    mod.append(str(lst[i + 1]) * 3)
                    mod = list(dict.fromkeys(mod))
            elif lst[i] != lst[i - 1]:
                mod.append(str(lst[i]))
        if int(len_pass) > 9:
            mod.append(mod[0:(int(len_pass) - 10)])
            mod = list(chain(*mod))
            print(mod)
            for i in mod:
                v = str(dic_num.get(i))
                x.append(v)
            x = ''.join(str(e) for e in x)
            print(f"{fg(27)}{attr(1)}Your {str(len_pass)} length password is: {attr(0)}", end="")
            if cap.lower() == "yes" or cap.lower() == "y":
                print(f'{fg(82)}{attr(1)}{x.capitalize()}{attr(0)}')
            else:
                print(f'{fg(82)}{attr(1)}{x.lower()}{attr(0)}')
        else:
            for i in mod:
                v = str(dic_num.get(i))
                x.append(v)
            x = ''.join(str(e) for e in x)
            print(f"{fg(27)}{attr(1)}Your password is: {attr(0)}", end="")
            if cap.lower() == "yes" or cap.lower() == "y":
                print(f'{fg(82)}{attr(1)}{x.capitalize()}{attr(0)}')
            else:
                print(f'{fg(82)}{attr(1)}{x.lower()}{attr(0)}')

    else:
        print(f"{fg(196)}{attr(1)}OOPS...numbers has more than 10 digits...{attr(0)}")


try:
    print(f'{fg(226)}{attr(1)}Warning: Every Field must be answered!!!{attr(0)}')
    ph_num(int(input(f"{fg(27)}{attr(1)}Phone number: {attr(0)}")),
           str(input(f"{fg(27)}{attr(1)}Captalize first letter yes(y) or no(n): {attr(0)}")),
           len_pass=input(f"{fg(27)}{attr(1)}Enter the length of password(default: >= 8): {attr(0)}"))

except ValueError:
    print(f"{fg(196)}{attr(1)}accepts only 10 digits phone number without special characters...{attr(0)}")
