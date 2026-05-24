📘 Student Registration System
A simple Python console application that allows you to register students, list them, and display approved students based on their exam grades.
This project was created as a learning exercise to practice functions, lists, dictionaries, conditionals, and file handling using JSON.

🚀 Features
Add new students

List all registered students

Display only approved students

Data persistence using a JSON file

Input validation (name, age, grade)

Automatic screen clearing for a cleaner interface

📂 Project Structure
Código
project-folder/
│
├── students.json        # Automatically generated file storing student data
├── main.py              # Main program (your script)
└── README.md            # Project documentation
🧠 How It Works
Each student is stored as a dictionary with:

python
{
    "name": "John",
    "age": 18,
    "exam_grade": 15.5
}
All students are kept inside a list called students.

A student is considered approved if:

Código
exam_grade >= 10   # Scale: 0–20
📌 Menu Options
When running the program, the user can choose:

Código
[1] Add students
[2] List students
[3] List approved students
[4] Exit
🛠️ Technologies Used
Python 3

JSON for data storage

os and pathlib for file and system operations

📥 How to Run
Make sure you have Python 3 installed.

Clone the repository:

bash
git clone https://github.com/your-username/your-repo-name.git
Navigate to the project folder:

bash
cd your-repo-name
Run the program:

bash
python main.py
📄 Requirements
This project was built to satisfy the following requirements:

Use a list named students

Each student must be a dictionary containing:

name

age

grade

Implement functions to:

add a student

list students

show approved students

Use if conditions to check approval

Consider approved students with grade ≥ 10

🎉 Future Improvements (Optional)
Edit or delete students

Search students by name

Export data to CSV

GUI version (Tkinter)

Web version (Flask)

📜 License
This project is open-source and free to use.
