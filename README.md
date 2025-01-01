# Face Recognition Attendance Management System

This project is developed for **CSE 3200 (Software Development Project II)** under the supervision of **[Mahit Kumar Paul](https://www.ruet.ac.bd/mahitcse)**, Assistant Professor, Department of Computer Science & Engineering, Rajshahi University of Engineering & Technology (RUET).

### Project Overview

The Face Recognition Attendance Management System utilizes **Python** and **OpenCV** to automate attendance marking based on facial recognition. The system employs the **Haarcascade Algorithm** for face detection and the **Local Binary Pattern Histogram (LBPH)** for face recognition. 

The main functionalities of the system are as follows:
1. **Student Registration**: Student details (name, roll number, department) are collected and stored in a **MySQL database**.
2. **Image Capturing**: Images for registered students are captured and saved in a local directory.
3. **Model Training**: The model is trained using the captured images for accurate facial recognition.
4. **Attendance Marking**: When a student’s face is recognized, their name, roll number, and department are displayed, and their attendance is recorded in a `.csv` file.

### Installation

To run this system, ensure you have the necessary dependencies installed:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AudityGhosh/Face_Recognition_Attendance_Management_System.git
    ```

2. **Install the required Python packages**:

    ```bash
    pip install opencv-python numpy mysql-connector-python
    ```

3. **Set up the MySQL database**:
   - Create a database to store student information.
   - Ensure that your MySQL server is running.

### File Descriptions

- **attendance.py**: Handles the attendance logic, records attendance in a `.csv` file.
- **developer.py**: Contains the backend logic for student data management.
- **face_recognition.py**: Implements the face recognition algorithm using LBPH.
- **haarcascade_frontalface_default.xml**: Haarcascade algorithm used for face detection.
- **help.py**: A helper script for supporting various system operations.
- **main.py**: The main driver script to start the system.
- **student.py**: Manages student information and registration.

### How to Use

1. **Register Students**: 
   - Run `developer.py` to add student details into the database.
   - Capture student images using `student.py` and store them in the local directory.

2. **Run the Face Recognition**:
   - Execute `main.py` to launch the system and start recognizing faces.
   - When a student's face is detected, their information is displayed, and their attendance is recorded.

3. **Attendance Report**: 
   - The attendance is recorded in a `.csv` file where each student’s attendance is updated with each recognition.

### License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

### Acknowledgements

- **Instructor**: [Mahit Kumar Paul](https://www.ruet.ac.bd/mahitcse), Assistant Professor, RUET
- **Libraries Used**: OpenCV, MySQL, Numpy
- **Face Detection Algorithm**: Haarcascade
- **Face Recognition Algorithm**: Local Binary Pattern Histogram (LBPH)
