def upper_str(string):
    """ Функция возвращает строку заглавными буквами """
    upper_string = string.upper()
    return upper_string


def up_first_letter(string):
    """ Функция делает заглавными первые буквы каждого слова в строке """
    str_list = string.split(" ")
    upper_letters_str = []
    for word in str_list:
        up_letter_word = word.capitalize()
        upper_letters_str.append(up_letter_word)
    return ' '.join(upper_letters_str)
