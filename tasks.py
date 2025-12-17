def greet_user(name):
    print(f"Hello, {name}!")


def add_numbers(a, b):
    return a + b


def print_1_to_n(n):
    i = 1
    while i <= n:
        print(i)
        i += 1


def print_even_1_to_50():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)


def adult_or_minor(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


def sum_greater_than_10(nums):
    total = 0
    for x in nums:
        if x > 10:
            total += x
    return total


def squares_1_to_n(n):
    return [i * i for i in range(1, n + 1)]


def print_star_square(n):
    for _ in range(n):
        line = ""
        for _ in range(n):
            line += "*"
        print(line)


def build_3x3_matrix(value):
    matrix = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(value)
        matrix.append(row)
    return matrix


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def words_to_length_dict(words):
    d = {}
    for w in words:
        d[w] = len(w)
    return d


def filter_values_gt_50(d):
    out = {}
    for k, v in d.items():
        if v > 50:
            out[k] = v
    return out


def max_without_max(nums):
    if not nums:
        raise ValueError("List is empty")

    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m


def sum_until_zero():
    total = 0
    while True:
        user_input = input("Enter a number (0 to stop): ")
        try:
            n = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if n == 0:
            break
        total += n
    return total


def min_max_avg(nums):
    if not nums:
        raise ValueError("List is empty")

    mn = nums[0]
    mx = nums[0]
    total = 0.0

    for x in nums:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
        total += x

    avg = total / len(nums)
    return mn, mx, avg


def print_values_from_list_of_lists(data):
    for row in data:
        for item in row:
            print(item)


def only_odds(nums):
    out = []
    for x in nums:
        if x % 2 != 0:
            out.append(x)
    return out


def print_star_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)


def print_key_value(d):
    for k, v in d.items():
        print(f"{k} -> {v}")


def add_or_update_score(scores, student, score):
    scores[student] = score


def class_average(scores):
    if not scores:
        return 0.0
    total = 0.0
    for v in scores.values():
        total += v
    return total / len(scores)


def top_student(scores):
    if not scores:
        return None

    best_name = None
    best_score = None

    for name, sc in scores.items():
        if best_score is None or sc > best_score:
            best_score = sc
            best_name = name

    return best_name, best_score
