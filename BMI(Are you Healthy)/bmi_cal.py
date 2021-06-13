# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

Height = float(input("Enter your Height in centimeter : "))

weight = float(input("Enter Your weight : "))

Height /= 100
BMI = 0
try:
    BMI = weight/(Height*Height)
except Exception as e:
    print("Error : ", e)

BMI_final = str(round(BMI, 2))

if(BMI > 0):

    print(f"Your BMI : {BMI_final}")
    if(BMI <= 18.5):
        print("Underweight")
    elif(BMI <= 24.9):
        print("Normal Weight")
    elif (BMI <= 29.9):
        print("OverWeight")
    else:
        print("Obesity")
else:
    print("Your Data is Invalid")
