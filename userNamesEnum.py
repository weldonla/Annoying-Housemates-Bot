class UserNamesEnum:
    Jake = "jacob_adam_weldon"
    Luke = "weldonla"
    Nat = "GnatOnTheWall"
    James = "soManyFeathers"

    def __init__(self) -> None:
        pass

    def getShortHand(self, userName: str):
        if userName == self.Jake:
            return "JAW"
        if userName == self.Luke:
            return "LAW"
        if userName == self.Nat:
            return "NW"
        if userName == self.James:
            return "JVD"