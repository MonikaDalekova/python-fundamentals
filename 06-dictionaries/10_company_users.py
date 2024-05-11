# company_employees = {}
# while True:
#     data = input()
#     if data == "End":
#         break
#     company_name, employee_id = data.split(" -> ")
#     if company_name not in company_employees.keys():
#         company_employees[company_name] = []
#     if employee_id not in company_employees[company_name]:
#         company_employees[company_name].append(employee_id)
#
# for company_name, employee_id in company_employees.items():
#     print(f"{company_name}")
#     # for employee in employee_id:
#     #     print(f"-- {employee}")
#     print(f"-- " + "\n-- ".join(employee_id))

#2
def company_employees(a, b):
    if a not in employee_dict:
        employee_dict[a] = []
    employee_dict[a].append(b) if b not in employee_dict[a] else b
    return employee_dict


command = input()
employee_dict = {}
while command != "End":
    company_name, employee_id = command.split(" -> ") # a and b
    employee_dict = company_employees(company_name, employee_id)
    command = input()
for company_name, ids in employee_dict.items():
    print(f"{company_name}")
    for employee in ids:
        print(f"-- {employee}")