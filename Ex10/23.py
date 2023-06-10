class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)
class Mealy:
    def __init__(self):
        self.state = "A"
    def clean(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "E":
            self.state = "F"
            return 5
        if self.state == "F":
            self.state = "G"
            return 7
        if self.state == "G":
            self.state = "D"
            return 9
        if self.state == "H":
            self.state = "B"
            return 10
        else:
            raise MealyError("clean")
    def pluck(self):
        if self.state == "A":
            self.state = "D"
            return 1
        if self.state == "E":
            self.state = "B"
            return 6
        if self.state == "H":
            self.state = "D"
            return 11
        if self.state == "G":
            self.state = "H"
            return 8
        else:
            raise MealyError("pluck")
def main():
    return Mealy()

def test():
    obj = main()
    for s in "ABCDEFGH":
        obj.state = s
        try:
            obj.clean()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.pluck()
        except MealyError:
            pass

o = main()
print(o.clean()) # 0
print(o.clean()) # 2
# print(o.pluck()) # MealyError
print(o.clean()) # 3
# print(o.pluck()) # MealyError
print(o.clean()) # 4
print(o.clean()) # 5
print(o.clean()) # 7
print(o.clean()) # 9
print(o.clean()) # 4
print(o.clean()) # 5
print(o.clean()) # 7
print(o.pluck()) # 8
print(o.pluck()) # 11
print(o.clean()) # 4
print(o.pluck()) # 6
print(o.clean()) # 2