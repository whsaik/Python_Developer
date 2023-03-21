from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # create label to display score
        self.label = Label(
            text=f"Score: {self.quiz.score}", 
            font=("Arial", 15, "italic"), 
            fg='white', 
            bg=THEME_COLOR
            )
        self.label.grid(row=0, column=1)
        
        # create canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Question", 
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        # creates buttons
        correct_img = PhotoImage(file=r"quizzler-app\images\true.png")
        wrong_img = PhotoImage(file=r"quizzler-app\images\false.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0, border=0, command=self.correct)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)
        
        self.canvas_next_question()
        
        self.window.mainloop()
        
    def canvas_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, 
                                   text=f"You've completed the quiz\n"
                                   f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        
    def correct(self):
        self.give_feedback(self.quiz.check_answer(user_answer='True'))
        
    def wrong(self):
        self.give_feedback(self.quiz.check_answer(user_answer='False')) 
            
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.canvas_next_question)