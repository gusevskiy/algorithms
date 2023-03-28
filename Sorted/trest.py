users = [
        {"name": "Alexey", "rate": 5, "course": "Python"},
        {"name": "Andrey", "rate": 2, "course": "Python"},
        {"name": "Vasa", "rate": 5, "course": "Python"},
        {"name": "Pety", "rate": 4, "course": "PHP"},
        {"name": "Vova", "rate": 5, "course": "C#"}
    ]

max_rate = (max(users, key=lambda x: x['rate']))['name']

print(max_rate)