# BMI Calculation Program with Unit Selection

def calculate_bmi(weight, height, is_metric=True):
    """
    Calculate the BMI value.
    If is_metric is True, use kg and meters.
    If is_metric is False, use pounds and inches.
    """
    if is_metric:
        return weight / (height ** 2)
    else:
        return (weight / (height ** 2)) * 703

def get_bmi_category(bmi):
    #Return the BMI category based on the BMI value.

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obese (Class I)"
    elif 35 <= bmi < 39.9:
        return "Obese (Class II)"
    else:
        return "Extremely Obese (Class III)"

def get_user_input(is_metric):
    #Get height and weight from the user based on the selected unit system.

    try:
        if is_metric:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters (e.g., 1.75): "))
        else:
            weight = float(input("Enter your weight in pounds: "))
            height = float(input("Enter your height in inches (e.g., 70): "))
        return weight, height
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

def display_results(bmi, category):
    #Display the BMI value and category to the user.

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")

def main():
    print("Welcome to the BMI (Body Mass Index) Calculation Program!\n")

    while True:
        # Ask the user to select the unit system
        unit_choice = input("Choose unit system:\n1. Metric (kg, meters)\n2. American (pounds, inches)\nEnter your choice (1 or 2): ").strip()
        is_metric = unit_choice == '1'

        weight, height = get_user_input(is_metric)
        if weight is not None and height is not None:
            bmi = calculate_bmi(weight, height, is_metric)
            category = get_bmi_category(bmi)
            display_results(bmi, category)

        # Ask the user if they want to calculate again
        restart = input("\nDo you want to perform another calculation? (Y/N): ").strip().lower()
        if restart != 'y':
            print("Program terminated. Goodbye!")
            break

if __name__ == "__main__":
    main()