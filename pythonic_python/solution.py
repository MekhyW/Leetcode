def print_indices_and_elements(elements) -> None:
    for i, name in enumerate(elements):
        print(f"{i} {name}")


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [num for num in range(start, end+1, 2)]


def get_char_set_from(s: str) -> set[str]:
    return {c for c in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    import math
    return {num: int(math.sqrt(num)) for num in range(start, end+1) if math.sqrt(num).is_integer()}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [num if num % 10 == 0 else -1 for num in numbers if num % 5 == 0]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(mystr) for mystr in strings]


def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return "My name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don't smoke, but I occasionally drink. I'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone."


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
    def __iter__(self):
        return self
    def __next__(self):
        try:
            x = self.elements[0]
            self.elements = self.elements[2:]
            return x
        except IndexError:
            raise StopIteration


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    vals = [e1, e2] + list(others)
    return sum(vals) / len(vals)


def keys_with_different_value() -> list[int]:
    return [5, 6, 7, 8, 9]


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        first, last = numbers[0], numbers[-1]
        numbers = numbers[1:-1]
        print(f'{first} {last}')
    if numbers:
        print(numbers[0])


def append_range(start: int, end: int, step: int=1, to=None) -> list[int]:
    if not to:
        to = []
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None
