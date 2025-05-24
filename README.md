# 🩺 CLI-Based Hospital Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-blue.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-rich%20|%20uv-orange)

Welcome to the **CLI-Based Hospital Management System (HMS)**, a powerful and modular command-line application built in Python to streamline hospital operations. Designed for small clinics and educational purposes, this system enables efficient management of patients, doctors, and appointments through a vibrant, user-friendly terminal interface. The menu is styled using the `rich` library for colorful and formatted display, ensuring an engaging user experience.

This project demonstrates professional software engineering practices, including **Object-Oriented Programming (OOP)**, **custom exception handling**, **JSON-based data persistence**, and **activity logging**, making it an excellent learning resource for developers and a practical tool for hospital management.

---

## 🌟 Key Features

- 🧬 **Object-Oriented Design**: Implements OOP principles (encapsulation, inheritance, polymorphism) in `hospital.py` for `Patient`, `Doctor`, and `Appointment` classes.
- 📝 **CRUD Operations**: Full Create, Read, Update, Delete functionality for patients, doctors, and appointments, managed in `manager.py` with JSON storage.
- 🎨 **Rich CLI Menu**: Uses the `rich` library to create a colorful and formatted menu in `main.py` for intuitive navigation.
- 🚨 **Custom Exception Handling**: Defines custom exceptions (`InvalidAgeError`, `InvalidDateError`, `InvalidGenderError`) in `exceptions.py` for robust input validation.
- 💾 **JSON Data Persistence**: Stores data in `patients.json`, `doctors.json`, and `appointments.json` for lightweight, portable storage.
- 🎨 **Custom Color Module**: Uses `color.py` for consistent ANSI color styling, especially for error messages.
- 📜 **Activity Logging**: Tracks operations and errors in `logs/hospital.log` using Python’s `logging` module.
- ⚡ **Dependency Management**: Utilizes `uv` for fast and reliable dependency installation.
- 🔒 **User-Friendly Prompts**: Intuitive input handling with clear error messages in `main.py`.

---

## 🛠 Technologies Used

| Technology       | Purpose                                      |
|------------------|----------------------------------------------|
| Python 3.10+     | Core programming language                    |
| Rich             | Colorful and formatted CLI menu              |
| JSON             | Lightweight data storage                     |
| Logging Module   | Activity and error logging                   |
| UV               | Dependency management                        |
| Custom Modules   | `hospital.py`, `manager.py`, `main.py`, `color.py`, `exceptions.py` |

---

## 📂 Project Structure

```
hospital_management_system/
├── main.py               # CLI menu, user inputs, and try-except error handling
├── hospital.py          # OOP classes (Patient, Doctor, Appointment) with OOP principles
├── manager.py           # CRUD operations and JSON data management
├── color/
│   └── color.py         # ANSI color codes for styling (e.g., error messages)
├── exceptions/
│   └── exceptions.py    # Custom exceptions (InvalidAgeError, InvalidDateError, InvalidGenderError)
│   └── main.py    # Custom error (validate_gender, validate_doctor_age, validate_patient_age, validate_date)
├── data/
│   ├── hospital-data.json    # hospital data storage
├── logs/
│   └── hospital.log          # Activity and error logs
├── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 📋 Prerequisites

- **Python**: Version 3.10 or higher
- **Git**: For cloning the repository
- **UV**: For dependency management (optional but recommended)
- **Virtual Environment**: To isolate dependencies
- **Terminal/CLI**: For running the application

### 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Muhammad-Fraooq/hospital_management_system.git
   cd hospital_management_system
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

---

## 🖥 Usage

Launch the application with `python main.py` to access an interactive CLI menu styled with `rich` for a colorful and engaging experience. Navigate using numeric inputs to manage hospital operations.

### Example Workflow

1. **Main Menu**:
   ```
   ==================================================
   ╔═ 🏥 Welcome to the Hospital Management System ═╗
   ║ 1. ➕ Add (Patient/Doctor)                     ║
   ║ 2. 📅 Book Appointment                         ║
   ║ 3. 📋 Show All Appointments                    ║
   ║ 4. 🔍 Search (Patient/Doctor)                  ║
   ║ 5. ⚙️  Settings (Patient/Doctor)                ║
   ║ 6. ❌ Cancel Appointment                       ║
   ║ 7. 🚪 Exit                                     ║
   ╚════════ Press a number to continue... ═════════╝
   ==================================================

   Enter your choice: 1
   ```

2. **Adding a Patient** (with custom error handling):
   ```
   Enter patient name: Alice Smith
   Enter patient age: 25
   Enter patient gender (M/F/O): F
   Enter patient condition: Asthma
   [SUCCESS] Patient Alice Smith added successfully!
   ```

   *Invalid Input Example*:
   ```
   Enter patient age: -5
   [ERROR] InvalidAgeError: Age cannot be negative.
   ```

3. **Checking Logs**:
   - View `logs/hospital.log` for detailed records of operations and errors.

---

## 🎯 Use Cases

- **Small Clinics**: Manage patient records, doctor schedules, and appointments efficiently in a lightweight CLI application.
- **Educational Tool**: Learn and practice:
  - Object-Oriented Programming (OOP) principles
  - Custom exception handling
  - JSON-based data persistence
  - CLI interface design with `rich` for menus
  - Modular code organization
- **Portfolio Project**: Showcase professional Python skills with real-world applicability.

---

## 🤝 Contributing

We welcome contributions to enhance the HMS! To contribute:

1. **Fork the repository**.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a **Pull Request** with a clear description.

Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

---

## 📬 Contact

Have questions or ideas? Let’s connect!

- 👨‍💻 **Name** : Muhammad Farooq
- 📧 **Email**: [Email](mailto:muhammad888xyz@gmail.com)
- 💼 **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/muhammad-farooq-developer/)
- 💻 **GitHub**: [GitHub](https://github.com/Muhammad-Fraooq)
- 🌐 **Portfolio**: [Muhammad Farooq](https://porfolio-milestone-2-pk.vercel.app/)

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

> 👨‍💻 *Crafted with passion by a GIAIC student on the journey to becoming a world-class Agentic AI Engineer.*