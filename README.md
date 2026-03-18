# 🏥 Health-Clinic Queue Manager

A web-based application built with **Flask** to manage patient registrations and waiting lists.

## 🏗️ Project Architecture
This project follows a modular structure to separate logic from presentation:
- **`app.py`**: The Controller (Flask routes and Queue logic).
- **`model.py`**: The Data Model (Patient OOP class).
- **`templates/`**: The View (HTML/CSS User Interface).

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Framework**: Flask
- **API**: Python Datetime
- **Data Structure**: List-based FIFO Queue
## 📋 Data Structure: FIFO Queue
The core of this application is a **First-In, First-Out (FIFO)** queue. In a medical clinic, it is essential to treat patients in the order they arrive. We implement this using:
- `append()` to add patients to the end of the list.
- `pop(0)` to remove the patient at the front of the list for treatment.
## 🧬 Object-Oriented Programming (OOP)
The `Patient` class in `model.py` demonstrates key OOP principles:
- **Encapsulation**: Attributes like `name`, `ailment`, and `arrival_time` are bundled within the object.
- **Behavior**: Methods like `get_summary()` and `is_urgent()` provide logic specific to the data.
## ⚙️ Installation & Setup
1. Ensure Python 3 is installed on your computer.
2. Install the Flask framework: `pip install flask`
3. Run the application: `python app.py`
4. Open your browser to `http://127.0.0.1:5000`.
## 🖥️ User Interface Features
- **Dashboard**: View the current waiting list in real-time.
- **Registration**: A simple form to input patient data.
- **Admin Control**: A "Reset System" feature to clear the queue.
- **Design**: Used CSS to make the app easy to read.
## 🔮 Future Enhancements
- Connect to a database to save patient history forever.
- Add a "Priority" button for emergency cases.
- Add a search bar to find specific patients in the queue.
---
**Course**: CSC 202 - Building for the Web  
**Submission Date**: March 20th, 2026  
**Project Status**: Complete and ready for grading.
