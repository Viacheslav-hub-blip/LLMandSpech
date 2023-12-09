class Salary(object):
    def __init__(self, pay: int):
        self._pay = pay

    def getTotal(self) -> int:
        return self._pay * 12


class Employee(object):
    def __init__(self, salary: Salary, bonus: float):
        self.salary = salary
        self.bonus = bonus

    def annualSalary(self) -> str:
        return "Total " + str(self.salary.getTotal() + self.bonus)
