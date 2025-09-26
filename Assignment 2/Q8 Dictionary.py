"""Q.8 For a given dictionary [Add few more entries]

employees = {'Amol' : ['C', 'C++','Java'],.....}

1. print employees and their skill sets
2. Find all the employees who know Java
3. Update skill for an employee
4. Add/remove employee data"""

employees = {
    'Amol': ['C', 'C++', 'Java'],
    'Priya': ['Python', 'JavaScript', 'SQL'],
    'Rahul': ['Python', 'R', 'Scala'],
    'Sneha': ['Java', 'Kotlin', 'Go'],
    'Vikram': ['C#', 'Python', 'TypeScript']
}

# 1. Print employees and skills
print("Employees and skills:")
for name, skills in employees.items():
    print(name, ":", skills)

# 2. Find employees who know Java
print("\nEmployees who know Java:")
for name, skills in employees.items():
    if 'Java' in skills:
        print(name)

# 3. Update skill for an employee
# Example: Add Python to Amol, remove SQL from Priya
employees['Amol'].append('Python')
employees['Priya'].remove('SQL')
print("\nAfter updating skills:")
for name, skills in employees.items():
    print(name, ":", skills)

# 4. Add/remove employee
# Example: Add Neha, remove Vikram
employees['Neha'] = ['Ruby', 'Perl']
del employees['Vikram']
print("\nAfter adding Neha and removing Vikram:")
for name, skills in employees.items():
    print(name, ":", skills)

