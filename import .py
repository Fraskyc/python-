import tkinter as tk

class Quiz(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.num_correct = 0
        self.question_num = 1

    def create_widgets(self):
        self.question_label = tk.Label(self, text="1. Jaké je hlavní město Francie?")
        self.question_label.pack()
        
        self.answer_var = tk.StringVar()
        self.answer_var.set("A")
        
        self.answer_a = tk.Radiobutton(self, text="A) Řím", variable=self.answer_var, value="A")
        self.answer_a.pack()
        
        self.answer_b = tk.Radiobutton(self, text="B) Londýn", variable=self.answer_var, value="B")
        self.answer_b.pack()
        
        self.answer_c = tk.Radiobutton(self, text="C) Berlín", variable=self.answer_var, value="C")
        self.answer_c.pack()
        
        self.answer_d = tk.Radiobutton(self, text="D) Paříž", variable=self.answer_var, value="D")
        self.answer_d.pack()
        
        self.check_button = tk.Button(self, text="Zkontrolovat", command=self.check_answer)
        self.check_button.pack()

    def check_answer(self):
        answer = self.answer_var.get()
        if answer == "D":
            self.num_correct += 1
            print("1. otázka je správně!")
        else:
            print("1. otázka je spatně!")
            
        self.question_num += 1
        if self.question_num == 2:
            self.question_label.config(text="2. Jaký je největší oceán na světě?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Tichý oceán")
            self.answer_b.config(text="B) Atlantický oceán")
            self.answer_c.config(text="C) Indický oceán")
            self.answer_d.config(text="D) Jižní oceán")
            self.check_button.config(command=self.check_answer2)
        elif self.question_num == 3:
            self.question_label.config(text="3. Jaká je Chorvatská měna?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Kuna")
            self.answer_b.config(text="B) Euro")
            self.answer_c.config(text="C) Dolar")
            self.answer_d.config(text="D) Yen")
            self.check_button.config(command=self.check_answer3)
        elif self.question_num == 4:
            self.question_label.config(text="4. Kdo napsal knihu  Harry Potter?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Stephenie Meyer")
            self.answer_b.config(text="B) J.K. Rowling")
            self.answer_c.config(text="C) Suzanne Collins")
            self.answer_d.config(text="D) Veronica Roth")
            self.check_button.config(command=self.check_answer4)
        elif self.question_num == 5:
            self.question_label.config(text="5. Který kontinent je největší?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Afrika")
            self.answer_b.config(text="B) Severní Amerika")
            self.answer_c.config(text="C) Asia")
            self.answer_d.config(text="D) Evropa")
            self.check_button.config(command=self.check_answer5)
        else:
            self.show_results()
        
    def check_answer2(self):
        answer = self.answer_var.get()
        if answer == "A":
            self.num_correct += 1
            print("2. otázka je správně!")
        else:
            print("2. otázka je spatně!")
            
        self.question_num += 1
        if self.question_num == 3:
            self.question_label.config(text="3. Jaká je Chorvatská měna?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Kuna")
            self.answer_b.config(text="B) Euro")
            self.answer_c.config(text="C) Dolar")
            self.answer_d.config(text="D) Yen")
            self.check_button.config(command=self.check_answer3)
        elif self.question_num == 4:
            self.question_label.config(text="4. Kdo napsal knihu  Harry Potter?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Stephenie Meyer")
            self.answer_b.config(text="B) J.K. Rowling")
            self.answer_c.config(text="C) Suzanne Collins")
            self.answer_d.config(text="D) Veronica Roth")
            self.check_button.config(command=self.check_answer4)
            self.check_button.config(command=self.check_answer4)
        elif self.question_num == 5:
            self.question_label.config(text="5. Který kontinent je největší?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Afrika")
            self.answer_b.config(text="B) Severní Amerika")
            self.answer_c.config(text="C) Asia")
            self.answer_d.config(text="D) Evropa")
            self.check_button.config(command=self.check_answer5)
        else:
            self.show_results()
        
    def check_answer3(self):
        answer = self.answer_var.get()
        if answer == "B":
            self.num_correct += 1
            print("3. otázka je správně!")
        else:
            print("3. otázka je spatně!")
            
        self.question_num += 1
        if self.question_num == 4:
            self.question_label.config(text="4. Kdo napsal knihu  Harry Potter?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Stephenie Meyer")
            self.answer_b.config(text="B) J.K. Rowling")
            self.answer_c.config(text="C) Suzanne Collins")
            self.answer_d.config(text="D) Veronica Roth")
            self.check_button.config(command=self.check_answer4)
        elif self.question_num == 5:
            self.question_label.config(text="5. Který kontinent je největší?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Afrika")
            self.answer_b.config(text="B) Severní Amerika")
            self.answer_c.config(text="C) Asia")
            self.answer_d.config(text="D) Evropa")
            self.check_button.config(command=self.check_answer5)
        else:
            self.show_results()
    
    def check_answer4(self):
        answer = self.answer_var.get()
        if answer == "B":
            self.num_correct += 1
            print("4. otázka je správně!")
        else:
            print("4. otázka je spatně!")
            
        self.question_num += 1
        if self.question_num == 5:
            self.question_label.config(text="5. Který kontinent je největší?")
            self.answer_var.set("A")
            self.answer_a.config(text="A) Afrika")
            self.answer_b.config(text="B) Severní Amerika")
            self.answer_c.config(text="C) Asia")
            self.answer_d.config(text="D) Evropa")
            self.check_button.config(command=self.check_answer5)
        else:
            self.show_results()
    def check_answer5(self):
        answer = self.answer_var.get()
        if answer == "C":
            self.num_correct += 1
            print("5. otázka je správně!")
        else:
            print("5. otázka je spatně!")
            
        self.show_results()
    
    def show_results(self):
        self.question_label.config(text=f"Odpověděl jsi {self.num_correct} z 5 otázek správně!")
        self.answer_a.config(state="Vyplý")
        self.answer_b.config(state="Vyplý")
        self.answer_c.config(state="Vyplý")
        self.answer_d.config(state="Vyplý")
        self.check_button.config(state="")
        self.quit_button = tk.Button(self.question_frame, text="Opustit", font=("Arial", 12), command=self.quit)
        self.quit_button.pack(pady=10)
    
root = tk.Tk()
app = Quiz(master=root)
app.mainloop()
   

