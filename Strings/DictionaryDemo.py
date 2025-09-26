weather_data = {"pune":[23,28],
                "mumbai":[32,37],
                "Delhi":[35,40]}

emp = {"name":"ABC",
       "age":180,
       "salary":200000.00,
       "skills":["python","C++","C#"]}

print("pune" in weather_data)
print("")

print("---------------")
for key , val in weather_data.items():
    print(key,val)

for val in weather_data.values():
    print(val)

for key in weather_data.keys():
    print(key)

emp.update({"age":60})
print(emp)

emp["skills"] = "python"
print(emp)

