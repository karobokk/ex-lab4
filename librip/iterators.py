# Итератор для удаления дубликатов
from setuptools.package_index import unique_everseen

class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if kwargs.get('ignore_case', False):
            self._items = list(unique_everseen(items, str.lower))
        else:
            self._items = list(unique_everseen(items))
        self._counter = -1

    def __next__(self):
        # Нужно реализовать __next__
        if self._counter + 1 >= len(self._items):
            raise StopIteration()
        self._counter += 1
        return self._items[self._counter]

    def __iter__(self):
        return self
