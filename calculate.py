class Calculate:
    running_total = 0
    first_number = True
    operator = ''

    def calculate(self, number, operator):
        if self.first_number:
            self.first_number = False
            self.operator = operator
            self.running_total = number
        else:
            match self.operator:
                case '+':
                    self.add(number)
                case '-':
                    self.subtract(number)
                case '/':
                    self.divide(number)
                case '*':
                    self.multiply(number)
            if operator == '=':
                self.first_number = True
                self.operator = ''
            else:
                self.operator = operator
        return self.running_total

    def add(self, number):
        self.running_total = self.running_total + number

    def subtract(self, number):
        self.running_total = self.running_total - number

    def divide(self, number):
        if number == 0:
            self.running_total = 0
        else:
            self.running_total = self.running_total / number

    def multiply(self, number):
        self.running_total = self.running_total * number

    def clear(self):
        self.running_total = 0
        self.first_number = True
        return self.running_total
