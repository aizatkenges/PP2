import json
x = [
    {
        "id": 1,
        "name": "Person 1",
        "age": 21,
        "city": "Los Angeles",
        "email": "person1@example.com"
    },
    {
        "id": 2,
        "name": "Person 2",
        "age": 22,
        "city": "New York",
        "email": "person2@example.com"
    },
    {
        "id": 3,
        "name": "Person 3",
        "age": 23,
        "city": "Los Angeles",
        "email": "person3@example.com"
    },
    {
        "id": 4,
        "name": "Person 4",
        "age": 24,
        "city": "New York",
        "email": "person4@example.com"
    },
    {
        "id": 5,
        "name": "Person 5",
        "age": 25,
        "city": "Los Angeles",
        "email": "person5@example.com"
    },
    {
        "id": 6,
        "name": "Person 6",
        "age": 26,
        "city": "New York",
        "email": "person6@example.com"
    },
    {
        "id": 7,
        "name": "Person 7",
        "age": 27,
        "city": "Los Angeles",
        "email": "person7@example.com"
    },
    {
        "id": 8,
        "name": "Person 8",
        "age": 28,
        "city": "New York",
        "email": "person8@example.com"
    },
    {
        "id": 9,
        "name": "Person 9",
        "age": 29,
        "city": "Los Angeles",
        "email": "person9@example.com"
    },
    {
        "id": 10,
        "name": "Person 10",
        "age": 30,
        "city": "New York",
        "email": "person10@example.com"
    },
    {
        "id": 11,
        "name": "Person 11",
        "age": 31,
        "city": "Los Angeles",
        "email": "person11@example.com"
    },
    {
        "id": 12,
        "name": "Person 12",
        "age": 32,
        "city": "New York",
        "email": "person12@example.com"
    },
    {
        "id": 13,
        "name": "Person 13",
        "age": 33,
        "city": "Los Angeles",
        "email": "person13@example.com"
    },
    {
        "id": 14,
        "name": "Person 14",
        "age": 34,
        "city": "New York",
        "email": "person14@example.com"
    },
    {
        "id": 15,
        "name": "Person 15",
        "age": 35,
        "city": "Los Angeles",
        "email": "person15@example.com"
    },
    {
        "id": 16,
        "name": "Person 16",
        "age": 36,
        "city": "New York",
        "email": "person16@example.com"
    },
    {
        "id": 17,
        "name": "Person 17",
        "age": 37,
        "city": "Los Angeles",
        "email": "person17@example.com"
    },
    {
        "id": 18,
        "name": "Person 18",
        "age": 38,
        "city": "New York",
        "email": "person18@example.com"
    },
    {
        "id": 19,
        "name": "Person 19",
        "age": 39,
        "city": "Los Angeles",
        "email": "person19@example.com"
    },
    {
        "id": 20,
        "name": "Person 20",
        "age": 40,
        "city": "New York",
        "email": "person20@example.com"
    }
]
y = json.dumps(x)
print(y["name"])
print(y["email"])