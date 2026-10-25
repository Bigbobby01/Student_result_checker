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
while True:
    name = input("Enter student's name: ")
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
    print("\n" + "=" * 30)
    print("      STUDENT RESULT REPORT")
    print("=" * 30)
    print("Student Name:", name)
    print("Score:", score, "/ 100")
    print("Grade:", grade)
    if score >= 45:
        print("Status: PASS")
    else:
        print("Status: FAIL")
    print("=" * 30)
    again = input("Check another student? (yes/no): ").strip().lower()
    if again == "no":
        print("Thank you for using Student Result Checker!")
        break
        