class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = []
        self._flatten(list_of_list)

    def _flatten(self, iterable):
        for item in iterable:
            if isinstance(item, list):
                self._flatten(item)
            else:
                self.stack.append(item)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.stack):
            raise StopIteration
        item = self.stack[self.current_index]
        self.current_index += 1
        return item

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print("Начало теста 3")
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(f"Сравнение: {flat_iterator_item} == {check_item}")
        assert flat_iterator_item == check_item

    result = list(FlatIterator(list_of_lists_2))
    print(f"Результат преобразования в список: {result}")
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print("Тест 3 пройден")


if __name__ == '__main__':
    test_3()
