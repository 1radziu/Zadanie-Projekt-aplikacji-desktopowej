import tkinter as tk
from tkinter import ttk
class Aplikacja:
    def __init__(self,okno):
        self.tekst1 = tk.StringVar()
        self.tekst2 = tk.StringVar()
        lista1 = tk.StringVar()

        self.label0 = tk.Label(okno, text='Podaj dane: ', background='#76EEC6', font = ('Arial', 12, 'italic'))
        self.label0.grid(row=0, column= 0)
        self.label01 = tk.Label(okno, text='Podaj Imię: ', background='#76EEC6')
        self.label01.grid(row=1, column=0)

        self.entry01 = tk.Entry(okno, textvariable=self.tekst1, font=('Arial',8,'italic'))
        self.entry01.grid(row=1, column=1)

        # self.b1 = tk.Button(okno, text='Podaj dane', background='#5795e6',command=lambda: self.zmien_tekst(self.label03, self.tekst1, 'Cześć '))
        # self.b1.grid(row=16,column=18) 

        self.label02 = tk.Label(okno, text='Podaj Nazwisko: ', background='#76EEC6')
        self.label02.grid(row=2,column=0)

        self.entry02 = tk.Entry(okno, textvariable=self.tekst2, font=('Arial',8,'italic'))
        self.entry02.grid(row=2,column=1)

        self.label03 = tk.Label(okno, text='Twój ulubiony język programowania: ', background='#76EEC6')
        self.label03.grid(row=3,column=0)

   
        self.label04 = tk.Checkbutton(okno, text='Java', background='#76EEC6')
        self.label04.grid(row=4, column= 0)
        self.label05 = tk.Checkbutton(okno, text='JavaScript', background='#76EEC6')
        self.label05.grid(row=5, column= 0)
        self.label06 = tk.Checkbutton(okno, text='Python', background = '#76EEC6')
        self.label06.grid(row=6, column= 0)        

        self.label07 = tk.Label(okno, text='Województwo: ', background='#76EEC6' )
        self.label07.grid(row=7, column=0)



    
    

        

        # self.b1 = tk.Button(okno, text='Podaj klasę', background='#5795e6', command=lambda: self.zmien_tekst(self.label04, self.tekst2, 'Jesteś z klasy '))
        # self.b1.grid(row=17, column=18)

        # self.label03 = tk.Label(okno, text='Cześć', background='#77aaed')
        # self.label03.grid(row=18, column=17)

        # self.label04 = tk.Label(okno, text='Jesteś z klasy',background='#77aaed')
        # self.label04.grid(row=19, column=17)

    # def zmien_tekst(self,label,textvar,text):
    #     label.config(text=(str(text) + str(textvar.get())))

okno = tk.Tk()
okno.title('ZSEiT')
okno.configure(background=('#76EEC6'))
okno.geometry('1280x960')
okno.resizable(False, False)
app = Aplikacja(okno)
okno.mainloop()       