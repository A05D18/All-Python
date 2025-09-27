"""Q.6
1.Find employees that know 'python'
2. Add a new skill - 'test' in skillset of all employees
3. Sort employees by skills
for the given dictionary of employees"""

emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'], 'Aditi': ['Python', 'PHP', 'Database']}
emp = list(map(lambda item: item[0], filter(lambda item: 'Python' in item[1], emp_data.items())))
print(emp)

for skills in emp_data.values():
    if "test" not in skills:
        skills.append("test")
print(emp_data)

res = dict(sorted(emp_data.items(), key=lambda item: item[1]))
print(res)
