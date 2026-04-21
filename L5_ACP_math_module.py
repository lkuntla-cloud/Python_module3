import math

def calculate_trigonometry():
    print("Harina's Trigonometry Calculator")
    
    try:
        degree_angle = float(input("Enter the angle in degrees: "))
        radian_angle = math.radians(degree_angle)

        
        sin_value = math.sin(radian_angle)
        cos_value = math.cos(radian_angle)
        
        if math.cos(radian_angle) == 0:
            tan_value = "Undefined"
        else:
            tan_value = math.tan(radian_angle)

        print(f"\nResults for {degree_angle}°:")
        print(f"Sine:    {round(sin_value, 4)}")
        print(f"Cosine:  {round(cos_value, 4)}")
        print(f"Tangent: {tan_value if isinstance(tan_value, str) else round(tan_value, 4)}")

    except ValueError:
        print("Invalid input! Please enter a numerical value for the angle.")

if __name__ == "__main__":
    calculate_trigonometry()
