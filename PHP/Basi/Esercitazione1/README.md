# Prima esercitazione PHP

## Forms, sessions and database

### Task 1

Creare "a mano" un database composto da tre tabelle:  

```sql
CREATE DATABASE SchoolDB;

USE SchoolDB;

CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(100),
    Teacher VARCHAR(100)
);

CREATE TABLE StudentCourses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

```

### Task 2  

Creare 2 o 3 pagine PHP con delle form nelle quali inserire i dati da salvare nel database.  

### Task 3  

Creare una pagina dove poter visualizzare tutti i corsi presenti nel database.  
