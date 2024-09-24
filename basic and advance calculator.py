#imported Moudles

import tkinter as tk
from tkinter import *
import pyautogui as gui

#calculator selection

select_cal = gui.confirm(text = 'Select the Calculator' , title = 'Calculator' , buttons = ['Simple Calculator' , 'Advance Calculator'])

#Advance Calculator with TKinter

if select_cal == 'Advance Calculator':

    calculation = ''

    #built in functions

    def add_to_calculatiuon(symbol):
        global calculation 
        calculation += str(symbol)
        text_result.delete(1.0,'end')
        text_result.insert(1.0 , calculation)


    def eval_calculation():
        global calculation
        try:
            result = str(eval(calculation))
            calculation = ''
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, result)
        except:
            clear_text_result()
            text_result.insert(1.0 ,'Error')

    def clear_text_result():
        global calculation
        calculation = ''
        text_result.delete(1.0 ,'end')

    #Window size and colors

    window = tk.Tk()
    window.geometry('370x580')
    window.title('Advance Calculator')
    window.resizable(False,False)
    window.configure(bg='#dbdbe2')

    text_result = tk.Text(window ,height=2 , width =12 , font=('arial' , 40))
    text_result.pack()

    #Buttons and operations

    btn_clear =Button(window , text='C' , width=3 , height=1 , font=('arial', 30),fg='#ffffff', bg='#ff9900' , command=clear_text_result).place(x=10 , y=130)
    btn_mod =Button(window , text='%' , width=3 , height=1 , font=('arial', 30),fg='#ffffff',bg='#0066ff' , command= lambda: add_to_calculatiuon('%')).place(x=100 , y=130)
    btn_mul =Button(window , text='x' , width=3 , height=1 , font=('arial', 30) ,fg='#ffffff',bg='#0066ff', command= lambda: add_to_calculatiuon('*')).place(x=190 , y=130)
    btn_pow =Button(window , text='^' , width=3 , height=1 , font=('arial', 30),fg='#ffffff',bg='#0066ff', command= lambda: add_to_calculatiuon('**')).place(x=280 , y=130)

    btn_7 =Button(window , text='7' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(7)).place(x=10 , y=220)
    btn_8 =Button(window , text='8' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(8)).place(x=100 , y=220)
    btn_9 =Button(window , text='9' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(8)).place(x=190 , y=220)
    btn_div =Button(window , text='÷' , width=3 , height=1 , font=('arial', 30),fg='#ffffff',bg='#0066ff', command= lambda: add_to_calculatiuon('/')).place(x=280 , y=220)

    btn_4 =Button(window , text='4' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(4)).place(x=10 , y=310)
    btn_5 =Button(window , text='5' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(5)).place(x=100 , y=310)
    btn_6 =Button(window , text='6' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(6)).place(x=190 , y=310)
    btn_sub =Button(window , text='-' , width=3 , height=1 , font=('arial', 30),fg='#ffffff',bg='#0066ff', command= lambda: add_to_calculatiuon('-')).place(x=280 , y=310)

    btn_1 =Button(window , text='1' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(1)).place(x=10 , y=400)
    btn_2 =Button(window , text='2' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(2)).place(x=100 , y=400)
    btn_3 =Button(window , text='3' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(3)).place(x=190 , y=400)
    btn_add =Button(window , text='+' , width=3 , height=1 , font=('arial', 30),fg='#ffffff',bg='#0066ff', command= lambda: add_to_calculatiuon('+')).place(x=280 , y=400)

    btn_0 =Button(window , text='0' , width=7 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon(0)).place(x=10 , y=490)
    btn_dot =Button(window , text='.' , width=3 , height=1 , font=('arial', 30), command= lambda: add_to_calculatiuon('*(0.1)')).place(x=190 , y=490)
    btn_equl =Button(window , text='=' , width=3 , height=1 , font=('arial', 30),fg='#ffffff',bg='#0066ff', command=eval_calculation).place(x=280 , y=490)




    window.mainloop()


elif select_cal == 'Simple Calculator':
    
    #Number Inputs
    
    x = float(gui.prompt( text = 'Enter your number' , title = 'Fisrt Number'))
    operator = gui.confirm( text = 'Choose The Operator' , title = 'Operator' , buttons = ['+' , '-' , '*' , '/' , '**' , '%'] )
    y = float(gui.prompt( text = 'Enter your number' , title = 'Second Number'))

    #user builted function
    def Addition():
        gui.alert(text =(x + y) , title = 'Answer')

    def Subtraction():
        gui.alert((x - y) , title = 'Answer')

    def Multiplication():
        gui.alert((x * y) , title = 'Answer')

    def Divison():
        gui.alert((x / y) , title = 'Answer')

    def  Power():
        gui.alert((x ** y) , title = 'Answer')

    def modularDivision():
        gui.alert((x % y) , title = 'Answer')

    #if condition for operator

    if operator == '+':
        Addition()
    elif operator == '-':
        Subtraction()
    elif operator == '*':
        Multiplication()
    elif operator == '/':
        Divison()
    elif operator == '**':
        Power()
    elif operator == '%':
        modularDivision()