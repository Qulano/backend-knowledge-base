import time
import threading
import multiprocessing
import asyncio

def countdown(start):
    s = start
    while s > 0:
        s -= 1
    print("Функция отработал")
# s = time.perf_counter()              


# tg_1 = threading.Thread(target=countdown, args=(50_000_000,))
# tg_2 = threading.Thread(target=countdown, args=(50_000_000,))
# s = time.perf_counter()
# test_tg = [tg_1 , tg_2]
# for obj in test_tg:
#     obj.start()
# for obj in test_tg:
#     obj.join()
# print(f"Функции отработали за {(time.perf_counter() - s):.9f} сек ")


# def query():
#     time.sleep(1)
# st = time.perf_counter()
# query()
# query()
# query()
# query()
# print(f"{(time.perf_counter() - st):.9f} сек")

# q_tg = threading.Thread(target=query)
# b_tg = threading.Thread(target=query)
# c_tg = threading.Thread(target=query)
# z_tg = threading.Thread(target=query)
# q_tgs = [q_tg, b_tg, c_tg, z_tg]   
# st = time.perf_counter()
# for obj in q_tgs:
#     obj.start()
# for obj in q_tgs:
#     obj.join()
# print(f"{(time.perf_counter() - st):.9f} сек")

# locker = threading.Lock()
# gob = 0
# def func_without_lock():
#     global gob
#     for i in range(1000):
#         loc = gob
#         time.sleep(0)
#         gob = loc + 1
    
# tg_1 = threading.Thread(target=func_without_lock)
# tg_2 = threading.Thread(target=func_without_lock)
# tags = [tg_1, tg_2]
# for obj in tags:
#     obj.start()
# for obj in tags:
#     obj.join()
# print(gob)

# gob = 0
# def func_with_lock():
#     with locker:
#         global gob
#         for i in range(1000):
#             loc = gob
#             time.sleep(0)
#             gob = loc + 1
# tg_1 = threading.Thread(target=func_with_lock)
# tg_2 = threading.Thread(target=func_with_lock)
# tags = [tg_1, tg_2]
# for obj in tags:
#     obj.start()
# for obj in tags:
#     obj.join()
# print(gob)

# if __name__ == "__main__":
#     p_1 = multiprocessing.Process(target=countdown, args=(50_000_000,))
#     p_2 = multiprocessing.Process(target=countdown, args=(50_000_000,))
#     ps = [p_1, p_2]
#     st = time.perf_counter()
#     for obj in ps:
#         obj.start()
#     for obj in ps:
#         obj.join()
    
#     print(f"Процессы отработали за {(time.perf_counter() - st):.9f} сек")

async def async_query():
    await asyncio.sleep(1)
async def main():
    start = time.perf_counter()
    await asyncio.gather(async_query(), async_query(), async_query(), async_query())
    print(f"Время выполнения {(time.perf_counter() - start):.3f} сек")
async def main_1():
    start = time.perf_counter()
    await async_query()
    await async_query()
    await async_query()
    await async_query()
    print(f"Время выполнения {(time.perf_counter() - start):.3f} сек")
if __name__ == "__main__":
    asyncio.run(main())

        
        
        