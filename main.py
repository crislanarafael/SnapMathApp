# Python Snap Math Application for Stanford University's Code In Place 2021 final project
# Developer: Crislana R. Date: May 25, 2021
# A tool to help students practice and master basic math skills with the help of Snap Math App's mascot, Sam the Sea Otter

from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image
import random
 #mainwin = Tk ()
 #mainwin.mainloo

#frame setup
root = Tk()
root.iconbitmap(r'C:\Users\crisl\OneDrive\Desktop\Code In Place Stanford\favicon_io\favicon.ico')
f = Frame(root, width = 500, height = 500, borderwidth = 10, bg="#ffde59")
f.pack_propagate(0) #forces the frame dimensions in line 13
f.configure(background='#ffde59')
my_img = ImageTk.PhotoImage(Image.open("seaotter.png"))
my_img2 = ImageTk.PhotoImage(Image.open("instructor_otter.png"))
my_img3 = ImageTk.PhotoImage(Image.open("end_otter.png"))

f.pack()

r = IntVar()
r.get()

#Introductory Text for Title Screen
intro_text1 = "Welcome to the Snap Math Application."
intro_text2 = "Improve your basic math skills and mental arithmetic in a snap (get it?)!"
intro_text3 = "I'm Sam the Sea Otter here to make your learning Otterly delightful!"

#math program global variables
global total_score
total_score = 0
type_of_arithmetic = ""
global number_questions
user_selected_questions = ""
user_selected_questions_label_text = StringVar()
current_question_display = StringVar()
question_content_display = StringVar()
result_display = StringVar()
global current_question
current_question = IntVar()
global question_loop
question_loop = 0
global number1
global number2
operations_list = ["+", "-", "*", "/"]
user_input = 0
global answer
answer = 0
global answer_is_correct
answer_is_correct = True

def main_window(main):
    main.iconbitmap(r'C:\Users\crisl\OneDrive\Desktop\Code In Place Stanford\favicon_io\favicon.ico') #set favicon
    main.title("Snap Math App")
    main.geometry("500x500") #sets main window size

def clear_title_frame():
    #for events
    """hello = "Hello"
    myLabel = Label(root, text=hello)
    myLabel.pack()"""
    for widgets in f.winfo_children():
        widgets.destroy()
    math_instructions()

def clear_instructions_frame():
    for widgets in f.winfo_children():
        widgets.destroy()
    math_setup()

def clear_setup_frame():
    for widgets in f.winfo_children():
        widgets.destroy()
    current_question.set(0)
    run_program()

def clear_frame():
    for widgets in f.winfo_children():
        widgets.destroy()

def enter_and_evaluate(value, type_of_arithmetic):
    #this function stores the user's answer and updates user's total score
    global total_score
    global answer_is_correct
    global answer

    if type_of_arithmetic == '+':
        answer = number1 + number2
    if type_of_arithmetic == '-':
        answer = number1 - number2
    if type_of_arithmetic == '*':
        answer = number1 * number2
    if type_of_arithmetic == '/':
        answer = int(round(number1 / number2))
    user_input = int(value) #value from the text field is a string and we convert it to an int
    if user_input == answer:
        total_score += 1
        messagebox.showinfo('SnapMathApp Feedback', 'You got the correct answer!')
    else:
        messagebox.showinfo('SnapMathApp Feedback', 'So close, the answer is ' + str(answer))
    print(answer)
    print(total_score)
    #print(operations_list[random.randint(0,3)])


def clear_question():
    clear_frame()
    if question_loop != number_questions:
        next_question()
    else:
        end_screen()

def end_screen():
    global total_score
    global number_questions
    result_display.set("Your score is: " + str(total_score) + " out of " + str(number_questions))

    end_frame = Frame(f, width=500, height=500)
    end_frame.configure(background='#ffde59')
    end_frame.pack_propagate(0)
    end_frame.pack()

    end_heading1 = Label(end_frame, text="Congratulations!", font="Arial 30 bold", bg = '#ffde59')
    end_heading1.pack()

    end_heading2 = Label(end_frame, text="You got to the very end! But the journey of learning never ends and there's always new things to learn. So keep learning, keep practicing, and don't give up because you are PAW-some!", wraplength = 450, justify = LEFT, font="Helvetica 13", bg='#ffde59')
    end_heading2.pack(fill = 'both')

    end_heading3 = Label(end_frame, textvariable = result_display, font="Arial 15", bg='#ffde59')
    end_heading3.pack()

    end_img = Label(end_frame, image=my_img3, bg="#ffde59")
    end_img.pack(fill="both")

    exit_program_button = Button(end_frame, text="Exit Program", font="Helvetica", command=root.quit)
    exit_program_button.pack()

