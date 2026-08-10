# Student Manager

A simple Python project for managing student records.

This project was developed as part of my Python programming practice and focuses on **Object-Oriented Programming (OOP)**, **CSV file handling**, and basic **CRUD operations**.

---

## 📌 Project Overview

The **Student Manager** allows users to manage a collection of students.

Each student contains:

* Name
* Student ID
* Major

The project provides functionality for adding, removing, searching, editing, displaying, and counting students.

---

## ✨ Features

* Add a new student
* Prevent duplicate Student IDs
* Remove a student by Student ID
* Search for a student
* Edit student information
* Display all students
* Show the total number of students
* Save student data to a CSV file
* Load existing student data from a CSV file

---

## 🏗️ Project Structure

The project consists of two main classes:

### `Student`

Represents an individual student.

Attributes:

* `name`
* `student_ID`
* `major`

The `__str__()` method is used to display student information in a readable format.

### `StudentManager`

Manages the collection of students and provides the main operations:

* `add_student()`
* `remove_student()`
* `show_students()`
* `search_student()`
* `edit_student()`
* `statistics()`
* `save_student()`
* `load_students()`

---

## 💾 Data Storage

Student records are stored in a CSV file:

```text
studentmanager.csv
```

The CSV file contains the following fields:

```text
name
student_ID
major
```

The program automatically saves the student list after adding, editing, or removing a student.

Existing records are loaded when `load_students()` is called.

---

## 🧠 Concepts Practiced

This project was designed to practice:

* Classes and objects
* Object-Oriented Programming
* Class methods
* Lists of objects
* Searching through objects
* Updating object attributes
* Input validation
* Duplicate checking
* CSV file handling
* `csv.DictReader`
* `csv.DictWriter`
* Reading and writing persistent data
* Basic CRUD operations

---

## 🎯 Learning Purpose

The main purpose of this project was to move beyond basic Python syntax and practice designing a small management system using classes and persistent data storage.

It also provided practice working with a collection of objects and connecting that collection to a CSV-based storage system.

---

## 🚀 Possible Future Improvements

Potential improvements for a future version include:

* Adding a user-friendly command-line menu
* Validating Student IDs and other inputs
* Handling empty student lists more explicitly
* Returning success/failure messages from manager methods
* Adding more student-related information
* Improving the search and filtering functionality
* Using a more consistent CRUD design
* Adding automated tests

---

## 🛠️ Technologies

* Python
* Object-Oriented Programming
* CSV

---

## 📚 Project Series

This project is part of my ongoing Python programming practice, where each project gradually introduces new programming concepts and more structured software design.

--

##Author

**Mahsa Rousta**