import expenseTracker
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.state("zoomed")
root.update_idletasks()
root.title("CashTrack - Expense Tracker")

bg_image = Image.open("background.png")
bg_image = bg_image.resize((width,height))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")

expense_file_path = "expenses.csv"
fixedBudget = tk.DoubleVar()
expAmt = tk.DoubleVar()
expName = tk.StringVar()

def set_budget():
    set_budget_window = tk.Toplevel(root)
    center_window(set_budget_window)
    set_budget_window.geometry("300x200")
    set_budget_window.title("Set Budget")
    budget_entry = tk.Entry(set_budget_window, textvariable = fixedBudget)
    budget_entry.bind("<Return>", lambda event: submit_budget())
    budget_entry.pack()
    submit_btn = tk.Button(set_budget_window, text="Submit", command=submit_budget)
    submit_btn.pack()

def submit_budget():
    budget = fixedBudget.get()
    expenseTracker.budget = float(budget)


def submit_expense(expense_input_window, cat_choice):
    expense_name = expName.get()
    expense_amount = float(expAmt.get())
    expense = expenseTracker.get_user_expense(expense_name, expense_amount, cat_choice)
    expenseTracker.save_expense_to_file(expense, expense_file_path)
    saving_label = tk.Label(expense_input_window, text="Expense saved successfully!", fg="green")
    saving_label.pack()
    expense_input_window.after(2000, expense_input_window.destroy)


def expenseInput(button):
    expense_input_window = tk.Toplevel(root)
    center_window(expense_input_window)
    expense_input_window.geometry("300x200")
    expense_input_window.title("Enter expense details")

    cat_choice = button.cget("text")

    name_label = tk.Label(expense_input_window, text="Expense Name:")
    name_label.pack(pady=10)
    name_entry = tk.Entry(expense_input_window, textvariable = expName)
    name_entry.pack()

    amt_label = tk.Label(expense_input_window, text="Expense Amount:")
    amt_label.pack(pady=10)
    amt_entry = tk.Entry(expense_input_window, textvariable = expAmt)
    amt_entry.pack()
    submit_expense_btn = tk.Button(expense_input_window, text="Submit", command=lambda: submit_expense(expense_input_window, cat_choice))
    submit_expense_btn.pack(pady=15)


#Budget button
budget_btn = tk.Button(root, text="Fix budget for the month", command=set_budget)
budget_btn.pack(pady=20)

#Category buttons
food_btn = tk.Button(root, text="Food", command=lambda: expenseInput(food_btn))
food_btn.pack(padx = 40, pady=10, side=tk.LEFT)

utility_btn = tk.Button(root, text="Utility", command=lambda: expenseInput(utility_btn))
utility_btn.pack(padx = 40, pady=10, side=tk.LEFT)

transport_btn = tk.Button(root, text="Transport", command=lambda: expenseInput(transport_btn))
transport_btn.pack(padx = 40, pady=10, side=tk.LEFT)

entertainment_btn = tk.Button(root, text="Entertainment", command=lambda: expenseInput(entertainment_btn))
entertainment_btn.pack(padx = 40, pady=10, side=tk.LEFT)

misc_btn = tk.Button(root, text="Miscellaneous", command=lambda: expenseInput(misc_btn))
misc_btn.pack(padx = 40, pady=10, side=tk.LEFT)

#Keeps window running until user closes it
root.mainloop()
'''
#Read file and summarize expenses
summarize_expenses(expense_file_path, budget)
'''