import tkinter
from tkinter import ttk

def main():
    opcion = None
    def reiniciar():
        window.destroy()
        main()

    window = tkinter.Tk()

    frame = ttk.Frame(window, padding= 30)
    frame.grid()

    ttk.Checkbutton(frame).grid(column=0, row=0)
    ttk.Label(frame, padding=10, text="Opción 1").grid(column=1, row=0)

    ttk.Checkbutton(frame).grid(column=0, row=1)
    ttk.Label(frame, padding=10, text="Opción 2").grid(column=1, row=1)

    ttk.Checkbutton(frame).grid(column=0, row=2)
    ttk.Label(frame, padding=10, text="Opción 3").grid(column=1, row=2)

    window.mainloop()

if __name__ == '__main__':
    main()