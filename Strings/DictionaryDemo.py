weather_data = {
    "pune": [23, 28],
    "mumbai": [32, 37],
    "Delhi": [35, 40],
    "Bangalore": [22, 29],
    "Chennai": [30, 36],
    "Kolkata": [29, 34],
    "Hyderabad": [25, 32],
    "Ahmedabad": [28, 35]
}

emp = [
    {"name": "ABC", "age": 30, "salary": 200000.00, "skills": ["Python", "C++", "C#"]},  # Age corrected to 30
    {"name": "Priya Sharma", "age": 29, "salary": 120000.00, "skills": ["Java", "Python", "SQL"]},
    {"name": "Michael Chen", "age": 35, "salary": 180000.00, "skills": ["C++", "JavaScript", "Go"]},
    {"name": "Anika Patel", "age": 26, "salary": 95000.00, "skills": ["Python", "R", "Tableau"]},
    {"name": "Raj Kumar", "age": 42, "salary": 210000.00, "skills": ["C#", "Azure", "Python"]},
    {"name": "Sophie Brown", "age": 31, "salary": 150000.00, "skills": ["Java", "Kotlin", "Android"]}
]

print("pune" in weather_data)
print("")

print("---------------")
# for key, val in weather_data.items():
#     print(key, val)
#
# for val in weather_data.values():
#     print(val)
#
# for key in weather_data.keys():
#     print(key)

# emp.update["name": "ABC"]({"age": 60})
# print(emp)
#
# emp["skills"] = "python"
# print(emp)

sort_by_age = list(filter(lambda item: item['age'] > 30, emp))
print(sort_by_age)

sort_by_sal = sorted(emp, key=lambda item: item['salary'])
print(sort_by_sal)

sort_by_java = list(filter(lambda item: "Java" in item['skills'], emp))
print(sort_by_java)
help(sorted)
