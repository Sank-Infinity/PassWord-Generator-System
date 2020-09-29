import random
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Password Generator')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter Level of Password (1, 2, 3, Alpha)')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def generatePass():
    x1 = entry1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "*~_@#$%^&!"

    try:
        if x1 == '1':
            all = lower
            length = 6
            password = "".join(random.sample(all, length))
            label3 = tk.Label(root, text='Your Level ' + x1 + ' Password is generated.', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)

            label4 = tk.Label(root, text=password, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)
        elif x1 == '2':
            all = lower + upper
            length = 8
            password = "".join(random.sample(all, length))
            label3 = tk.Label(root, text='Your Level ' + x1 + ' Password is generated.', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)

            label4 = tk.Label(root, text=password, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)
        elif x1 == '3':
            all = lower + upper + numbers
            length = 10
            password = "".join(random.sample(all, length))
            label3 = tk.Label(root, text='Your Level ' + x1 + ' Password is generated.', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)

            label4 = tk.Label(root, text=password, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)
        elif x1 == 'alpha' or x1 == "Alpha" or x1=='A' or x1 == "a":
            all = lower + upper + numbers + symbols
            length = 12
            password = "".join(random.sample(all, length))
            label3 = tk.Label(root, text='Your Level ' + x1 + ' Password is generated.', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)

            label4 = tk.Label(root, text=password, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)
        else:
            label3 = tk.Label(root, text='You enter invalid level code.\n Please try again !', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)



    except Exception as e:
        exit(0)




button1 = tk.Button(text='Generate password', command=generatePass, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()