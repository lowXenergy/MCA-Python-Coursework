import time

REQUIRED_TEMP = -28
MIN_TEMP = -80
MAX_TEMP = 20

try:
    temp = int(input("Enter current temperature (°C): ").strip())
except ValueError:
    print("Invalid input. Please enter a numeric temperature.")
    exit()

if temp < MIN_TEMP or temp > MAX_TEMP:
    print(f"Temperature must be between {MIN_TEMP}°C and {MAX_TEMP}°C.")
    exit()

print("\nStarting Temperature Control System...")

while True:
    if temp > REQUIRED_TEMP:
        print(f"Cooling ON  | Temp: {temp}°C")
        temp -= 1
        time.sleep(1)

    elif temp < REQUIRED_TEMP:
        print(f"Heating ON  | Temp: {temp}°C")
        temp += 1
        time.sleep(1)

    else:
        print(f"System OFF  | Temp stabilized at {temp}°C")
        break



# import time

# REQUIRED_TEMP = -28
# MIN_TEMP = -80
# MAX_TEMP = 20

# # External environment influence (per cycle)
# EXTERNAL_INFLUENCE = 0.5


# def main():
#     try:
#         temp = float(input("Enter current internal temperature (°C): ").strip())
#     except ValueError:
#         print("Invalid input. Please enter a numeric temperature.")
#         return

#     if temp < MIN_TEMP or temp > MAX_TEMP:
#         print(f"Temperature must be between {MIN_TEMP}°C and {MAX_TEMP}°C.")
#         return

#     external_temp = float(input("Enter external temperature (°C): ").strip())

#     # Freezer initially empty
#     has_items = input("Are there items inside the freezer? (yes/no): ").strip().lower()

#     if has_items not in ("yes", "no"):
#         print("Invalid input for freezer contents.")
#         return

#     print("\nStarting Deep Freezer System...\n")

#     while True:

#         # External temperature slowly affects internal temp
#         temp += (external_temp - temp) * EXTERNAL_INFLUENCE * 0.1

#         if has_items == "no":
#             print(f"Freezer OFF | Temp drifting to {temp:.2f}°C (empty)")
#             time.sleep(1)

#             # Allow user to place items later
#             has_items = input("Place items in freezer? (yes/no): ").strip().lower()
#             continue

#         # If items are present, regulate temperature
#         if temp > REQUIRED_TEMP:
#             print(f"Cooling ON  | Temp: {temp:.2f}°C")
#             temp -= 1

#         elif temp < REQUIRED_TEMP:
#             print(f"Heating ON  | Temp: {temp:.2f}°C")
#             temp += 1

#         else:
#             print(f"Stable at {temp:.2f}°C | Maintaining")

#         time.sleep(1)


# if __name__ == "__main__":
#     main()