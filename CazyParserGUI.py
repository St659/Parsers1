import tkinter
from tkinter import ttk
from CAZYParser import get_fasta
from threading import Thread


def parse_input(event):
    progress_bar.grid(row=3, column=0, columnspan=2)
    progress_bar.start()
    filename = fileEntry.get() + ".fasta"
    #t = Thread(target=get_fasta, args=(urlEntry.get(), fileEntry.get()))
    #t.start()
    #window.after(1000, check_thread, t)


def check_thread(thread):
    if thread.is_alive():
        window.after(1000, check_thread, thread)
    else:
        progress_bar.stop()


window = tkinter.Tk()

progress_bar = ttk.Progressbar(mode ='indeterminate')
urlEntry = tkinter.Entry(window)
fileEntry = tkinter.Entry(window)
parseButton = tkinter.Button(window, text = "Parser")
parseButton.bind("<Button-1>", parse_input)

urlLabel = tkinter.Label(window, text="URL")
fileLabel = tkinter.Label(window, text="Filename")

urlLabel.grid(row = 0, column = 0)
urlEntry.grid(row = 0, column = 1)
fileLabel.grid(row = 1, column = 0)
fileEntry.grid(row = 1, column = 1)

parseButton.grid(row = 2, column = 0, columnspan = 2)


window.mainloop()