def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 70:
        return "A"    
    elif score >= 60:
        return "B"   
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"  
    else: 
        return "F"   
name = input("Enter student's name:")
while True:
    try:
        score = int(input("Enter the student's score:"))
        if score < 0 or score > 100:
            print("Score must be betwwen 0 and 100!")
            continue
        break
    except ValueError:
         print("Please enter a valid number!")
grade = calculate_grade(score)    
print("Student:", name)
print("Grade:" , grade)
if score <= 0 or score >= 100:
    print("Status: Invalid score")
elif score >= 45:
    print("Status: Pass")
else:
    print("Status: Fail")    