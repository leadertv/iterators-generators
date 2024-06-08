class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list_index = 0
        self.current_item_index = 0
        print(f"Инициализация: текущий список {self.current_list_index}, текущий элемент {self.current_item_index}")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_index >= len(self.list_of_list):
            print("Все списки пройдены, итерация завершена.")
            raise StopIteration
        if self.current_item_index >= len(self.list_of_list[self.current_list_index]):
            print(f"Список {self.current_list_index} пройден, переходим к следующему списку.")
            self.current_list_index += 1
            self.current_item_index = 0
            return self.__next__()
        item = self.list_of_list[self.current_list_index][self.current_item_index]
        print(f"Возвращаем элемент: {item} (список {self.current_list_index}, индекс {self.current_item_index})")
        self.current_item_index += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print("Начало теста 1")
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(f"Сравнение: {flat_iterator_item} == {check_item}")
        assert flat_iterator_item == check_item

    result = list(FlatIterator(list_of_lists_1))
    print(f"Результат преобразования в список: {result}")
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("Тест 1 пройден")


if __name__ == '__main__':
    test_1()
