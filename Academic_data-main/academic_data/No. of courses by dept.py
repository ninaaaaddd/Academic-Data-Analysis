import os
from pathlib import WindowsPath
import matplotlib.pyplot as plt
from typing import Union
def get_no_of_students(path_of_excel_for_course:Union[str,WindowsPath]):
    import pandas as pd
    df=pd.read_csv(path_of_excel_for_course)
    no_of_students=df.shape[0]
    return no_of_students

def plot_graph(filt):
    plt.xlabel="Course"
    plt.ylabel="No. of students"
    plt.bar(filt.keys(),filt.values())
    plt.show()


def student_in_dept_by_course(dept:str):
    no_of_students_by_course={}
    branch_path=os.path.join(cwd,dept)
    for i in os.listdir(branch_path):
        if(i.endswith(".csv")):
            print(i)
            no_of_students_by_course[str(i)[0:6]]=get_no_of_students(os.path.join(branch_path,i))
    return no_of_students_by_course


# Get the current working directory
cwd = r"C:\Users\Ninad\OneDrive\Desktop\Academic_dataProject\Academic_data-main\academic_data\Year_2021\2022-2023 Autumn"
print(cwd)
no_of_dept=len(os.listdir(cwd))
print(no_of_dept)
print(os.listdir(cwd))
no_of_courses_by_dept={}
for i in os.listdir(cwd):
    no_of_courses_by_dept["{}".format(i)]=len(os.listdir(os.path.join(cwd,i)))

no_of_students_by_course={}
dept=os.listdir(cwd)[0]
branch_path=os.path.join(cwd,dept)
for i in os.listdir(branch_path):
    if(i.endswith(".csv")):
        print(i)
        no_of_students_by_course[str(i)[0:6]]=get_no_of_students(os.path.join(branch_path,i))
plot_graph(no_of_students_by_course)
req_info=student_in_dept_by_course("Computer Science")
# plot_graph(req_info)
plt.xlabel="Course"
plt.ylabel="No. of students"
plt.bar(req_info.keys(),req_info.values())
plt.show()