import datetime
import os
import sys

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

PLANS = {
    "1": {"name": "Monthly",   "months": 1,  "price": 1000},
    "2": {"name": "Quarterly", "months": 3,  "price": 2700},
    "3": {"name": "Yearly",    "months": 12, "price": 9000},
}

DISCOUNTS = {
    "child": 60,
    "adult": 32,
    "senior": 25,
    "couple": 40,
    "prepaid": 10,
    "renewal": 5
}

HISTORY_FILE = "membership_history.txt"

# ─────────────────────────────────────────────
# INPUT HELPERS (FIXED VALIDATION)
# ─────────────────────────────────────────────

def get_yes_no(prompt):
    while True:
        try:
            val = input(prompt).strip().lower()
            if val in ("yes", "no"):
                return val
            print("Invalid input. Please enter 'yes' or 'no'.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit()

def get_int(prompt, min_val=0, max_val=120):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit()

# ─────────────────────────────────────────────
# FESTIVAL ENGINE
# ─────────────────────────────────────────────

FESTIVALS = [
    ("New Year", 1, 1, 7, 20),
    ("Holi", 3, 20, 28, 15),
    ("Eid", 4, 1, 30, 15),
    ("Independence Day", 8, 13, 17, 12),
    ("Navratri", 10, 1, 12, 10),
    ("Diwali", 10, 18, 30, 25),
    ("Christmas & NYE", 12, 24, 31, 20),
]

def get_festival_discount():
    today = datetime.date.today()
    for name, month, start, end, discount in FESTIVALS:
        if today.month == month and start <= today.day <= end:
            return name, discount
    return None, 0

# ─────────────────────────────────────────────
# MEMBER DISCOUNT
# ─────────────────────────────────────────────

def get_member_discount(age, married):
    if married == "yes":
        return DISCOUNTS["couple"], "Couple"
    elif age < 18:
        return DISCOUNTS["child"], "Child"
    elif age <= 50:
        return DISCOUNTS["adult"], "Adult"
    else:
        return DISCOUNTS["senior"], "Senior"

# ─────────────────────────────────────────────
# FILE HANDLING
# ─────────────────────────────────────────────

def save_membership(name, phone, plan, start, end, price, festival):
    with open(HISTORY_FILE, "a") as f:
        tag = f" [{festival}]" if festival else ""
        f.write(f"{name} | {phone} | {plan} | {start} → {end} | ₹{price:.2f}{tag}\n")

def load_history(name, phone):
    if not os.path.exists(HISTORY_FILE):
        return None

    last = None
    with open(HISTORY_FILE, "r") as f:
        for line in f:
            if line.startswith(f"{name} | {phone}"):
                last = line.strip()
    return last

# ─────────────────────────────────────────────
# DISPLAY
# ─────────────────────────────────────────────

def show_plans():
    print("\nAvailable Plans:")
    print("-" * 40)
    for k, v in PLANS.items():
        print(f"{k}. {v['name']} — ₹{v['price']} / {v['months']} month(s)")
    print("-" * 40)

# ─────────────────────────────────────────────
# MAIN FLOW
# ─────────────────────────────────────────────

def main():
    print("\n" + "="*45)
    print("WELCOME TO LOCAL GYM")
    print("="*45)

    # --- Name ---
    name = input("Enter your name: ").strip()
    if not name:
        print("Invalid name.")
        return

    # --- Phone ---
    phone = input("Enter your phone number: ").strip()
    if not phone.isdigit() or len(phone) < 8:
        print("Invalid phone number.")
        return

    # --- Existing Member ---
    history = load_history(name, phone)
    if history:
        print("\nPrevious record found:")
        print(history)
        is_renewal = get_yes_no("Renew membership? (yes/no): ") == "yes"
    else:
        print("\nNew Member Registration")
        is_renewal = False

    # --- Age ---
    age = get_int("Enter age: ")

    # --- Marital ---
    married = get_yes_no("Are you married? (yes/no): ")

    # --- Prepaid ---
    prepaid = get_yes_no("Pay upfront (prepaid)? (yes/no): ")

    # --- Plan ---
    show_plans()
    choice = input("Select plan (1/2/3): ").strip()
    if choice not in PLANS:
        print("Invalid plan.")
        return

    plan = PLANS[choice]
    base_price = plan["price"]
    months = plan["months"]

    # --- Couple Adjustment ---
    if married == "yes":
        base_price *= 2

    # --- Discounts ---
    member_discount, label = get_member_discount(age, married)
    festival_name, fest_discount = get_festival_discount()

    price = base_price * (1 - member_discount / 100)
    price *= (1 - fest_discount / 100)

    if is_renewal:
        price *= (1 - DISCOUNTS["renewal"] / 100)

    if prepaid == "yes":
        price *= (1 - DISCOUNTS["prepaid"] / 100)

    final_price = price
    savings = base_price - final_price

    # --- Dates ---
    start = datetime.date.today()
    end = start + datetime.timedelta(days=30 * months)

    save_membership(name, phone, plan["name"], start, end, final_price, festival_name)

    # --- Receipt ---
    print("\n" + "="*45)
    print("MEMBERSHIP RECEIPT")
    print("="*45)
    print(f"Name           : {name}")
    print(f"Phone          : {phone}")
    print(f"Plan           : {plan['name']} ({months} months)")
    print(f"Start Date     : {start}")
    print(f"End Date       : {end}")
    print("-"*45)
    print(f"Base Price     : ₹{base_price:.2f}")
    print(f"Member Type    : {label} (-{member_discount}%)")

    if festival_name:
        print(f"{festival_name} Offer : -{fest_discount}%")
    else:
        print("Festival Offer : None")

    if is_renewal:
        print(f"Renewal Bonus  : -{DISCOUNTS['renewal']}%")

    if prepaid == "yes":
        print(f"Prepaid Bonus  : -{DISCOUNTS['prepaid']}%")

    print("-"*45)
    print(f"Final Price    : ₹{final_price:.2f}")
    print(f"You Saved      : ₹{savings:.2f}")
    print("="*45)

    if is_renewal:
        print("Membership Renewed Successfully!")
    else:
        print("Welcome to LOCAL GYM!")
    print("="*45)


if __name__ == "__main__":
    main()