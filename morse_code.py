morse_code = {

    'А': '·−',     'Б': '−···',    'В': '·−−',     'Г': '−−·',

    'Д': '−··',    'Е': '·',       'Ж': '···−',    " ":  '/',

    'З': '−−··',   'И': '··',      'Й': '·−−−',    'К': '−·−',

    'Л': '·−··',   'М': '−−',      'Н': '−·',      'О': '−−−',

    'П': '·−−·',   'Р': '·−·',     'С': '···',     'Т': '−',

    'У': '··−',    'Ф': '··−·',    'Х': '····',    'Ц': '−·−·',

    'Ч': '−−−·',   'Ш': '−−−−',    'Щ': '−−·−',    'Ъ': '−··−',

    'Ы': '−·−−',   'Ь': '−··−',    'Э': '··−··',   'Ю': '··−−',

    'Я': '·−·−',

    '0': '−−−−−',  '1': '·−−−−',   '2': '··−−−',   '3': '···−−',

    '4': '····−',  '5': '·····',   '6': '−····',   '7': '−−···',

    '8': '−−−··',  '9': '−−−−·',

    '.': '······', ',': '·−·−·−',  '?': '··−−··',  '!': '−−··−−',

    '/': '−··−·',  '(': '−·−−·',   ')': '−·−−·−',  ':': '−−−···',

    ';': '−·−·−',  '=': '−···−',   '+': '·−·−·',   '-': '−····−',

    '"': '·−··−·', "'": '·−−−−·',  '@': '·−−·−·',

}

reverse_morse = {v: k for k, v in morse_code.items()}

 

def user_write_morse_txt_file(user_text,add_or_new_f = 'w' or 'a'):

    with open('user.txt',add_or_new_f , encoding='UTF-8') as f:

        result = ''

        for letter in user_text:

            temp_l = morse_code.get(letter, '?')

            result += temp_l

            result += '|'

        f.write(result+'\n')

 

def read_morse_txt_file(path_and_name_file, num_str):

    with open(path_and_name_file,'r', encoding='UTF-8') as f:

        for _ in range(num_str - 1):

            next(f)

        letter = f.readline()

        letter = list(letter.split('|'))

        result = ''

    for x in letter:

        if x != '' and x != '\n':

            temp = reverse_morse.get(x)

            result += str(temp)

    return print(result)

 

def check_string():

    while True:

        user_text = input('Введите текст для шифра:').upper().strip()

        if not user_text:

            print('Введено пустое значение, повторите ввод')

            continue

        try:

            invalid = [char for char in user_text if char not in morse_code]

            if invalid:

                raise ValueError(f'Символы {' '.join(invalid)} не поддерживается')

           

            return user_text

        except ValueError as e:

            print(f"Ошибка: {e}. Введите текст на русском языке.")

        except Exception as e:

            print(f"Произошла неизвестная ошибка: {e}")

 

def check_num(counter):

    while True:

        num_str = input('Введите какую строчку хотите расшифровать:')

        if not num_str:

            print('Введено пустое значение, повторите ввод')

            continue

        try:

            num_str = int(num_str)

            if num_str < 1 or num_str>counter:

                raise ValueError(f'Введите правильный номер строки в диапозоне от 1 до {counter}')

            return num_str

        except ValueError as e:

            if 'invalid literal' in str(e):

                print('Ошибка: Введите целое число!')

            else:

                print(f'Ошибка: {e}')

        except Exception as e:

            print(f"Произошла неизвестная ошибка: {e}")

 

def check_status(status_user):

    status_user.upper().strip()

    if status_user == 'ДА':

        return True

    else:

        return False

 

counter = 0

x = True

while x:

    if x:

        if counter == 0:

            user_text_morse = check_string()

            user_write_morse_txt_file(user_text_morse,'w')

            print('Создан файл user.txt и ответ зашифрован')

            counter +=1

        else:

            user_text_morse = check_string()

            user_write_morse_txt_file(user_text_morse,'a')

            counter +=1

        x = check_status(input('Введите ДА для продолжение, или любое другое значение для выхода:').upper().strip())

    else:

        break

 

print(f'Введено {counter} строчек')

 

num_string_user = check_num(counter)

read_morse_txt_file('user.txt',num_string_user)

print('Мы закончили работу :)')

