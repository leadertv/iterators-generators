import types


def flat_generator(list_of_lists):
    for i, sublist in enumerate(list_of_lists):
        print(f"Обработка списка {i}: {sublist}")
        for j, item in enumerate(sublist):
            print(f"Возвращаем элемент: {item} (список {i}, индекс {j})")
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print("Начало теста 2")
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(f"Сравнение: {flat_iterator_item} == {check_item}")
        assert flat_iterator_item == check_item

    result = list(flat_generator(list_of_lists_1))
    print(f"Результат преобразования в список: {result}")
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print("Тест 2 пройден")


if __name__ == '__main__':
    test_2()
