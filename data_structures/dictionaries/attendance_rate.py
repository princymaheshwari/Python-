# Attendance Rate
# Write a function attendance_rate() that takes in a dictionary attendance_list as a parameter. The function maps student names to their attendance status ("Present" or "Absent"), and returns the percentage of students who are present.

def attendance_rate(attendance_list):

    no_of_people_present = sum(1 for status in attendance_list.values() if status == "Present")
    return (no_of_people_present/len(attendance_list))*100

    
attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
    
}

print(attendance_rate(attendance_list))
