import csv
filename = "students"
#  Load Data 
    
def load_data():
    students = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    "roll": int(row["roll"]),
                    "name": row["name"],
                    "marks": float(row["marks"])
                })
    except FileNotFoundError:
        pass
    return students
#  Save Data 
def save_data(students):
    with open(filename, "w", newline="") as file:
        fieldnames = ["roll", "name", "marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
#  Add Student 
def add_student(students):
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        for student in students:
            if student["roll"] == roll:
                print(" Roll number already exists!")
                return
        students.append({"roll": roll, "name": name, "marks": marks})
        save_data(students)
        print(" Student Added Successfully")
    except ValueError:
        print(" Invalid input! Please enter correct values.")
#  View Students 
def view_students(students):
    if not students:
        print(" No Student Records Found!")
        return
    print("\n------ Student Records ------")
    print("Roll\tName\tMarks")
    for student in students:
        print(f"{student['roll']}\t{student['name']}\t{student['marks']}")
    print("-----------------------------")
#  Search Student 
def search_student(students):
    try:
        roll = int(input("Enter Roll Number to Search: "))
        for student in students:
            if student["roll"] == roll:
                print("\n Student Found:")
                print(f"Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}")
                return
        print(" Student Not Found!")
    except ValueError:
        print(" Enter a valid roll number!")
#  Update Student 
def update_student(students):
    try:
        roll = int(input("Enter Roll Number to Update: "))
        for student in students:
            if student["roll"] == roll:
                student["name"] = input("Enter New Name: ")
                student["marks"] = float(input("Enter New Marks: "))
                save_data(students)
                print(" Student Updated Successfully!")
                return
        print(" Student Not Found!")
    except ValueError:
        print(" Invalid input!")
#  Delete Student 
def delete_student(students):
    try:
        roll = int(input("Enter Roll Number to Delete: "))
        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                save_data(students)
                print(" Student Deleted Successfully!")
                return
        print(" Student Not Found!")
    except ValueError:
        print(" Enter valid roll number!")
#  Sort Students 
def sort_students(students):
    if not students:
        print(" No records to sort!")
        return
    print("\n1. Sort by Name")
    print("2. Sort by Marks")
    choice = input("Enter choice: ")
    if choice == "1":
        students.sort(key=lambda x: x["name"].lower())
        print(" Sorted by Name Successfully!")
    elif choice == "2":
        students.sort(key=lambda x: x["marks"], reverse=True)
        print(" Sorted by Marks Successfully!")
    else:
        print(" Invalid Choice!")
        return
    view_students(students)
#  Reports 
def generate_report(students):
    if not students:
        print(" No records available!")
        return
    topper = max(students, key=lambda x: x["marks"])
    average = sum(student["marks"] for student in students) / len(students)
    print("\n------ REPORT ------")
    print(f" Topper: {topper['name']} (Roll: {topper['roll']}, Marks: {topper['marks']})")
    print(f" Average Marks: {average:.2f}")
    print("--------------------")
def admin_login():
    USERNAME = "python"
    PASSWORD = "ps@123"
    print(" ADMIN LOGIN ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == USERNAME and password == PASSWORD:
        print(" Login Successful!")
        return True
    else:
        print(" Invalid Username or Password!")
        return False
#  Main Program 
def main():
    students = load_data()
    if not admin_login():
        return
    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM ")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Generate Report")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            sort_students(students)
        elif choice == "7":
            generate_report(students)
        elif choice == "8":
            print(" Exit Program")
            break
        else:
            print(" Invalid choice! Try again.")
if __name__ == "__main__":
    main()