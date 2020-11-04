import random

def create_outline():
    #Step1
    course_topics = {"Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code", "Functions", "Modules", "How to structure data"}
    course_list = list(course_topics)
    sorted_list = sorted(course_list)
    print("Course Topics:")
    for i in range(0, len(sorted_list)):
        print("* ", end="")
        print(sorted_list[i])

    #Step2
    problems = ["Problem 1", "Problem 2", "Problem 3"]
    course_dict = {}
    print("Problems:")
    for j in course_list:
        course_dict[j] = problems
    for key, value in course_dict.items():
        print("*", key,": ", end="")
        print(*value, sep=", ")

    #Step3
    grades = ("STARTED","GRADED", "COMPLETED")
    print("Student Progress:")
    Student1 = ("1. ","Nyari", "Introduction to Python", "Problem 2",grades[0])
    Student2 = ("2. ","Adam", "How to make decisions","Problem 1",grades[1])
    Student3 = ("3. ","Kayden", "Tools of the Trade","Problem 3",grades[2])
    progress = [Student1, Student2, Student3]
    progress.sort(key=lambda i: i[4], reverse=True)
    for num, name, topic, problem, grade in progress:
        print("{} {} - {} - {} [{}]".format(num, name, topic, problem, grade))
    pass
    #Step4
    

if __name__ == "__main__":
    create_outline()
