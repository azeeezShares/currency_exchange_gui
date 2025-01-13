import tkinter


# oyna yaratish
root = tkinter.Tk()

# oynani sozlash
root.geometry("490x400")
root.title("salom dunyo")
root.configure(background="blue")

tkinter.Label(root, text="Hello world", foreground="yellow").grid(column=0, row=0)
tkinter.Label(root, text="Hello world", foreground="yellow", bg="green").grid(column=1, row=1)
tkinter.Button(root, text="Meni bos", ).grid(column=0, row=2)

tkinter.mainloop()