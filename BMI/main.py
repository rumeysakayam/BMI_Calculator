from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.config(bg="white")
window.config(padx=30, pady=30)
window.minsize(250, 250)

#get weight
w_label = Label(window, text="Enter your weight: (kg)", fg="black", bg="white")
w_label.pack()

w_entry = Entry(width=15, bg="white", fg="black")
w_entry.pack()

#get height
h_label = Label(window, text="Enter your height: (cm)", fg="black", bg="white")
h_label.pack()

h_entry = Entry(width=15, bg="white", fg="black")
h_entry.pack()

#button
def bmi_calculator():
    user_weight = w_entry.get()
    user_height = h_entry.get()
    try:
        user_bmi = int(user_weight) / (int(user_height) / 100) ** 2
        bmi_level = bmi_class(user_bmi)
        bmi_label = Label(window, text=f"Your BMI is {round(user_bmi, 2)} and you are {bmi_level} ")
        bmi_label.pack()
    except ValueError:
        error_message = Label(text="Please enter valid values")
        error_message.pack()


calculate_button = Button(text="Calculate", command=bmi_calculator)
calculate_button.pack()


#bmi_class
def bmi_class(user_bmi):
    if user_bmi <= 18.5:
        return "Underweight"
    elif 18.5 < user_bmi <= 25:
        return "Normal"
    elif 25 < user_bmi <= 30:
        return "Overweight"
    elif user_bmi > 30:
        return "Obese"


window.mainloop()