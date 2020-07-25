import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = 'label1')
label2 = tkinter.Label(main_window, text = 'label2')

tombol1 = tkinter.Button(main_window, text = "Button1")
tombol2 = tkinter.Button(main_window, text = "Button2")

#method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#method show GUI
main_window.mainloop()