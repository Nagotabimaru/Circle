# 1
# class Circle:
#     def __init__(self, radius: int):
#         self.radius = radius
#
#     def circ_len(self):  # длина окружности
#         return self.radius * 3.14 * 2
#
#     def __eq__(self, other):  # ==
#         return self.radius == other.radius
#
#     def __lt__(self, other):  # <
#         return self.circ_len() < other.circ_len()
#
#     def __le__(self, other):  # <=
#         pass
#
#     def __gt__(self, other):  # >
#         pass
#
#     def __ge__(self, other):  # >=
#         pass
#
#     def __add__(self, num: int):  # +
#         return Circle(self.radius + num)
#
#     def __iadd__(self, num: int):  # +=
#         self.radius += num
#
#     def __sub__(self, num: int):  # +
#         pass
#
#     def __isub__(self, num: int):  # +
#         pass

# 3
class Airplane:
    def __init__(self, airplane: int):
        self.airplane = airplane

    def human(self):
        return self.airplane

    def __eq__(self, other):  # ==
        return self.airplane == other.radius

    def __lt__(self, other):  # <
        return self.human() < other.circ_len()

    def __le__(self, other):  # <=
        pass

    def __gt__(self, other):  # >
        pass

    def __ge__(self, other):  # >=
        pass

    def __add__(self, num: int):  # +
        return Airplane(self.airplane + num)

    def __iadd__(self, num: int):  # +=
        self.airplane += num

    def __sub__(self, num: int):  # +
        pass

    def __isub__(self, num: int):  # +
        pass


# времени мало, не успеваю некоторые сделать
# Ничего страшного, главное, что что-то вы успеваете делать. 
# Жалко, конечно, что комплексные числа пропустили, интересная задачка
