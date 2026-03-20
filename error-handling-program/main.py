STUDENTS_ID = {
  21016112910: "MOHIT SINGH",
  21016112911: "RAJ GUPTA",
  21016112912: "ROHAN SHARMA",
  21016112913: "ABHI TYAGI",
  21016112914: "SOHIT SHARMA",
  21016112915: "PRIYANSHU RAWAT",
  21016112916: "KANISHQ YADAV",
  21016112917: "ASHI DIXIT",
  21016112918: "AYUSH SINGH",
  21016112919: "KHUSHI PANDEY",
  21016112920: "SHUBHAM SHARMA",
}

try:
    for i in range(10):
        i = int(input("Enter your student id: "))
    
        if i in STUDENTS_ID:
            print(f"Name: {STUDENTS_ID[i]} | Roll Number: {i}")
        else:
            print("Student ID not found")
    
except ValueError:
    print("Invalid input! Please enter a number.")
