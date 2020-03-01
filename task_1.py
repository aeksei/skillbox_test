import string


def Split(split_str, sep=string.whitespace):
    print('aeksei94@gmail.com')

    # Проверка корректности ввода
    if sep != string.whitespace:
        if not isinstance(sep, str):
            raise TypeError("Недопустимый тип разделителя. Разделитель должен быть строкой")
        if len(sep) != 1:
            raise ValueError("Недопустимое значение разделителя. Длина должна быть один символ")

    if not split_str:
        return ['']

    split_result = ['']
    split = False
    for char in split_str:
        if char in sep:
            split = True
        else:
            # Если было разбиение на прошлом шаге, то добавляем новый элемент в список
            # иначе приписываем символ к последнему элементу
            if split:
                split_result.append(char)
                split = False
            else:
                split_result[-1] += char

    if sep == split_str[-1]:
        split_result.append('')

    return split_result


def compare_with_string_split_method(s, sep=string.whitespace):
    my_split = Split(s, sep)
    in_build_split = s.split(sep)
    if my_split != in_build_split:
        raise ValueError("{} != {}".format(my_split, in_build_split))


if __name__ == '__main__':
    compare_with_string_split_method("")
    compare_with_string_split_method("", "1")
    compare_with_string_split_method("1234", "1")
    compare_with_string_split_method("123", "2")
    compare_with_string_split_method("123", "3")
