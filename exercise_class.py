# ex 1

# class Sofa(object):
#     def __init__(self, ingredient):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = False
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f"Газировка + {self.ingredient}")
#         else:
#             print("Обычная газировка")
#
#
# drink1 = Sofa("лайм")
# drink2 = Sofa(1)
# drink1.show_my_drink()
# drink2.show_my_drink()

# ex 2

class TriangleChecker(object):
    def __init__(self, sides):
        self.sides = sides


    def is_triangle(self):
        if isinstance(self.sides[0], (int, float)) and isinstance(self.sides[1], (int, float)) and isinstance(self.sides[2], (int, float)):
            if self.sides[0] > 0 and self.sides[1] > 0 and self.sides[2] > 0:
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return "Ура, можно построить треугольник!"
                return "Жаль, что из этого ничего не получится"
            return "С отрицательными числами ничего не выйдет!"
        return "Нужно вводить только числа!"


triangle1 = TriangleChecker([3, 7, 5])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([3, 9, 5])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([-3, 9, 5])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([3, "ua", 5])
print(triangle4.is_triangle())

# ex 4

# class Nikola(object):
#     def __init__(self, name, age):
#         self.name = name
#         if self.name != "Nikola":
#             self.name = f"I'm not {self.name}, I'm Nikola"
#         self.age = age
#
#
# person1 = Nikola("Nikola", 25)
# person2 = Nikola("Vasya", 35)
# print(person1.name)
# print(person2.name)
