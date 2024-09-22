def calculate(sides):
    return sides[0] * sides[1]

lengths = [(3, 4), (10, 3), (5, 6), (1, 9)]
print(list(map(calculate, lengths)))

def check(triangle):
    triangles = []
    if (triangle[0] + triangle[1] > triangle[2] and
        triangle[0] + triangle[2] > triangle[1] and
        triangle[1] + triangle[2] > triangle[0]):
        
        triangles.append(triangle[0])
        triangles.append(triangle[1])
        triangles.append(triangle[2])
        return True
    else:
        return False

triangles_list = [(3, 4, 5), (6, 8, 10), (3, 10, 7), (7, 24, 25), (6, 10, 1000)]
print(list(filter(check, triangles_list)))

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(even_numbers)
print(reduce(lambda x, y: x + y, even_numbers))

names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

for name, surname in zip(names, surnames):
    print(name, surname)
