import time
from collections import deque

# lts = [x for x in range(50000)]
# start = time.perf_counter()
# for element in range(50_000):
#     if element in lts:
#         True
# print(f"Поиск по списку отработал за {(time.perf_counter() - start):.7f}")

s = {x for x in range(50_000)}
st = time.perf_counter()
for element in range(50_000):
    if element in s:
        True
print(f"Поиск по множеству отработал за {(time.perf_counter() - st):.7f}")

lst = [x for x in range(100_000)]
deq = deque(x for x in range(100_000))
start = time.perf_counter()
while lst:
    lst.pop(0)
print(f"Элементы были удалены за {(time.perf_counter() - start):.7f} сек")
start = time.perf_counter()
while deq:
    deq.popleft()
print(f"Элементы были удалены за {(time.perf_counter() - start):.7f} сек")


def two_sum(lst, target):
    seen = {}
    for index, val in enumerate(lst, start=0):
        need = target - val
        if need in seen:
            return f"Индекс первого {seen[need]}, индекс второго {index}"
        seen[val] = index 
    else:
        return "Желаемая пара не нешлась"
print(two_sum([1, 2, 7, 19], 9))
       

ls = [x for x in range(0, 1_000_000, 2)]
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    step_count = 0 
    while left <= right:
        step_count += 1
        average = (left + right) // 2
        if lst[average] == target:
            return f"Число под индексом {average}, потратили {step_count} шагов"
        elif target > lst[average]:
            left = average + 1
        else:
            right = average - 1
    return f"Элемент не найден, потратили шагов {step_count}"
print(binary_search(ls, 24))