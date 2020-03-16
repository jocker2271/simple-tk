import requests
import tkinter as tk
import tkinter.ttk

YA_TOKEN = 'trnsl.1.1.20200316T062349Z.8488dcd6e088d8e3.f9d3009e90048a1e5f6398e28d7d52bda74aa126'
REQUEST = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'

def translate_en_ru():
    text = en_text.get(1.0, tk.END)
    r = requests.get(REQUEST.format(YA_TOKEN, text, 'en-ru'))
    print(r.json['text'][0])

window = tk.Tk()
window.geometry('580x300')
window.resizable(False,False)

tk.Button(window, text='Translate!', command=translate_en_ru).pack(side=tk.BOTTOM)
notebook = tkinter.ttk.Notebook(window)
notebook.pack(fill=tk.BOTH)

en_frame = tk.Frame(window)
ru_frame = tk.Frame(window)
en_text = tk.Text(en_frame)
ru_text = tk.Text(ru_frame)

en_frame.pack()
ru_frame.pack()
en_text.pack()
ru_text.pack()

notebook.add(en_frame, text='English')
notebook.add(ru_frame, text='Russian')

window.mainloop()