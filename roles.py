class Base:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Manager(Base):
    def __init__(self, name, position="manager"):
        super().__init__(name, position)

    @staticmethod
    def look_at_report(report):
        print(report)


class Salesman(Base):
    def __init__(self, name, position="salesman"):
        super().__init__(name, position)

    @staticmethod
    def look_at_bill(bill):
        print(bill)
