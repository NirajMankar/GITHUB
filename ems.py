# Simplified Employee Management System (EMS)

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, "
              f"Department: {self.department}, Salary: {self.salary}")


class EMS:
    def __init__(self):
        self.employees = {}

    # Add employee
    def add_employee(self, emp_id, name, department, salary):
        if emp_id in self.employees:
            print(" Employee ID already exists!")
        else:
            self.employees[emp_id] = Employee(emp_id, name, department, salary)
            print(" Employee added successfully!")

    # Display all employees
    def display_all(self):
        if not self.employees:
            print(" No employees found.")
        else:
            print("\n--- Employee List ---")
            for emp in self.employees.values():
                emp.display_info()

    # Search employee by ID
    def search_employee(self, emp_id):
        if emp_id in self.employees:
            print(" Employee Found:")
            self.employees[emp_id].display_info()
        else:
            print(" Employee not found.")

    # Remove employee
    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(" Employee removed successfully!")
        else:
            print(" Employee not found.")


# --- Main Program (Menu-driven) ---
def main():
    ems = EMS()

    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Remove Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            salary = input("Enter Salary: ")
            ems.add_employee(emp_id, name, department, salary)

        elif choice == "2":
            ems.display_all()

        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            ems.search_employee(emp_id)

        elif choice == "4":
            emp_id = input("Enter Employee ID to remove: ")
            ems.remove_employee(emp_id)

        elif choice == "5":
            print(" Exiting EMS. Goodbye!")
            break

        else:
            print(" Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

