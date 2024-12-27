def input_grades():
    grades = {}
    while True:
        subject = input("Enter the subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            grades[subject] = grade
        except ValueError:
            print("Invalid input! Please enter a numeric grade.")
    return grades

def calculate_average(grades):
    if grades:
        return sum(grades.values()) / len(grades)
    return 0

def store_grades_in_file(grades, file_name):
    with open(file_name, 'w') as file:
        for subject, grade in grades.items():
            file.write(f"{subject}: {grade}\n")

def main():
    grades = input_grades()
    average = calculate_average(grades)
    print(f"Average grade: {average}")
    store_grades_in_file(grades, 'grades.txt')

main()
