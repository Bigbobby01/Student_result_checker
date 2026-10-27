def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"
passed = 0
failed = 0
def check_student():
    global passed, failed
    while True:
        while True:
            name = input("Enter student's name: ").strip()
            if name:
                break
            print("Student name cannot be empty. Please try again!")
        while True:
            try:
                score = int(input("Enter the student's score: "))
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        grade = calculate_grade(score)
        with open("student_records.txt", "a") as file:
            file.write(f"{name} - Score: {score} - Grade: {grade}\n")
        print("Student record saved successfully!")
        print("\n" + "=" * 30)
        print("      STUDENT RESULT REPORT")
        print("=" * 30)
        print("Student Name:", name)
        print("Score:", score, "/ 100")
        print("Grade:", grade)
        if score >= 45:
            print("Status: PASS")
            passed += 1
        else:
            print("Status: FAIL")
            failed += 1
        print("=" * 30)
        again = input("Check another student? (yes/no): ").strip().lower()
        if again == "no":
            print("Thank you for using Student Result Checker!")
            break
print("\n" + "=" * 30)
print("       CLASS SUMMARY")
print("=" * 30)
print("Students Passed:", passed)
print("Students Failed:", failed)
print("Total Students:", passed + failed)
print("=" * 30)
print("\nSAVED STUDENT RECORDS")
print("=" * 30)
with open("student_records.txt", "r") as file:
    records = file.read()
print(records)
def search_student():
    search_name = input("Enter the student's name to search: ").strip().lower()
    with open("student_records.txt", "r") as file:
        records = file.readlines()
    found = False
    for record in records:
        if search_name in record.lower():
            print(record.strip())
            found = True
            break
    if not found:
        print("Student not found.")
def show_menu():
    print("\n===== STUDENT RESULT CHECKER =====")
    print()
    print("1. Check a new student")
    print("2. View saved student records")
    print("3. Search for a student")
    print("4. Exit")
    print()
    choice = input("Choose an option: ")
    return choice
while True:
    choice = show_menu()
    if choice == "1":
        check_student()
    elif choice == "2":
        with open("student_records.txt", "r") as file:
            records = file.read()
        print(records)
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you for using Student Result Checker!")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")