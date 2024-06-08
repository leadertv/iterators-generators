import types


def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            print(f"Обработка вложенного списка: {item}")
            yield from flat_generator(item)
        else:
            print(f"Возвращаем элемент: {item}")
            yield item


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print("Начало теста 4")
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(f"Сравнение: {flat_iterator_item} == {check_item}")
        assert flat_iterator_item == check_item

    result = list(flat_generator(list_of_lists_2))
    print(f"Результат преобразования в список: {result}")
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print("Тест 4 пройден")

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
