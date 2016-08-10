#-*- coding: utf-8 -*-
from tkinter import *
from comp_databutton import databutton_list, databutton_values
from comp_datasort import datasort_list, datasort_map

window = Tk()

name = Label(window, text = "이름 : ")
name.grid(row = 0, column = 0)
name_row = Frame(window)
name_row.grid(row = 0, column = 1, sticky = N)
display_name = Entry(name_row, width = 45, bg = "light green")
display_name.grid()

score = Label(window, text = "점수 : ")
score.grid(row = 0, column = 2)
score_row = Frame(window)
score_row.grid(row = 0, column = 3, sticky = N)
display_score = Entry(score_row, width = 45, bg = "light green")
display_score.grid()

number = Label(window, text = "번호 : ")
number.grid(row = 1, column = 2)
number_row = Frame(window)
number_row.grid(row = 1, column = 3, sticky = N)
display_number = Entry(number_row, width = 45, bg = "light green")
display_number.grid()

filename1 = Label(window, text = "파일이름 : ")
filename1.grid(row = 2, column = 2)
filename1_row = Frame(window)
filename1_row.grid(row = 2, column = 3,sticky = N)
display_filename1 = Entry(filename1_row, width = 45, bg = "light blue")
display_filename1.grid()

filename2 = Label(window, text = "파일이름 : ")
filename2.grid(row = 3, column = 2)
filename2_row = Frame(window)
filename2_row.grid(row = 3, column = 3, sticky = N)
display_filename2 = Entry(filename2_row, width = 45, bg = "light blue")
display_filename2.grid()

databutton_row = Frame(window)
databutton_row.grid(row  = 0, column = 4, rowspan = 4, sticky = E)

datasort_row = Frame(window)
datasort_row.grid(row = 4, column = 0, columnspan = 4, sticky = W)

button_groups = {
    'databutton':{'list':databutton_list, 'window':databutton_row, 'width':10, 'cols':1},
    'datasort':{'list':datasort_list, 'window':datasort_row, 'width':20, 'cols':4},
}

insertnumber = 1
dataoutput_dic_number = {}
dataoutput_dic_name = {}
dataoutput_dic_score = {}
dataoutput_dic_nametemp = [0]
dataoutput_dic_scoretemp = [0]

def isnumber_float(x):
    try:
        float(x)
        return False;
    except ValueError:
        return True;
def isnumber_int(x):
    try:
        int(x)
        return False;
    except ValueError:
        return True;

