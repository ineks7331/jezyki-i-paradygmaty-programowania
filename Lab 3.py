class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_all_employees(self):
        if not self.employees:
            print("No employees available.")
        for employee in self.employees:
            print(employee)

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [employee for employee in self.employees if not (min_age <= employee.age <= max_age)]

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                return employee
        return None

    def update_salary(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.update_salary(new_salary)
            print(f"Salary of {name} has been updated to {new_salary}.")
        else:
            print(f"Employee {name} not found.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def display_menu(self):
        print("\nEmployee Management System")
        print("1. Add new employee")
        print("2. Show all employees")
        print("3. Remove employees by age range")
        print("4. Update salary")
        print("5. Exit")

    def add_employee(self):
        name = input("Enter name (First Last): ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        new_employee = Employee(name, age, salary)
        self.manager.add_employee(new_employee)
        print(f"Employee {name} added.")

    def show_all_employees(self):
        print("\nEmployees List:")
        self.manager.show_all_employees()

    def remove_employees_by_age_range(self):
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)
        print(f"Employees in the age range {min_age}-{max_age} have been removed.")

    def update_salary(self):
        name = input("Enter the name of the employee to update salary: ")
        new_salary = float(input(f"Enter new salary for {name}: "))
        self.manager.update_salary(name, new_salary)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.show_all_employees()
            elif choice == '3':
                self.remove_employees_by_age_range()
            elif choice == '4':
                self.update_salary()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()
