from bmi_calculator import calculate_bmi, bmi_category


def main():
    print("=" * 30)
    print("       BMI CALCULATOR")
    print("=" * 30)

    try:
        weight = float(input("Your weight in kg: "))
        height = float(input("Your height in meters: "))

        if weight <= 0:
            print("Weight must be greater than 0.")
            return
        if height <= 0:
            print("Height must be greater than 0.")
            return

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print("\n" + "=" * 30)
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category yours: {category}")
        print("=" * 30)

    except ValueError:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()