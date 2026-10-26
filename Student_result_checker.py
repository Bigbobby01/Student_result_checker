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