import tkinter as tk
from tkinter import messagebox

class C0deW1zardGUI:
    def __init__(self):
        self.username = ""
        self.chat_visible = False
        self.dark_mode = False

        self.window = tk.Tk()
        self.window.title("C0de W1zard")

        self.welcome_label = tk.Label(self.window, text="Welcome to C0de W1zard!")
        self.welcome_label.pack(pady=10)

        self.username_label = tk.Label(self.window, text="Enter your username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window, width=50)
        self.username_entry.pack(padx=10, pady=5)
        self.username_entry.bind("<Return>", self.start_chat)

        self.start_chat_button = tk.Button(self.window, text="Press Enter", command=self.start_chat)
        self.start_chat_button.pack(pady=5)

        self.conversation_text = tk.Text(self.window, height=10, width=50)
        self.conversation_text.pack(padx=10, pady=5)
        self.conversation_text.configure(state="disabled")

        self.user_input_entry = tk.Entry(self.window, width=50)
        self.user_input_entry.pack(padx=10, pady=5)
        self.user_input_entry.insert(tk.END, "Press Enter to Send")
        self.user_input_entry.bind("<Return>", self.send_message)
        self.user_input_entry.configure(state="disabled")
        self.user_input_entry.bind("<FocusIn>", self.clear_entry_field)

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=5)

        self.dark_mode_button = tk.Button(self.button_frame, text="Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(side="left")

        self.quit_button = tk.Button(self.button_frame, text="Quit Program", command=self.quit_program)
        self.quit_button.pack(side="left")

        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

        self.window.mainloop()

    def start_chat(self, event=None):
        self.username = self.username_entry.get()

        if self.username != "":
            self.username_label.pack_forget()
            self.username_entry.pack_forget()
            self.start_chat_button.pack_forget()


            welcome_message = f"Welcome, {self.username}! Start chatting with C0de W1zard."
            self.conversation_text.configure(state="normal")
            self.conversation_text.insert(tk.END, welcome_message + "\n")
            self.conversation_text.configure(state="disabled")

            self.chat_visible = True
            self.user_input_entry.configure(state="normal")

    def send_message(self, event=None):
        if self.chat_visible:
            user_input = self.user_input_entry.get()

            self.user_input_entry.delete(0, tk.END)


            self.conversation_text.configure(state="normal")
            self.conversation_text.insert(tk.END, f"{self.username}: {user_input}\n")
            self.conversation_text.configure(state="disabled")

            bot_response = self.get_response(user_input)


            self.conversation_text.configure(state="normal")
            self.conversation_text.insert(tk.END, "C0de W1zard: " + bot_response + "\n")
            self.conversation_text.configure(state="disabled")

            self.conversation_text.see(tk.END)

    def get_response(self, user_input):

        questions = [
            "hello",
            "What is Python?",
            "What are the main features of object-oriented programming?",
            "How do you define a function in Python?",
            "What is the difference between list and tuple in Python?",
            "What is the purpose of 'if __name__ == '__main__':' in Python?",
        ]
        answers = [
            f"Hey {self.username}, How can I help you?",
            "Python is a high-level programming language known for its simplicity and readability.",
            "The main features of object-oriented programming include encapsulation, inheritance, and polymorphism.",
            "In Python, you can define a function using the 'def' keyword followed by the function name and parameters.",
            "A list is mutable, meaning you can change its elements, while a tuple is immutable.",
            "The 'if __name__ == '__main__':' condition is used to check if the current module is being run as the main program.",
        ]

        for i in range(len(questions)):
            if questions[i].lower() in user_input.lower():

                return answers[i]

        return f"I'm sorry {self.username}, I don't have an answer for that question."

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.window.config(bg="black")
            self.conversation_text.config(bg="black", fg="white")
        else:
            self.window.config(bg="white")
            self.conversation_text.config(bg="white", fg="black")

    def quit_program(self):
        confirm = messagebox.askyesno("Quit", "Are you sure you want to quit?")

        if confirm:
            self.window.destroy()

    def close_window(self):
        self.quit_program()

    def clear_entry_field(self, event=None):
        if self.user_input_entry.get() == "Press Enter to Send":
            self.user_input_entry.delete(0, tk.END)

chatbot_gui = C0deW1zardGUI()
