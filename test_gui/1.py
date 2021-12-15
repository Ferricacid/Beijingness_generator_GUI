# Beijingness Generator
# 2021 Dec 10 Lucy Wu
# Reference: https://github.com/VirtualOilCake/Beijingese-Generator

import PySimpleGUI as sg

sg.theme('DarkAmber') 
layout = [  [sg.Text('北京话生成器')],
            [sg.Text('输入你的话'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('北儿京儿话儿生儿成儿器儿', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   
        break
    text_processed = values[0]
    new = ''
    for i in text_processed:
        if i == "你":
            new += "您儿"
        elif i in "~!@#$%^&*()_+=- `?><,./;':}{][""，。？！·、》《“”；‘：}{】【|——）（*&……%￥#@~":
            new += i
        elif i >= 'A' and i <= 'z':
            new += i+'r'
        else:
            new += i+"儿"
    sg.popup_scrolled(new)

window.close()