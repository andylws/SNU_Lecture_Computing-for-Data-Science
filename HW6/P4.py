class Calculator:
    def __init__(self):
        self.total = 0
        self.current_num = 0
        self.state = None

    def digit(self, num):
        if self.current_num == 0:
            self.current_num = num
        else:
            self.current_num = self.current_num * 10 + num

    def plus(self):
        if self.state == "plus":
            self.total = self.total + self.current_num
        elif self.state == "minus":
            self.total = self.total - self.current_num
        else:
            self.total = self.current_num
        self.current_num = 0
        self.state = "plus"

    def minus(self):
        if self.state == "plus":
            self.total = self.total + self.current_num
        elif self.state == "minus":
            self.total = self.total - self.current_num
        else:
            self.total = self.current_num
        self.current_num = 0
        self.state = "minus"

    def clear(self):
        self.total = 0
        self.current_num = 0
        self.state = None

    def equal(self):
        if self.state == "plus":
            self.total = self.total + self.current_num
        elif self.state == "minus":
            self.total = self.total - self.current_num
        else:
            self.total = self.current_num
        return self.total
