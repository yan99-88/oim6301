import bmi

#result = bmi.compute_bmi(70, 1.75)
#print(f"Your BMI is: {result:.2f}")

people = [
    {"name": "Alice", "height": 1.65, "weight": 60},
    {"name": "Bob", "height": 1.80, "weight": 75},
    {"name": "Charlie", "height": 1.72, "weight": 68},
    {"name": "David", "height": 1.78, "weight": 82},
    {"name": "Eva", "height": 1.60, "weight": 55},
    {"name": "Frank", "height": 1.85, "weight": 90},
    {"name": "Grace", "height": 1.70, "weight": 63},
    {"name": "Henry", "height": 1.74, "weight": 71},
]

for person in people:
    #print(person)
    weight = person["weight"]
    height = person["height"]
    bmi_value = bmi.compute_bmi(person["weight"], person["height"])
    category = bmi.classify_bmi(bmi_value)
    print(f"{person['name']} has a BMI of {bmi_value:.2f} and is classified as {category}.")