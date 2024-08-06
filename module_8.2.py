def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    count = 0
    for i in numbers:
        try:
            result += i
            count += 1
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data, count


def calculate_average(numbers):
    try:
        res = personal_sum(numbers)
        return res[0] / res[2]
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')