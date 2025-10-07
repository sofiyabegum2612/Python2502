from functools import reduce

SYSTEM_INFO = ("Edify Technologies", "Student Management System", "v1")
ADMIN_INFO = ("9090880", "admin@edify.com")

def add_student(students):
    student_id = input("Enter ID: ")
    if student_id in students:
        print("ID Already Exist, Try with different ID")
        return students
    name = input("Enter Name: ").title()
    scores = []
    while True:
        score_input = input("Enter Score or type done: ")
        if score_input == "done":
            break
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score Should be 0-100 ")
        else:
            print("Score Should Numbers Only")
    skills = set()
    while True:
        skill_input = input("Enter Skill or type done: ")
        if skill_input == "done":
            break
        skills.add(skill_input.title())
    # Return a new dict (immutability)
    new_students = students.copy()
    new_students[student_id] = {
        "name": name,
        "scores": scores,
        "skills": skills
    }
    print("Student Saved")
    print(new_students)
    return new_students

def update_student(students):
    student_id = input("Enter ID To Update: ")
    if student_id in students:
        new_name = input("Enter New Name: ").title()
        new_students = students.copy()
        new_students[student_id]["name"] = new_name
        print("Student Name Updated")
    else:
        print("ID Doesn't Exist to Update")
        new_students = students
    print(new_students)
    return new_students

def delete_student(students):
    student_id = input("Enter ID To Delete: ")
    if student_id in students:
        new_students = students.copy()
        remove = new_students.pop(student_id)
        print(remove)
    else:
        print("ID Doesn't Exist to Delete")
        new_students = students
    print(new_students)
    return new_students

def list_students(students):
    def student_stats(data):
        name = data["name"]
        scores = data["scores"]
        if scores:
            avg = reduce(lambda x, y: x + y, scores) / len(scores)
            high_score = max(scores)
            low_score = min(scores)
        else:
            avg = high_score = low_score = 0
        skills = data["skills"]
        skills_count = len(skills)
        return name, scores, avg, high_score, low_score, skills, skills_count

    for sid, data in students.items():
        name, scores, avg, high_score, low_score, skills, skills_count = student_stats(data)
        print("=" * 50)
        print("STUDENT DETAILS")
        print("=" * 50)
        print(f"ID: {sid}")
        print(f"NAME: {name}")
        print(f"ALL SCORES: {scores}")
        print(f"AVG SCORE: {avg}")
        print(f"HIGH SCORE: {high_score}")
        print(f"LOWEST SCORE: {low_score}")
        print(f"ALL SKILLS: {skills}")
        print(f"NO OF SKILLS: {skills_count}")

def exit_system():
    print("Exit System")
    print("=" * 50)
    print("CONTACT ADMIN FOR MORE INFORMATION")
    print(f"ADMIN CONTACT NO: {ADMIN_INFO[0]}")
    print(f"ADMIN EMAIL ID: {ADMIN_INFO[1]}")
    print("=" * 50)

def main():
    students = {}
    menu_actions = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": list_students,
        "5": exit_system
    }
    while True:
        print("Choose an option: ")
        print("1 - Add Student")
        print("2 - Update Student")
        print("3 - Delete Student")
        print("4 - List Student")
        print("5 - Exit System")
        choice = input("Enter Choice (1-5): ")
        if choice in menu_actions:
            if choice == "4":
                menu_actions[choice](students)
            elif choice == "5":
                menu_actions[choice]()
                break
            else:
                students = menu_actions[choice](students)
        else:
            print("Invalid Option, Only Select (1-5)")

if __name__ == "__main__":
    main()