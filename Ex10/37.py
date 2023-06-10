class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)

class Mealy():
    def __init__(self):
        self.state = "A"
    def jog(self):
        if self.state == "A":
            self.state = "A"
            return 1
        if self.state == "D":
            self.state = "E"
            return 4
        else:
            raise MealyError("jog")

    def hurry(self):
        if self.state == "A":
            self.state = "B"
            return 0
        else:
            raise MealyError("hurry")

    def close(self):
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "E":
            self.state = "B"
            return 6
        if self.state == "H":
            self.state = "D"
            return 11
        if self.state == "F":
            self.state = "G"
            return 7
        if self.state == "G":
            self.state = "H"
            return 8
        else:
            raise MealyError("close")

    def post(self):
        if self.state == "E":
            self.state = "F"
            return 5
        if self.state == "H":
            self.state = "E"
            return 10
        if self.state == "G":
            self.state = "G"
            return 9
        else:
            raise MealyError("post")

def main():
    return Mealy()

def test():
    obj = main()
    for s in "ABCDEFGH":
        obj.state = s
        try:
            obj.post()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.jog()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.close()
        except MealyError:
            pass
        obj.state = s
        try:
            obj.hurry()
        except MealyError:
            pass

o = main()
print(o.jog()) # 1
print(o.hurry()) # 0
print(o.close()) # 2
print(o.close()) # 3
print(o.jog()) # 4
print(o.post()) # 5
print(o.close()) # 7
print(o.post()) # 9
print(o.post()) # 9
print(o.post()) # 9
print(o.post()) # 9
print(o.post())# 9
print(o.close()) # 8
print(o.post()) # 10
print(o.close()) # 6
print(o.close()) # 2