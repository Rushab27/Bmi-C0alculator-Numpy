import numpy as np


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI rounded to 2 decimals."""
    weight = np.array(weight_kg, dtype=float)
    height = np.array(height_m, dtype=float)

    if np.any(weight <= 0) or np.any(height <= 0):
        raise ValueError("Weight and height must be positive numbers.")

    bmi = weight / np.square(height)
    return float(np.round(bmi, 2))


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def main() -> None:
    print("BMI Calculator (Python + NumPy)")

    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi}")
        print(f"Category: {bmi_category(bmi)}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
