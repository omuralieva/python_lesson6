array = [6, 'string', [40, 50], 1.2, 1, 1, 1, 1, 1, 1]
numbers_list = [3.4, 5.1, 2.2, 4.1, 1.0, 3.8]
numbers = [[1, 2], [2, 1], [4, 3], [5, 2], [3, 3]]
systems = ['Windows', 'macOS', 'Linux']



if __name__ == '__main__':
    array.append('Hello')                                     # добавляет элемент в конец списка
    print(array)
    array.extend(['World', ['Hello', 30], 'Piece', 2, 5])     # добалвяет список в конец списка
    print(array)
    array.insert(0, 'mom')                                    # добавляет элемент по заданным индексом
    print(array)
    array.remove([40, 50])                                    # удаляет заданный элемент
    print(array)
    array.pop(3)                                              # удаляет элемент под заданным индексом
    print(array)

    print(array.index('string'))                              # показывает индекс заданного элемента
    print(array.count(1))                                     # подсчитывает колличество заданных элементов
    numbers_list.sort()                                       # сортирует спикок по возрастанию
    print(numbers_list)
    numbers_list.sort(reverse=True)                           # сортирует список по убыванию
    print(numbers_list)
    numbers.sort()                                            # вариант сортировки списка в списке
    print(numbers)
    systems.reverse()                                         # меняет местами элементы списка (в обратном порядке)
    print(systems)
for о in reversed(systems):                                   # дает доступ к отдельным элементам(в обратном порядке)
    print(о)
    systems.copy()                                            # поверхностная копия списка
    print(systems)
    systems.clear()
    print(systems)                                            # очищает список

