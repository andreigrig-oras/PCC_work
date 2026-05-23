from Employee import Employee
import pytest

@pytest.fixture
def create_employee ():
    employee=Employee("dan","mathews",1)
    return employee    

def test_give_defauls_raise(create_employee):
    create_employee.give_raise()
    assert create_employee.salary_review() == 5001

def test_give_custom_raise(create_employee):
    create_employee.give_raise(1)
    assert create_employee.salary_review() == 2