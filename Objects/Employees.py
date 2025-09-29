class Employee:
    count = 0

    def __init__(self, empid=100, name="aaa", salary=5000):
        self._empid = empid
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError('Salary is cannot be zero or negative')
        else:
            self._salary = value

    def calculate_sal(self):
        hra = self._salary * 0.4
        da = self._salary * 0.15
        return self._salary + hra + da

    def __str__(self):
        return f"Employee details ID: {self._empid} Name: {self._name} and Salary is: {self._salary}"

    def __repr__(self):
        return f"Employee ({self._empid} , {repr(self._name)} , {self._salary})"

    def calc_premium(self):
        return f"the premium is : {self._salary * 0.01}"


#         return f"Employee ({self._empid} , '{self._name}' , {self._salary})"
# can be used with inside '' or with repr() to represent string
class NewEmployee:
    count = 0  # Class Attribute

    def __init__(self, name="aaa", salary=10000):
        NewEmployee.count += 1
        self._empid = NewEmployee.count
        self._name = name
        self._salary = salary


    def calculate_sal(self):
        hra = self._salary * 0.4
        da = self._salary * 0.15
        return self._salary + hra + da

    def __str__(self):
        return f"Employee details ID: {self._empid} Name: {self._name} and Salary is: {self._salary}"

    def __repr__(self):

        return f"Employee ({self._empid} , {repr(self._name)} , {self._salary})"

    @staticmethod
    def show_employee_count():
        print('Employee count', NewEmployee.count)

    @classmethod
    def set_count(cls):
        cls.count = 100


