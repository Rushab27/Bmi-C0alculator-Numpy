import numpy as np


def calculate_bmi(weight, height):
    """
    Calculate BMI using NumPy.
    Formula:
    BMI = weight / height^2
    Parameters:
        weight: Weight in kilograms
        height: Height in meters
    Returns:
        BMI value
    """

    weight = np.array(weight)
    height = np.array(height)

    bmi=weight/np.square(height)
    return float(bmi)


def bmi_category(bmi):"""
    Determine BMI category.
    """
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"