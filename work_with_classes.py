# exercise 1
# class Triangle(object):
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#     number_of_sides = 3
#     def check_angle(self):
#         if self.angle1 + self.angle2 + self.angle3 == 180:
#             return True
#         else:
#             return False
#
# my_triangle = Triangle(30, 90, 60)
# print(my_triangle.number_of_sides)
# print(my_triangle.check_angle())
#
#
# exercise 2
# class Song(object):
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#          for row in self.lyrics:
#              print(row)
#
# happy_bday = Song(["May god bless you", "Have a sunshine on you", "Happy Birthday to you!"])
# print(happy_bday.sing_me_a_song())
#
#
#exercise 3
# class Lunch(object):
#     def __init__(self, menu):
#         self.menu = menu
#     def menu_price(self):
#         if self.menu == "menu1":
#             print("Your choice:", self.menu, "Price 12.00")
#         elif self.menu == "menu2":
#             print("Your choice:", self.menu, "Price 13.40")
#         else:
#             print("Error in menu")
#
# Paul = Lunch("menu1")
# print(Paul.menu_price())

# exercise 4
# class Point3D(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __repr__(self):
#         return "(%d, %d, %d)"%(self.x, self.y, self.z)
#
# my_point = Point3D(1, 2, 3)
# print(my_point)


class Cat:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, num):
        self._age = num

cat1 = Cat()
cat1.age = 7
cat1._age = 6
print(cat1.age)