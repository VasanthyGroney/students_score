from input import students

def students_grade(students):
    grades = []
    for student in students:
        name = student['name']
        scores = student['scores']
        average = sum(scores) / len(scores)
        grade = find_average(average)
        grades.append({
            "name": name,
            "average": round(average, 2),
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

def get_topper(grades):
    return max(grades, key=lambda x: x['average'])

def generate_html(grades, topper):
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Grades</title>
        <style>
            table {{ border-collapse: collapse; width: 50%; margin: auto; }}
            th, td {{ border: 1px solid black; padding: 8px; text-align: center; }}
            th {{ background-color: #f2f2f2; }}
            .topper {{ background-color: #d4edda; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">Student Grades</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Average</th>
                <th>Grade</th>
            </tr>
            {}
        </table>
        <h3 style="text-align: center;">Topper: {} with Average {}</h3>
    </body>
    </html>
    """
    rows = ""
    for student in grades:
        topper_class = "topper" if student == topper else ""
        rows += f"""
        <tr class="{topper_class}">
            <td>{student['name']}</td>
            <td>{student['average']}</td>
            <td>{student['grade']}</td>
        </tr>
        """
    return html_template.format(rows, topper['name'], topper['average'])

# Process the student grades
processed_grades = students_grade(students)
topper = get_topper(processed_grades)

# Generate and save the HTML scoreboard
html_content = generate_html(processed_grades, topper)
with open("student_grades.html", "w") as file:
    file.write(html_content)

print("HTML scoreboard generated: student_grades.html")
