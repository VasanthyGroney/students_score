from input import students

def students_grade(students):
    grades = []
    for student in students:
        name = student['name']
        scores = student['scores']
        average = sum(scores) / len(scores)
        grade = find_average(average)  # Call find_average with the average score
        grades.append({
            "name": name,
            "average": round(average, 2),  # Round average to 2 decimal places
            "grade": grade
        })
    return grades

def find_average(average):
    if average == 100:
        return "Outstanding"
    elif 90 <= average <= 99:
        return "A grade"
    elif 80 <= average <= 89:
        return "B grade"
    elif 70 <= average <= 79:
        return "C grade"
    elif 60 <= average <= 69:
        return "D grade"
    elif 50 <= average <= 59:
        return "E grade"
    elif 1 <= average <= 49:
        return "F grade"
    else:
        return "Invalid entry"

# Process the student grades
processed_grades = students_grade(students)

# Print the results
for grade in processed_grades:
    print(grade)
