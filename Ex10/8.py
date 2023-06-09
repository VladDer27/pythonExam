class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class Mealy:
    def __init__(self):
        self.state = "A"

    def paint(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "B"
            return 3
        if self.state == "C":
            self.state = "D"
            return 4
        if self.state == "D":
            self.state = "E"
            return 7
        else:
            raise MealyError("paint")

    def speed(self):
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "A"
            return 5
        else:
            raise MealyError("speed")

    def init(self):
        if self.state == "B":
            self.state = "E"
            return 2
        if self.state == "C":
            self.state = "E"
            return 6
        if self.state == "E":
            self.state = "F"
            return 8
        else:
            raise MealyError("init")


def main():
    return Mealy()


def test():
    obj = main()
    for s in "ABCDEF":
        obj.state = s
        try:
            obj.paint()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.init()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.speed()
        except MealyError:
            pass


o = main()
# print(o.paint())  # 0
# print(o.paint())  # 3
# print(o.speed())  # 1
# print(o.speed())  # 5
# print(o.paint())  # 0
# print(o.paint())  # 3
# print(o.speed())  # 1
# print(o.paint())  # 4
# print(o.paint())  # 7
# print(o.init())  # 8
print(o.paint()) # 0
print(o.speed()) # 1
print(o.speed()) # 5
# print(o.init()) # MealyError
print(o.paint()) # 0
print(o.paint()) # 3
print(o.paint()) # 3
print(o.speed())# 1
print(o.paint()) # 4
print(o.paint()) # 7
print(o.init()) # 8
