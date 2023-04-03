class father:
    def __init__(self) -> None:
        self.a = 10
        print("father init")
class son(father):
    # def  __init__(self) -> None:
    #     super().__init__()
    #     print("son init")
    pass

s = son()

print(s.__dict__)