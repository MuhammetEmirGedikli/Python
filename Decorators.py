def extra(func):
    def wrapper(numbers):
        even_sum = 0
        even_count = 0
        odd_sum = 0
        odd_count = 0

        for number in numbers:
            if number % 2 == 0:
                even_sum += number
                even_count += 1
            else:
                odd_sum += number
                odd_count += 1

        print("Average of odd numbers:", odd_sum / odd_count)
        print("Average of even numbers:", even_sum / even_count)

        func(numbers)
    return wrapper

@extra
def find_average(numbers):
    total = 0

    for i in numbers:
        total += i

    print("Overall average:", total / len(numbers))

print(find_average([1, 2, 3, 4, 5, 13, 4, 531]))
