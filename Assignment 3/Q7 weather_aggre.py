"""Q.7
Following data displays min/max/average temp for cities
weather= [{'Mumbai' : [28, 30, 32]},.....]

1. Print the weather data
2. Print the city with maximum/min temp
3. Print all the cities that expereince min temp more than 30 degree
4. Create a dictionary to print 'City':'Ave temp'"""

weather = [
    {'pune': [23, (23+28)/2, 28]},
    {'mumbai': [32, (32+37)/2, 37]},
    {'Delhi': [35, (35+40)/2, 40]},
    {'Bangalore': [22, (22+29)/2, 29]},
    {'Chennai': [30, (30+36)/2, 36]},
    {'Kolkata': [29, (29+34)/2, 34]},
    {'Hyderabad': [25, (25+32)/2, 32]},
    {'Ahmedabad': [28, (28+35)/2, 35]}

]
print("-----------Weather data---------------")
for i in weather:
    for key, value in i.items():
        print(key,":",value)
print("-----------Max Temp City---------------")
max_temp_city = max(weather, key=lambda x: list(x.values())[0][2])
print(max_temp_city)
print("-----------Min Temp City---------------")
min_temp_city = min(weather, key=lambda x: list(x.values())[0][0])
print(min_temp_city)
print("-----------Hottest City---------------")
hot_cities = list(map(lambda x: list(x.keys())[0], filter(lambda x: list(x.values())[0][0] > 30, weather)))
print(hot_cities)
print("-----------Cities with avg---------------")
avg_cities = dict(map(lambda x: (list(x.keys())[0], list(x.values())[0][1]),weather))
print(avg_cities)