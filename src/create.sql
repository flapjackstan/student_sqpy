CREATE TABLE Student (  StudentId  INTEGER UNIQUE PRIMARY KEY,
                        FirstName VARCHAR(32),
                        LastName VARCHAR (32),
                        GPA REAL, --float
                        Major VARCHAR (16),
                        FacultyAdvisor VARCHAR(32),
                        isDeleted BOOLEAN);
/*
INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted)
VALUES ('elmer', 'camargo', '3.4', 'data', 'mac', '0');*/

INSERT INTO Student (StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted)
VALUES ('328093','elmer', 'camargo', '3.4', 'data', 'mac', '0');

DELETE FROM Student WHERE FirstName = 'elmer'