def click(key):
    global insertnumber
    global dataoutput_dic_number
    global dataoutput_dic_name
    global dataoutput_dic_score
    global dataoutput_dic_temp

    display_current.delete(0, END)

    if key in databutton_list:
        if key == '추가':
            if(str(display_name.get()) in dataoutput_dic_name):
                display_current.insert(END, '[추가 실패] 동일한 이름이 이미 존재합니다.')
            elif(str(display_name.get()) == ""):
                display_current.insert(END, '[추가 실패] 이름이 공란입니다.')
            elif(isnumber_float(display_score.get())):
                display_current.insert(END, '[추가 실패] 점수가 올바른 형태가 아닙니다.')
            else:
                dataoutput_dic_number[str(insertnumber)] = str(str(insertnumber) + '\t' + str(display_name.get()) + '\t' + str(display_score.get()) + '\n')
                dataoutput_dic_name[str(display_name.get())] = str(str(insertnumber) + '\t' + str(display_name.get()) + '\t' + str(display_score.get()) + '\n')
                dataoutput_dic_score[str(display_score.get())] = str(str(insertnumber) + '\t' + str(display_name.get()) + '\t' + str(display_score.get()) + '\n')
                dataoutput_dic_nametemp.append(display_name.get())
                dataoutput_dic_scoretemp.append(display_score.get())

                display_dataoutput.insert(END, dataoutput_dic_number[str(insertnumber)])
                insertnumber = insertnumber + 1
                display_current.insert(END, '성공적으로 추가하였습니다.')
            display_name.delete(0, END)
            display_score.delete(0, END)
        elif key == '삭제':
            if(isnumber_int(display_number.get())):
                display_current.insert(END, '[삭제 실패] 번호가 올바른 형태가 아닙니다.')
            elif(str(display_number.get()) in dataoutput_dic_number):
                del dataoutput_dic_number[display_number.get()]
                del dataoutput_dic_name[dataoutput_dic_nametemp[int(display_number.get())]]
                del dataoutput_dic_score[dataoutput_dic_scoretemp[int(display_number.get())]]

                display_current.insert(END, '성공적으로 삭제하였습니다.')
                display_dataoutput.delete("0.0", "end")
                temp = list(dataoutput_dic_number.keys())
                temp.sort()
                for i in temp:
                    display_dataoutput.insert(END, dataoutput_dic_number[i])
            else:
                display_current.insert(END, '[삭제 실패] 존재하지 않는 번호를 입력했습니다.')
            display_number.delete(0, END)
        elif key == '저장':
            f = open(str(display_filename1.get()) + str('.txt'), 'w')
            for i in dataoutput_dic_number.keys():
                f.write(dataoutput_dic_number[i])
            f.close()
            display_current.insert(END, str('성공적으로 저장하였습니다. (파일이름 : ') + str(display_filename1.get()) + str(' )'))
            display_filename1.delete(0, END)
        elif key == '열기':
            display_dataoutput.delete("0.0", "end")
            try:
                f = open(str(display_filename2.get()) + str('.txt'), 'r')
                while True:
                    line = f.readline()
                    if not line: break
                    display_dataoutput.insert(END, line)
                f.close()
                display_current.insert(END, str('성공적으로 파일을 읽었습니다. (파일이름 : ') + str(display_filename2.get()) + str(' )'))
            except FileNotFoundError:
                display_current.insert(END, '[열기 실패] 파일이 존재하지 않습니다.')
            display_filename2.delete(0, END)
    elif key in datasort_list:
        if key == '번호순':
            display_dataoutput.delete("0.0", "end")
            temp = list(dataoutput_dic_number.keys())
            temp.sort()
            for i in temp:
                display_dataoutput.insert(END, dataoutput_dic_number[i])
        elif key == '이름순':
            display_dataoutput.delete("0.0", "end")
            temp = list(dataoutput_dic_name.keys())
            temp.sort()
            for i in temp:
                display_dataoutput.insert(END, dataoutput_dic_name[i])
        elif key == '점수내림차순':
            display_dataoutput.delete("0.0", "end")
            temp = list(dataoutput_dic_score.keys())
            temp.sort()
            temp.reverse()
            for i in temp:
                display_dataoutput.insert(END, dataoutput_dic_score[i])
        elif key == '점수오름차순':
            display_dataoutput.delete("0.0", "end")
            temp = list(dataoutput_dic_score.keys())
            temp.sort()
            for i in temp:
                display_dataoutput.insert(END, dataoutput_dic_score[i])


for label in button_groups.keys():
    r = 0
    c = 0
    buttons = button_groups[label]
    for btn_text in buttons['list']:
        def cmd(x = btn_text):
            click(x)
        Button(buttons['window'], text = btn_text, width = buttons['width'], command = cmd).grid(row = r, column = c)
        c = c + 1
        if c >= buttons['cols']:
            c = 0
            r = r + 1


dataoutput_row = Frame(window)
dataoutput_row.grid(row = 5, column = 0, columnspan = 4, sticky = W)
display_dataoutput = Text(dataoutput_row, width = 120, bg = "light yellow")
display_dataoutput.grid()

current_messageoutput_row = Frame(window)
current_messageoutput_row.grid(row = 6, column = 0, columnspan = 4, sticky = W)
display_current = Entry(current_messageoutput_row, width = 120, bg = "pink")
display_current.grid()

window.mainloop()
