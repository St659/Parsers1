import tkinter

window = tkinter.Tk()

urlEntry = tkinter.Entry(window)
parseButton = tkinter.Button(window, text = "Parser")

urlEntry.pack()
parseButton.pack()

window.mainloop()