def next_question():
    global question_loop
    global number_questions
    if question_loop <= number_questions:
        run_program()

def run_program():
    #initialize
    answer_text = ""
    current_answer = False
    global question_loop
    question_loop += 1
    global current_question
    global answer_is_correct
    current_question.set(current_question.get()+1)
    #frame within a frame - inception style
    question_frame = Frame(f, width=400, height=400, borderwidth=10, bg="#ffde59")
    question_frame.configure(background='#add8e6')
    question_frame.pack_propagate(0)
    question_frame.pack()

    #randomize operations
    type_of_arithmetic = operations_list[random.randint(0, 3)] #selects a random index from operations_list
    global number1
    global number2
    number1 = random.randint(1,1000)
    number2 = random.randint(1,1000)

    #starts with question 1
    current_question_display.set("Question " + str(current_question.get()))
    setup_heading = Label(question_frame, textvariable=current_question_display, font="Arial 20 bold")
    setup_heading.pack()

    blankspace1 = Label(question_frame, text="", font="Helvetica 15 bold", bg="#add8e6", anchor='w', justify=LEFT)
    blankspace1.pack(fill='both')

    #question_content_display.set("What is " + number1.get + operation + number2 + " ?")
    question_content = Label(question_frame, text= "What is " + str(number1) + " " + type_of_arithmetic + " " + str(number2) + " = ?",font="Arial 20 bold")
    question_content.pack()

    blankspace2 = Label(question_frame, text="", font="Helvetica 15 bold", bg="#add8e6", anchor='w', justify=LEFT)
    blankspace2.pack(fill='both')

    answer_label = Label(question_frame, text="Enter answer in textfield below. If you have a division question enter your answer to the nearest integer. ", wraplength = 380,font="Helvetica 11")
    answer_label.pack()

    blankspace3 = Label(question_frame, text="", font="Helvetica 15 bold", bg="#add8e6", anchor='w', justify=LEFT)
    blankspace3.pack(fill='both')

    input_text = Text(question_frame, height = 1, width = 15)
    input_text.pack()

    blankspace4 = Label(question_frame, text="", font="Helvetica 15 bold", bg="#add8e6", anchor='w', justify=LEFT)
    blankspace4.pack(fill='both')

    enter_Button = Button(question_frame, text="Enter Answer", command=lambda: enter_and_evaluate(input_text.get("1.0", END), type_of_arithmetic), font="Helvetica")
    enter_Button.pack()

    #added message box to alert user if they got the question correct or not
    blankspace5 = Label(f, text="", font="Helvetica 15 bold", bg="#ffde59", anchor='w', justify=LEFT)
    blankspace5.pack(fill='both')

    end_setup_Button = Button(f, text="Next Question >>>", command=clear_question, font="Helvetica")
    end_setup_Button.pack()

def num_questions_selected(value):
    #answer_label = Label(f, text=value)
    #answer_label.pack()
    if (r.get() == 4):
        user_selected_questions_label_text.set("You have selected 4 questions")
    if (r.get() == 8):
        user_selected_questions_label_text.set("You have selected 8 questions")
    if (r.get() == 16):
        user_selected_questions_label_text.set("You have selected 16 questions")
    global number_questions
    number_questions = value
    #print(number_questions)

