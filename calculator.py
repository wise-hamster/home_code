def plus(num_1, num_2):
    return num_1 + num_2


def minus(num_1, num_2):
    return num_1 - num_2


def multiplication(num_1, num_2):
    return num_1 * num_2


def division(num_1, num_2):
    return num_1 / num_2


def calculator(num_1, num_2, sign):
    try:
        if sign == '+':
            return plus(num_1, num_2)
        elif sign == '-':
            return minus(num_1, num_2)
        elif sign == '*':
            return multiplication(num_1, num_2)
        elif sign == '/':
            return division(num_1, num_2)
    except ZeroDivisionError:
        return ('You cant divide by zero.')


def check_num():
    x = True
    while x:
        num_user = input('Enter a number: ').strip()

        if num_user.isdigit():
            x = False
            num_user = int(num_user)
        elif '.' in num_user:
            if num_user[0] == '.' or num_user[-1] == '.':
                x = True
                print('Incorrect number entered')
            else:
                num_user = float(num_user)
                x = False
        else:
            print('Incorrect number entered')
    return num_user


def check_character():
    x = True
    while x:
        character_user = input('Enter a character +,-,*,/: ').strip()
        if character_user in '+-/*':
            x = False
            return character_user
        else:
            print('Incorrect character entered')

def start_calculator():
    print('To operate the calculator, follow the commands')
    x = True
    while x:
        num_1_input = check_num()
        sign_input = check_character()
        num_2_input = check_num()
        print(calculator(num_1_input, num_2_input, sign_input))
        y = True
        while y:
            ex_or_co = input('To continue or exit, enter Y/N: ').strip().lower()
            if ex_or_co == 'y':
                y = False
            elif ex_or_co == 'n':
                y = False
                x = False
            else:
                print('Unknown command, please repeat the input')

if __name__ == "__main__":
    print("Запуск калькулятора в режиме выполнения")
    start_calculator()
