import sys

b = ["печенье", "молоко", "магический посох"]
iterator = iter(b)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("Элементов больше нет")
        break

    
    
class PullTimer:
    def __init__(self, second):
        self.count = second
    def __iter__(self):
        return self
    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        else:
            count = self.count
            self.count -= 1
            return count
timer = PullTimer(4)
for i in timer:
    print(i)
else:
    print("Проход закончен")

for i in timer:
    print(i)
    
    
def pull_timer(second):
    while second != 0:
        print((f"Проснулся, сейчас отдам {second}"))
        yield second
        second -= 1
    
gen = pull_timer(4)

print(next(gen))
print(next(gen))

gin = pull_timer(4)
for i in gin:
    print(i)

list_nums = [x for x in range(1_000_000)]

gen_nums = (x for x in range(100_000_000))

print(sys.getsizeof(list_nums) / (1024 * 1024))

print(sys.getsizeof(gen_nums) / (1024 * 1024))

print(next(gen_nums))
print(next(gen_nums))
# print(len(gen_nums))

dict_num = {x: k for x, k in zip(range(1, 7), range(10, 70 , 10)) if x % 2 == 0}

set_num = {x for x in range(10)}
print(dict_num)
print(set_num)

def log_stream(log_1, log_2):
    yield from log_1
    yield from log_2
    
def extract_errors(stream):
    for line in stream:
        clean_line = line.strip(" ")
        if clean_line.startswith("ERROR"):
            yield clean_line

log_1 = ["INFO: user ok", " ERROR: db timeout "]
log_2 = [" ", "ERROR: auth failed"]
stream = log_stream(log_1, log_2)
pipeline = extract_errors(stream)
for line in pipeline:
    print(line)
    
nested = [1, [2, [3, 4]], 5]
def flatten(item):
    for elm in item:
        if isinstance(elm, list):
            yield from flatten(elm)
        else:
            yield elm
num = flatten(nested)   
print([i for i in num])


def spit(lst):
    yield from lst

def remove(spit):
    for elm in spit:
        if elm % 2 != 0:
            yield elm

nums = [2, 4, 5, 8]
sp = spit(nums)
numbers = remove(sp)
print(list(numbers))