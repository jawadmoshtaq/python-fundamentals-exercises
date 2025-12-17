from tasks import (
    greet_user,
    add_numbers,
    adult_or_minor,
    count_vowels,
    min_max_avg,
    top_student,
    add_or_update_score,
    class_average,
)

if __name__ == "__main__":
    print("OK - Python is running")

    greet_user("Jawad")
    print("10 + 7 =", add_numbers(10, 7))
    print("Age 17 =", adult_or_minor(17))
    print("Vowels in 'Hello World' =", count_vowels("Hello World"))
    print("Min/Max/Avg =", min_max_avg([1, 2, 3, 10]))

    scores = {}
    add_or_update_score(scores, "Ali", 18.5)
    add_or_update_score(scores, "Sara", 27.0)
    add_or_update_score(scores, "Omid", 24.0)
    print("Average score =", class_average(scores))
    print("Top student =", top_student(scores))
