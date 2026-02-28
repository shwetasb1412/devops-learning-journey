class Employee:
    def __init__(self, emp_id, name,department,basic_salary,experience_years):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.basic_salary=basic_salary
        self.experience_years=experience_years

    
    def calculate_annual_salary(self):
        annual_salary=self.basic_salary*12
        return annual_salary
    
    def apply_increment(self,increment_percent):
        self.basic_salary=self.basic_salary+(self.basic_salary*increment_percent/100)
        print(f"Updated basic salary:{self.basic_salary}")
    
    def add_experience(self,years):
        self.experience_years=self.experience_years+years
        print(f"Updated basic salary:{self.experience_years}")

    def change_department(self, department):
        self.department=department
    
    def get_employee_summary(self):
        print(f"Employee id: {self.emp_id}, Name: {self.name}, Department: {self.department}, experience years: {self.experience_years}, current basic salary: {self.basic_salary}")


E1=Employee(101,"Ethan","SOC",70000,0)
E1.get_employee_summary()
E1.calculate_annual_salary()
E1.apply_increment(10)
E1.add_experience(10)
E1.change_department("IAM")
E1.get_employee_summary()
