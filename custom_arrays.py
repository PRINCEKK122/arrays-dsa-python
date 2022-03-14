from typing import List, Set


class Array:
    def __init__(self):
        self.__count = 0
        self.__items: List[int] = []

    def size(self) -> int:
        return self.__count

    def remove_at(self, index: int) -> int:
        if index < 0 or index >= self.__count:
            raise IndexError("Please provide a valid index!")

        for i in range(0, self.__count):
            if i == index:
                self.__count -= 1
                return self.__items[i]

    def intersect(self, another_array: List[int]) -> List[int]:
        common_elements: Set = set()
        self.__items.sort()
        another_array.sort()

        for i in range(0, self.__count):
            for j in range(0, len(another_array)):
                if self.__items[i] < another_array[j]:
                    break

                if self.__items[i] == another_array[j]:
                    common_elements.add(self.__items[i])

        return list(common_elements)

    def insert(self, item: int) -> None:
        self.__count += 1
        self.__items.append(item)

    def reverse(self) -> List[int]:
        for i in range(0, self.__count // 2):
            temp = self.__items[i]
            self.__items[i] = self.__items[self.__count - 1 - i]
            self.__items[self.__count - 1 - i] = temp

        return self.__items

    def index_of(self, value: int):
        for i in range(0, self.__count):
            if self.__items[i] == value:
                return i

        return -1

    def max(self) -> int:
        largest_number = self.__items[0]

        for index in range(1, len(self.__items)):
            if self.__items[index] >= largest_number:
                largest_number = self.__items[index]

        return largest_number

    def insert_at(self, item: int, index: int) -> None:
        if index < 0 or index >= self.__count:
            raise IndexError("Please provide a valid index!")

        self.__items.append(0)
        self.__count += 1

        for i in range(self.__count - 2, index - 1, -1):
            self.__items[i + 1] = self.__items[i]

        self.__items[index] = item

    def print(self) -> None:
        for i in range(0, self.__count):
            print(self.__items[i])
