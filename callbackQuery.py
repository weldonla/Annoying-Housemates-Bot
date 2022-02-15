class CallBackQuery:
    typeOfQuery: str
    choreId: int
    data: any

    def __init__(self, typeOfQuery: str, choreId: int, data: any) -> None:
        self.typeOfQuery = typeOfQuery
        self.choreId = choreId
        self.data = data
        pass