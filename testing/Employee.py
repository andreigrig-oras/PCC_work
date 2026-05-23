class Employee:
    def __init__ (self, f_name, l_name, salary):
        self.f_name=f_name
        self.l_name=l_name
        self.salary=int(salary)
    def give_raise(self, raise_increase=5000):
        self.salary+=raise_increase
    def salary_review(self):
        return (self.salary)

#Dan=Employee("dan","murphy","40000")
#Dan.give_raise()
#print(f"Dan's salary is now: {Dan.salary_review()}")