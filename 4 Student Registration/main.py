print("MCA Function Registration System")

MAX_SEATS = 100
TXT_FILE = "registrations.txt"

registered_students = []


def load_from_file():
    try:
        with open(TXT_FILE, "r") as file:
            for line in file:
                try:
                    roll, name, course, day = line.strip().split(":")
                    registered_students.append({
                        "roll": roll,
                        "name": name,
                        "course": course,
                        "day": int(day)
                    })
                except ValueError:
                    # Skip corrupted lines instead of crashing
                    continue
    except FileNotFoundError:
        pass


def save_to_file(student):
    with open(TXT_FILE, "a") as file:
        file.write(
            f"{student['roll']}:{student['name']}:{student['course']}:{student['day']}\n"
        )


def roll_exists(roll):
    return any(student["roll"] == roll for student in registered_students)


def check_registration(course, day):
    if course.upper() != "MCA":
        return False, "Registration Failed: Only MCA students are allowed."

    if day > 25:
        return False, "Registration Failed: The deadline was May 25."

    if len(registered_students) >= MAX_SEATS:
        return False, "Registration Failed: All seats are full."

    return True, "Success! You are registered."


def list_registrations():
    if not registered_students:
        print("No students registered yet.")
        return

    print("\nRegistered Students")
    for student in registered_students:
        print(
            f"Roll: {student['roll']} | "
            f"{student['name']} ({student['course']}) - Day {student['day']}"
        )


def main():
    load_from_file()

    while True:
        print("\nSelect any option:")
        print("1. Register Student")
        print("2. View Registered Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # print(f"\nSeats filled: {len(registered_students)}/{MAX_SEATS}")
            print(f"\nSeats filled: 100/100")

            if len(registered_students) >= MAX_SEATS:
                print("Can't register. All seats are already filled.")
                continue

            # roll = input("Enter Roll Number: ").strip()

            # if roll_exists(roll):
            #     print("This roll number is already registered.")
            #     continue

            roll = input("Enter Roll Number: ").strip()

            if not roll.isdigit() or int(roll) < 0:
                print("Invalid roll number. It must be a non-negative number.")
                continue

            if roll_exists(roll):
                print("This roll number is already registered.")
                continue

            name = input("Enter your name: ").strip()
            course = input("Enter your course: ").strip().upper()

            day_input = input("Enter registration date: ")
            if not day_input.isdigit():
                print("Invalid date. Please enter a number.")
                continue

            day = int(day_input)

            allowed, message = check_registration(course, day)
            print(message)

            if allowed:
                student = {
                    "roll": roll,
                    "name": name,
                    "course": course.upper(),
                    "day": day
                }

                save_to_file(student)
                registered_students.append(student)

        elif choice == "2":
            list_registrations()

        elif choice == "3":
            print("Exiting")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()