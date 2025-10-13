# # python compound interest calculator
# # A = P (1 + r/n) ^ nt
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: ")) / 100
# time = float(input("Enter the time in years: "))
# n = float(input("Enter the number of times interest is compounded per year: "))
# amount = principal * (1 + rate / n) ** (n * time)
# print(f"The amount after {time} years is: {amount:.2f}")
# # A = P (1 + r/n) ^ nt
# interest = amount - principal
# print(f"The interest earned after {time} years is: {interest:.2f}")

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principal amount (greater than 0): "))
#     if principle <= 0:
#         print("Principal amount must be greater than 0. Please try again.")
# while rate <= 0:
#     rate = float(input("Enter the rate of interest (greater than 0): "))
#     if rate <= 0:
#         print("Rate of interest must be greater than 0. Please try again.")
# while time <= 0:
#     time = float(input("Enter the time in years (greater than 0): "))
#     if time <= 0:
#         print("Time must be greater than 0. Please try again.")
# n = float(input("Enter the number of times interest is compounded per year: "))
# amount = principle * (1 + rate / (100 * n)) ** (n * time)
# print(f"The amount after {time} years is: {amount:.2f}")

# and the interest earned
asalu = 0
vaddi = 0
kaalam = 0

while True:
    asalu = float(input("Enter the principal amount (greater than 0): "))
    if asalu > 0:
        break
    print("Principal amount must be greater than 0. Please try again.")
while True:
    vaddi = float(input("Enter the rate of interest (greater than 0): "))
    if vaddi > 0:
        break
    print("Rate of interest must be greater than 0. Please try again.")
while True:
    kaalam = float(input("Enter the time in years (greater than 0): "))
    if kaalam > 0:
        break
    print("Time must be greater than 0. Please try again.")
mottham = asalu * (1 + vaddi / 100) ** kaalam
print(f"The amount after {kaalam} years is: {mottham:.2f}")