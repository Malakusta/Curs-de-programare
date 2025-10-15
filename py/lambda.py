people = [
    {"name": "Vlad", "age": 30, "city": "Bucuresti"},
    {"name": "Ana", "age": 25, "city": "Cluj"},
    {"name": "Mihai", "age": 35, "city": "Iasi"}
    ]


people.sort(key=lambda person: person["age"])

print(people)