from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkcalendar import DateEntry  # Import DateEntry widget from tkcalendar
import pymysql
from connection import connect

class messages:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.root = Toplevel()
        self.root.title("Leave Application")
        self.root['background'] = '#FFFFFF'

        self.font = ("Arial", 20, "bold")
        self.conn = connect()
        self.cr = self.conn.cursor()

        # Colors
        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#0D2601"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        self.mainLabel = Label(self.root, text="Send Message", font=('Arial', 24, 'bold'), bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.leaveForm = Frame(self.root, bg=self.bg_color)
        self.leaveForm.pack()

        self.lb1 = Label(self.leaveForm, text="Employee ID", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, pady=10, padx=20)

        self.t1 = Entry(self.leaveForm, font=self.font, width=30)
        self.t1.grid(row=0, column=1, pady=10, padx=20)
        self.t1.insert(END, self.employee_id)
        self.t1.configure(state='readonly')

        self.lb2 = Label(self.leaveForm, text="Title", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, pady=10, padx=20)

        self.t2 = Entry(self.leaveForm, font=self.font, width=30)
        self.t2.grid(row=1, column=1, pady=10, padx=20)

        self.lb3 = Label(self.leaveForm, text="Date", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, pady=10, padx=20)

        # # Replace Entry with DateEntry for calendar date selection
        # self.t3 = DateEntry(self.leaveForm, font=self.font, width=30, background='darkblue', foreground='white', borderwidth=2)
        # self.t3.grid(row=2, column=1, pady=10, padx=20)

        # Replace Entry with DateEntry for calendar date selection
        self.t3 = DateEntry(self.leaveForm, font=self.font, width=30, background='darkblue', foreground='white',
                            borderwidth=2, date_pattern='Y-m-d')
        self.t3.grid(row=2, column=1, pady=10, padx=20)

        self.lb4 = Label(self.leaveForm, text="Description", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb4.grid(row=3, column=0, pady=10, padx=20)
        # Replace Entry with Text for larger text box
        self.t4 = Text(self.leaveForm, font=self.font, width=30, height=5)
        self.t4.grid(row=3, column=1, pady=10, padx=20)

        # Label for Time
        self.lb5 = Label(self.leaveForm, text="Time", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb5.grid(row=4, column=0, pady=10, padx=20)

        # Entry for selecting time
        self.t5 = ttk.Combobox(self.leaveForm, font=self.font, width=30)
        self.t5['values'] = (
        '09:00 AM', '09:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM', '12:30 PM', '01:00 PM',
        '01:30 PM', '02:00 PM', '02:30 PM', '03:00 PM', '03:30 PM', '04:00 PM', '04:30 PM', '05:00 PM', '05:30 PM',
        '06:00 PM', '06:30 PM', '07:00 PM', '07:30 PM', '08:00 PM', '08:30 PM', '09:00 PM')
        self.t5.grid(row=4, column=1, pady=10, padx=20)

        self.submitButton = Button(self.root, text="Submit", width=15, font=self.font, command=self.submitmessage, bg=self.button_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.submitButton.pack(pady=20)

        # Bind hover effects to the submit button
        self.submitButton.bind("<Enter>", self.on_enter)
        self.submitButton.bind("<Leave>", self.on_leave)

        self.root.mainloop()


    # def submitmessage(self):
    #     emp_id = self.t1.get()
    #     date = self.t2.get()
    #     remarks = self.t3.get("1.0", "end-1c")  # Get text from Text widget
    #
    #     try:
    #         # Insert leave information into the database table
    #         sql_insert_message = "INSERT INTO messages (emp_id_B, title, date, description,time) VALUES (%s, %s, %s, %s, %s)"
    #         self.cr.execute(sql_insert_message, (emp_id_B, title, date, description,time))
    #         self.conn.commit()
    #         msg.showinfo("Leave Application", "Leave submitted successfully.")
    #     except Exception as e:
    #         self.conn.rollback()
    #         msg.showerror("Error", f"An error occurred: {e}")

    def submitmessage(self):
        emp_id = self.t1.get()
        title = self.t2.get()
        date = self.t3.get()
        description = self.t4.get("1.0", "end-1c")  # Get text from Text widget
        time = self.t5.get()

        try:
            # Insert message information into the database table
            sql_insert_message = "INSERT INTO messages (emp_id_B, title, date, description, time) VALUES (%s, %s, %s, %s, %s)"
            self.cr.execute(sql_insert_message, (emp_id, title, date, description, time))
            self.conn.commit()
            msg.showinfo("Message Sent", "Message submitted successfully.")
        except Exception as e:
            self.conn.rollback()
            msg.showerror("Error", f"An error occurred: {e}")

    def on_enter(self, event):
        # Change background color when mouse enters button
        self.submitButton.config(bg=self.button_hover_color)

    def on_leave(self, event):
        # Restore background color when mouse leaves button
        self.submitButton.config(bg=self.button_color)

if __name__ == "__main__":
    messages = messages()

