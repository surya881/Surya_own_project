import tkinter as tk
from tkinter import messagebox

class KBCGame:
    def __init__(self):
        self.question_index = 0
        self.score = 0
        self.time_remaining=180

        self.questions = [
            {
                "question": "Which is the capital city of India?",
                "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
                "answer": 1
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["Yuan", "Yen", "Rupee", "Euro"],
                "answer": 1
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
                "answer": 0
            },
            {
                "question": "Question 4",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": 2
            },
            {
                "question": "Question 5",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": 3
            }
        ]

        self.window = tk.Tk()
        self.window.title("KBC Game")
        self.window.geometry("400x400")

        self.question_label = tk.Label(self.window, text="Question",font=("Helvetica",16, "bold"), wraplength=380)
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(pady=10)

        self.next_button = tk.Button(self.window, text="Next", command=self.next_question,font=("Helvetica", 12, "bold"), bg="green", fg="white")
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(self.window, text="Score: 0",font=("Helvetica", 14))
        self.score_label.pack()

        self.timer_label = tk.Label(self.window, text="Time Remaining: 30:00",font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.show_question()
        self.update_timer()

        self.window.mainloop()

    def show_question(self):
        question = self.questions[self.question_index]

        self.question_label.configure(text=question["question"])

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        self.selected_option = tk.IntVar() 

        for i, option in enumerate(question["options"]):
            radio_button = tk.Radiobutton(self.options_frame, text=option, variable=self.selected_option, value=i,font=("Helvetica", 12))
            radio_button.pack()

    def check_answer(self):
        question = self.questions[self.question_index]
        selected_option = self.selected_option.get()

        if selected_option == question["answer"]:
            self.score += 1
            self.score_label.configure(text="Score: {}".format(self.score))
            return True
        else:
            messagebox.showinfo("Wrong Answer", "You selected the wrong option.\nFinal score: {}".format(self.score))
            self.window.destroy()
            return False

    def next_question(self):
        if self.selected_option.get() == -1:
            messagebox.showerror("Error", "Please select an option!")
            return

        is_correct = self.check_answer()

        if is_correct:
            self.question_index += 1

        if self.question_index < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Game Over", "Quiz completed!\nFinal score: {}".format(self.score))
            self.window.destroy()

    def update_timer(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.timer_label.configure(text="Time Remaining: {:02d}:{:02d}".format(minutes, seconds))

        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.window.after(1000, self.update_timer)

KBCGame()