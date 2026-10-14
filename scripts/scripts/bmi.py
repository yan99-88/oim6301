def compute_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify the BMI into categories"""
    # print(bmi)
    if bmi >= 30:
        category = "Obese"
    elif bmi >= 25:
        category = "Overweight"
    elif bmi >= 18.5:
        category = "Normal"
    else:
        category = "Underweight"
    return category

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi_value = compute_bmi(weight, height)
    category = classify_bmi(bmi_value)
    print(f"Your BMI is: {bmi_value:.2f}")
    print(f"Your category is: {category}")

if __name__ == "__main__":
    main()