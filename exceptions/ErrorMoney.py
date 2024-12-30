class ErrorMoney(ValueError):

    def __init__(self,messaggio):
        super().__init__(messaggio)
        self.messaggio = messaggio