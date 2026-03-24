BASE_FEE = 1000

COUPLE_DISCOUNT = 40      # percent
CHILD_DISCOUNT = 60       # percent
ADULT_DISCOUNT = 32      # percent
SENIOR_DISCOUNT = 25      # percent


def calculate_individual_discount(age):
    if age < 18:
        return CHILD_DISCOUNT
    elif age <= 50:
        return ADULT_DISCOUNT
    else:
        return SENIOR_DISCOUNT


def main():
    print("\n" + "=" * 35)
    print("Welcome to the Gym!")
    print(f"Base Fee: ₹{BASE_FEE}")
    print("=" * 35)

    couple = input("Are you registering as a couple? (yes/no): ").strip().lower()

    if couple not in ("yes", "no"):
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    # Couple membership branch
    if couple == "yes":
        total_base = BASE_FEE * 2
        discount_amount = total_base * (COUPLE_DISCOUNT / 100)
        final_fee = total_base - discount_amount

        print(f"Total Base Fee (2 people): ₹{total_base:.2f}")
        print(f"Couple Discount ({COUPLE_DISCOUNT}%): ₹{discount_amount:.2f}")
        print(f"Final Couple Fee: ₹{final_fee:.2f}")

    # Individual membership branch
    else:
        try:
            age = int(input("Enter your age: ").strip())
        except ValueError:
            print("Invalid input. Age must be a number.")
            return

        if age < 0 or age > 120:
            print("Invalid age.")
            return

        discount_percent = calculate_individual_discount(age)
        discount_amount = BASE_FEE * (discount_percent / 100)
        final_fee = BASE_FEE - discount_amount

        print(f"Discount ({discount_percent}%): ₹{discount_amount:.2f}")
        print(f"Final Individual Fee: ₹{final_fee:.2f}")


# if __name__ == "__main__":
main()