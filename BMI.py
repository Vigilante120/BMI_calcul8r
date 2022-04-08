w = float(input("Enter your weight in Kilograms: "))
ht = float(input("Enter your height in feet: "))
feet = ht * 0.3048
BM = w / feet ** 2
print("________________________________")
if BM < 18.5:
    print("You're UnderWeight", round(BM, 1))

elif BM < 24.9:
    print("You're NormalWeight", round(BM, 1))

elif BM < 29.9:
    print("You're OverWeight", round(BM, 1))

elif BM >= 29.9:
    print("You're Obese", round(BM, 1))
print("________________________________")
print("Re-run to check another BMI!")
print("________________________________")
