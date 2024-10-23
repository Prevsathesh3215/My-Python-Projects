from tkinter import *
import questions

data = questions.Questions()
INITIAL_TEXT = 'Choose your trivia genre:'


class QuizInterface:
    def __init__(self):
        self.__score = 0
        self.__count = 0
        self.__qna = []

        self.__root = Tk()
        self.__root.title('API Quizzler')
        self.__root.minsize(400, 600)
        self.__root.config(background='#55ACD3')

        right_img = PhotoImage(file="true.png")
        wrong_img = PhotoImage(file="false.png")
        self.__right_button = Button(image=right_img, border=1, activebackground='#55ACD3',
                                   command=lambda: self.check_ans('True'))
        self.__wrong_button = Button(image=wrong_img, border=1, activebackground='#55ACD3',
                                   command=lambda: self.check_ans('False'))

        self.__canvas = Canvas()
        self.__canvas.place(height=400, x=8.5, y=80)
        self.__text = self.__canvas.create_text(190, 70, text=INITIAL_TEXT,
                                                font=('Times New Roman', 15),
                                                justify='center', width=200)

        self.genre_choice()

        self.__root.mainloop()

    def genre_choice(self):

        self.__films = Button(text='Entertainment: Films', height=2,
                       padx= 8, relief=GROOVE,
                       command=lambda: [data.send_category(11), self.destroy_all_buttons()])

        self.__music = Button(text='Entertainment: Music', height=2,
                       padx= 8, relief=GROOVE,
                       command=lambda: [data.send_category(12), self.destroy_all_buttons()])

        self.__video_games = Button(text='Entertainment: Video Games', height=2,
                             padx= 8, relief=GROOVE,
                             command=lambda: [data.send_category(15), self.destroy_all_buttons()])

        self.__maths = Button(text='Science: Mathematics', height=2,
                       padx= 8, relief=GROOVE,
                       command=lambda: [data.send_category(19), self.destroy_all_buttons()])


        self.__films.place(x=130, y=190)
        self.__music.place(x=130, y=250)
        self.__video_games.place(x=110, y=310)
        self.__maths.place(x=130, y=370)


    def destroy_all_buttons(self):

        self.__root.after(10, lambda: [self.__films.destroy(),
                                       self.__music.destroy(), self.__video_games.destroy(),
                                       self.__maths.destroy()])

        self.__canvas.delete('all')

        self.start_questions()

    def start_questions(self):

        self.__qna = data.obtain_questions()
        self.__text = self.__canvas.create_text(190, 200, text=self.__qna[self.__count]['question'],
                                                font=('Times New Roman', 20),
                                                justify='center', width=200)

        self.__label = Label(text=f"Score= {self.__score}", font=('Arial', 12, 'bold'), bg='#55ACD3',
                             fg='white')
        self.__label.place(x=300, y=40)


        self.__right_button.place(x=30, y=485)
        self.__wrong_button.place(x=265, y=485)



    def check_ans(self, flag):

        player_ans = flag
        actual_answer = self.__qna[self.__count]['answer']

        if player_ans == actual_answer and self.__count != 9:
            self.__canvas.configure(bg='green')
            self.__score += 1
        else:
            self.__canvas.configure(bg='red')

        self.__label.config(text=f"Score= {self.__score}")

        self.__canvas.after(1000, self.next_question)

    def next_question(self):

        self.__canvas.configure(bg='white')
        if self.__count == 9:
            self.__canvas.itemconfig(self.__text, text=f'Your score: {self.__score}')

            exit_button = Button(text='Exit', command=self.__root.destroy,
                                 width= 10, height= 2)
            exit_button.place(x=170, y=370)

        else:
            self.__count += 1
            self.__canvas.itemconfig(self.__text, text=self.__qna[self.__count]['question'])








