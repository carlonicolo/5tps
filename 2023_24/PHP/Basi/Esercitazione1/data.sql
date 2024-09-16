----------- Creazione database esempio phpmyadmin ---------------

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




-- SELECT * FROM courses, students, studentcourses where courses.CourseID = studentcourses.CourseID AND studentcourses.StudentID = students.StudentID

-- JOIN example

SELECT Students.Name AS NomeStudente, Students.Email as Email, Courses.CourseName as NomeCorso, Courses.Teacher as Prof
FROM StudentCourses
JOIN Students ON StudentCourses.StudentID = Students.StudentID
JOIN Courses ON StudentCourses.CourseID = Courses.CourseID;


---------------------------