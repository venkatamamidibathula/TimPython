courses = ["python", "java", "go"]

students_enrolled = {
    "Mahesh": {"Git", "Python","Java", "Docker"},
    "Ganesh": {"Python","Java","Go"},
    "Jim": {"Python","Java","Go","Full Stack"}
}
#<= gives subset
#< proper subset
students = []
for applicant,courses_enrolled in students_enrolled.items():
    if set(courses) < set(item.lower() for item in courses_enrolled):
        students.append(applicant)
print(students)