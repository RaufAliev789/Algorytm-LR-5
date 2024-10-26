from collections import deque #добавить и удалить с начала или конца
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: #возвр. в виде цел. ч. списка
        output = []
        q = deque()
        l = 0
        r = 0

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]: #тк изначально дек пуст надо написать q (иначе пр. упадет)
                q.pop()
            q.append(r)

            # Удаляем левый элемент, если он выходит за пределы текущего окна
            if q and q[0] < l:
                q.popleft()

            # Если мы заполнили первое окно, добавляем максимум в выходной список
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1  # Сдвигаем левый указатель вправо

            r += 1  # Сдвигаем правый указатель вправо

        return output

# Ввод данных
n = int(input("Введите количество элементов: "))  # Ввод количества элементов
nums = list(map(int, input("Введите элементы через пробел: ").split()))  # Ввод элементов
k = int(input("Введите размер окна: "))  # Ввод размера окна

# Создаем объект класса Solution и вызываем метод
solution = Solution()
result = solution.maxSlidingWindow(nums, k)

# Вывод результата
print("Выход:", ' '.join(map(str, result)))