# CodeAlpha File Automation 📂

## 📌 Project Overview
This project is a simple file automation program developed using Python as part of the CodeAlpha Python Programming Internship.

The program automatically identifies image files with JPG, JPEG, and PNG extensions and moves them into a separate folder named `JPG_Files`.

## ✨ Features
- Automatically detects image files in the project folder.
- Supports JPG, JPEG, and PNG file formats.
- Creates a destination folder automatically if it does not exist.
- Moves the selected image files into the destination folder.
- Displays a success message for each moved file.

## 🛠️ Technologies Used
- Python 3
- Visual Studio Code

## 📚 Python Concepts Used
- `os` module
- `shutil` module
- File and folder handling
- Conditional statements
- Loops
- Path management

## 📂 Project Structure

```text
CodeAlpha_FileAutomation/
│
├── file_automation.py
├── README.md
└── JPG_Files/
    └── (moved image files)
```

## ▶️ How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code.
4. Place sample JPG, JPEG, or PNG images in the same folder as `file_automation.py`.
5. Open the terminal and run:

```bash
python file_automation.py
```

If the command does not work, try:

```bash
py file_automation.py
```

## 💻 Expected Output

```text
flower.png moved successfully!
All JPG files have been moved!
```

The exact filenames displayed will depend on the images placed in the folder.

## 🎯 Learning Outcome
This project helped me understand file handling, directory management, Python modules, and automating repetitive file management tasks.

## 👩‍💻 Author
Ayushree 

## 🎓 Internship
CodeAlpha - Python Programming Internship