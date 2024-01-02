class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, position, salary):
        if emp_id not in self.employees:
            self.employees[emp_id] = {'name': name, 'position': position, 'salary': salary}
            print(f"Employee {emp_id} added successfully.")
        else:
            print(f"Employee {emp_id} already exists. Use update option to modify details.")

    def view_employee(self, emp_id):
        if emp_id in self.employees:
            employee_details = self.employees[emp_id]
            print(f"Employee ID: {emp_id}")
            print(f"Name: {employee_details['name']}")
            print(f"Position: {employee_details['position']}")
            print(f"Salary: ${employee_details['salary']}")
        else:
            print(f"Employee {emp_id} not found.")

    def update_employee(self, emp_id, name=None, position=None, salary=None):
        if emp_id in self.employees:
            employee_details = self.employees[emp_id]
            if name:
                employee_details['name'] = name
            if position:
                employee_details['position'] = position
            if salary:
                employee_details['salary'] = salary
            print(f"Employee {emp_id} details updated successfully.")
        else:
            print(f"Employee {emp_id} not found.")

    def display_all_employees(self):
        print("Employee Records:")
        for emp_id, details in self.employees.items():
            print(f"Employee ID: {emp_id}, Name: {details['name']}, Position: {details['position']}, Salary: ${details['salary']}")

# Example usage
ems = EmployeeManagementSystem()

ems.add_employee(1, 'John Doe', 'Manager', 50000)
ems.add_employee(2, 'Jane Smith', 'Developer', 60000)

ems.display_all_employees()

ems.view_employee(1)

ems.update_employee(1, salary=55000)

ems.display_all_employees()
