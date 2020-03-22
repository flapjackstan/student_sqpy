import string


class Student:
    def __init__(self, first, last, gpa, major, advisor):
        self.first = first.lower()
        self.last = last.lower()
        self.gpa = float(gpa)
        self.major = major.lower()
        self.advisor = advisor.lower()
        self.isDeleted = 0

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def getGPA(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def getAdvisor(self):
        return self.advisor

    def getDeleted(self):
        return self.isDeleted

    def getStudent(self):
        return (self.getFirst(), self.getLast(),self.getGPA(), self.getMajor(), self.getAdvisor(), self.getDeleted())