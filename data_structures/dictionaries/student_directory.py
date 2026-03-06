# Student Directory
# Write a function student_directory() that takes a list of student_names as a parameter and returns a dictionary of students, where each student in student_names is a key mapped to a unique numerical ;' ID.

def student_directory(student_names):
    
    return {name: i for i, name in enumerate(student_names, start = 1)}
    
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
student_directory(student_names)
