# 2025.08.21
# 10_dictionary.py

scores = { 'Kim': 90, 'Yamada': 85, "John": 80 }

for name, score in scores.items() :
    print(f'{name} got {score} points.')

print(scores["Yamada"])