def math_setup():
    #screen allowing the user to select the number of questions
    setup_heading = Label(f, text="Snap Math Setup", font="Arial 20 bold", bg="#ffde59")
    setup_heading.pack()

    setup_question_label = Label(f, text="Select the number of questions to solve:", font="Helvetica 15 bold", bg="#ffde59", anchor='w', justify=LEFT)
    setup_question_label.pack(fill = 'both')

    question_option1 = Radiobutton(f, text = "4 Questions", variable=r, value = 4, bg="#ffde59", anchor='w', font="Helvetica 15", command = lambda: num_questions_selected(r.get()))
    question_option1.pack(fill = 'both')

    question_option2 = Radiobutton(f, text="8 Questions", variable=r, value=8, bg="#ffde59", anchor='w', font="Helvetica 15", command = lambda: num_questions_selected(r.get()))
    question_option2.pack(fill='both')

    question_option2 = Radiobutton(f, text="16 Questions", variable=r, value=16, bg="#ffde59", anchor='w',font="Helvetica 15", command=lambda: num_questions_selected(r.get()))
    question_option2.pack(fill='both')

    user_answer_label = Label(f, textvariable=user_selected_questions_label_text, font="Helvetica 15 bold", bg="#ffde59", anchor='w', justify=LEFT)
    user_answer_label.pack(fill = 'both')

    blankspace1 = Label(f, text="", font="Helvetica 15 bold", bg="#ffde59", anchor='w', justify=LEFT)
    blankspace1.pack(fill='both')

    end_setup_Button = Button(f, text="I'm Ready!", command=clear_setup_frame, font="Helvetica")
    end_setup_Button.pack()

    blankspace2 = Label(f, text="", font="Helvetica 15 bold", bg="#ffde59", anchor='w', justify=LEFT)
    blankspace2.pack(fill='both')

    #put at the bottom
    instructions1 = Label(f, text="Developer's Note: I'm planning to add extra setup features such as a modifiable number of questions, question types, question breakdowns in the future", font="Helvetica 11", bg="#ffde59", anchor='w', wraplength=490, justify=LEFT)
    instructions1.pack(fill='both')

def math_instructions():
    main_title = Label(f, text="Instructions: ", font="Arial 20 bold", bg="#ffde59")
    main_title.pack()

    instructions_img = Label(f, image=my_img2, bg="#ffde59")
    instructions_img.pack(fill="both")

    instructions1 = Label(f, text="• Work out the given math problems WITHOUT a computer.", font="Helvetica 11", bg="#ffde59", anchor='w', wraplength = 500, justify = LEFT)
    instructions1.pack(fill = 'both')

    instructions2 = Label(f,text="• Read the question carefully and double check your final answer.", font="Helvetica 11", bg="#ffde59", anchor='w', wraplength=500, justify=LEFT)
    instructions2.pack(fill = 'both')

    instructions3 = Label(f, text="• Enter the answer in the text field and click the SUBMIT button to submit your answer.", font="Helvetica 11", bg="#ffde59", anchor='w', wraplength=500, justify=LEFT)
    instructions3.pack(fill = 'both')

    instructions5 = Label(f, text="• Have fun! (Sam says: 'I'll be over here sleeping in the water')", font="Helvetica 11", bg="#ffde59",anchor='w', wraplength=500, justify=LEFT)
    instructions5.pack(fill='both')

    blank_space= Label(f, text = "", bg="#ffde59")
    blank_space.pack()
    instructions_Button = Button(f, text="I'm Ready!", command=clear_instructions_frame, font="Helvetica")
    instructions_Button.pack()


def main_content():
    main_title = Label(f, text="Snap Math App", font="Arial 30 bold",bg="#ffde59")
    main_title.config(anchor=CENTER)
    main_title.pack()

    main_img_label = Label(f, image = my_img, bg="#ffde59")
    main_img_label.pack()

    main_heading1 = Label(f, text=intro_text1, font="Helvetica 10", bg="#ffde59")
    main_heading1.pack()

    main_heading2 = Label(f, text=intro_text2, font="Helvetica 10", bg="#ffde59")
    main_heading2.pack()

    main_heading3 = Label(f, text=intro_text3, font="Helvetica 10", bg="#ffde59")
    main_heading3.pack()

    main_heading3 = Label(f, text="", bg="#ffde59")
    main_heading3.pack()

    main_Button = Button(f, text="Let's Begin", command=clear_title_frame, font="Helvetica")
    main_Button.pack()

main_window(root)
main_content()
mainloop()





