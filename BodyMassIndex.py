import time

while True:
    a = int(input("Height (cm):"))
    b = int(input("Weight (kg):"))
    c = float(b / (a / 100) ** 2)

    print("Calculating your body mass index.")
    time.sleep(0.4)
    print("Calculating your body mass index..")
    time.sleep(0.4)
    print("Calculating your body mass index...\n")
    time.sleep(0.6)

    if c <= 18.5:
        print("Underweight")
    elif 18.5 < c < 24.9:
        print("Normal weight")
    elif 25 <= c <= 29.9:
        print("Overweight")
    elif 30 <= c < 34.9:
        print("Obesity (Class 1)")
    elif 35 <= c < 39.9:
        print("Obesity (Class 2)")
    elif c >= 40:
        print("Obesity (Class 3)")

    print("\nBody Mass Index: {}".format([c]))



