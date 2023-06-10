class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)
class Mealy():
    def __init__(self):
        self.state = "A"
    def send(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 3
        if self.state == "E":
            self.state = "F"
            return 8
        if self.state == "C":
            self.state = "H"
            return 5
        else:
            raise MealyError("send")
    def pose(self):
        if self.state == "A":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 4
        if self.state == "D":
            self.state = "G"
            return 7
        if self.state == "F":
            self.state = "G"
            return 9
        else:
            raise MealyError("pose")
    def run(self):
        if self.state == "A":
            self.state = "F"
            return 1
        if self.state == "D":
            self.state = "E"
            return 6
        if self.state == "F":
            self.state = "H"
            return 10
        if self.state == "G":
            self.state = "H"
            return 11
        else:
            raise MealyError("run")

def main():
    return Mealy()

def test():
    obj = main()
    for s in "ABCDEFGH":
        obj.state = s
        try:
            obj.pose()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.send()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.run()
        except MealyError:
            pass

o = main()
print(o.send()) # 0
print(o.send())# 3
print(o.pose()) # 4
print(o.run()) # 6
# print(o.run()) # MealyError
print(o.send()) # 8
# print(o.send()) # MealyError
print(o.pose()) # 9
print(o.run()) # 11