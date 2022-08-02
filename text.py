from tkinter import *
from tkinter import messagebox

def extract_data():
    print(text_box.get('1.0', 'end'))


ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#84BF04')


message ='''
You are invited to a Birthday Party

venue: Az Resort
Timing: 7 pm, wednesday

Please visit with family.

Regards,
James


'''

text_box = Text(
    ws,
    height=13,
    width=40,
    wrap='word'
)
text_box.pack(expand=True)
text_box.insert('end', message)

Button(
    ws,
    text='Change Text',
    command=extract_data
).pack(expand=True)

ws.mainloop()