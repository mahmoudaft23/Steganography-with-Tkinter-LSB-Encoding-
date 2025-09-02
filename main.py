from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from tkinter import messagebox
import random
import string
import sys
import os
from tkinter import filedialog
root = tk.Tk()
root.title("HW1")
root.geometry("700x750")


x = "1"
y=1
label = tk.Label(root, text="Original image:")
label.pack(side=tk.TOP, anchor='w', pady=1, padx=20)

def loed():
    global load, imgpixel, photo_label
    path = filedialog.askopenfilename()
    if path:
        load = Image.open(path)
        imgpixel = np.array(load)
        image = load.resize((250, 250))
        photo = ImageTk.PhotoImage(image)
        photo_label = tk.Label(root, image=photo)
        photo_label.image = photo
        photo_label.pack(side=tk.TOP, anchor='w', pady=1, padx=20)

def onebit(original,message):
    global matrix
    index = 0
    for k in range(load.height):
        for h in range(load.width - 1):
            newarr_zero = np.array_split(original[k][h], 3)
            red1_zero = newarr_zero[0][0]
            green1_zero = newarr_zero[1][0]
            blue1_zero = newarr_zero[2][0]
            red1_new_zero = (red1_zero & 0b11111100)
            green1_new_zero = (green1_zero & 0b11111100)
            blue1_new_zero = (blue1_zero & 0b11111100)
            original[k][h] = (red1_new_zero, green1_new_zero, blue1_new_zero)
    matrix = original.copy()
    for i in range(load.height):
        for j in range(0, load.width - 1, 3):
            if index < len(message):
                char = message[index]
                bits = format(ord(char), '08b')
                bits = list(map(int, bits))


                newarr = np.array_split(original[i][j], 3)
                red1 = newarr[0][0]
                green1 = newarr[1][0]
                blue1 = newarr[2][0]

                red1_new = (red1 & 0b11111110) | (bits[0])
                green1_new = (green1 & 0b11111110) | (bits[1])
                blue1_new = (blue1 & 0b11111110) | (bits[2])
                matrix[i][j] = (red1_new, green1_new, blue1_new)
                newarr2 = np.array_split(original[i][j + 1], 3)
                red2 = newarr2[0][0]
                green2 = newarr2[1][0]
                blue2 = newarr2[2][0]

                red2_new = (red2 & 0b11111110) | (bits[3])
                green2_new = (green2 & 0b11111110) | (bits[4])
                blue2_new = (blue2 & 0b11111110) | (bits[5])
                matrix[i][j + 1] = (red2_new, green2_new, blue2_new)

                newarr3 = np.array_split(original[i][j + 2], 3)
                red3 = newarr3[0][0]
                green3 = newarr3[1][0]
                blue3 = newarr3[2][0]


                red3_new = (red3 & 0b11111110) | (bits[6])
                green3_new = (green3 & 0b11111110) | (bits[7])
                matrix[i][j + 2] = (red3_new, green3_new, blue3)

                index += 1
            else:
                break
    return matrix


def towbit(original, message):
    global matrix
    index = 0
    for k in range(load.height):
        for h in range(load.width - 1):
            newarr_zero = np.array_split(original[k][h], 3)
            red1_zero= newarr_zero[0][0]
            green1_zero=newarr_zero[1][0]
            blue1_zero=newarr_zero[2][0]

            red1_new_zero = (red1_zero & 0b11111100)
            green1_new_zero = (green1_zero & 0b11111100)
            blue1_new_zero = (blue1_zero & 0b11111100)
            original[k][h] = (red1_new_zero, green1_new_zero, blue1_new_zero)
    matrix = original.copy()
    for i in range(load.height):
        for j in range(0, load.width - 1, 2):
            if index < len(message):
                char = message[index]
                bits = format(ord(char), '08b')
                bits = list(map(int, bits))

                newarr = np.array_split(original[i][j], 3)
                red1 = newarr[0][0]
                green1 = newarr[1][0]
                blue1 = newarr[2][0]


                red1_new = (red1 & 0b11111100) | (((bits[0] << 1) | bits[1]))
                green1_new = (green1 & 0b11111100) | (((bits[2] << 1) | bits[3]))
                blue1_new = (blue1 & 0b11111100) | (((bits[4] << 1) | bits[5]))
                matrix[i][j] = (red1_new, green1_new, blue1_new)

                newarr2 = np.array_split(original[i][j + 1], 3)
                red2 = newarr2[0][0]
                green2 = newarr2[1][0]
                blue2 = newarr2[2][0]
                red2_new = (red2 & 0b11111100) | ((bits[6] << 1) | bits[7])
                matrix[i][j + 1] = (red2_new, green2, blue2)

                index += 1
            else:
                break
    return matrix


def threebit(original, message):
    global matrix
    index = 0
    for k in range(load.height):
        for h in range(load.width - 1):

            newarr_zero = np.array_split(original[k][h], 3)
            red1_zero = newarr_zero[0][0]
            green1_zero = newarr_zero[1][0]
            blue1_zero = newarr_zero[2][0]

            red1_new_zero = (red1_zero & 0b11111100)
            green1_new_zero = (green1_zero & 0b11111100)
            blue1_new_zero = (blue1_zero & 0b11111100)
            original[k][h] = (red1_new_zero, green1_new_zero, blue1_new_zero)
    matrix = original.copy()
    for i in range(load.height):
        for j in range(load.width - 1):
            if index < len(message):
                char = message[index]
                bits = format(ord(char), '08b')
                bits = list(map(int, bits))

                newarr = np.array_split(original[i][j], 3)
                red1 = newarr[0][0]
                green1 = newarr[1][0]
                blue1 = newarr[2][0]

                red1_new = (red1 & 0b11111000) | (((bits[0] << 2) | ((bits[1] << 1) | bits[2])))
                green1_new = (green1 & 0b11111000) | (((bits[3] << 2) | ((bits[4] << 1) | bits[5])))
                blue1_new = (blue1 & 0b11111100) | (((bits[6] << 1) | bits[7]))
                matrix[i][j] = (red1_new, green1_new, blue1_new)

                index += 1
            else:
                break
    return matrix


def show_selection(value):
    global x
    x = value


def Restore():
    global x, matrix,y
    if y==1:
        matrix = imgpixel.copy()
    else:
        matrix=matrix
    if x == "1":
        print("\n1:")
        for i in range(load.height):
            for j in range(0, load.width - 1, 3):
                red, green, blue = matrix[i][j]
                red2, green2, blue2 = matrix[i][j + 1]
                red3, green3, blue3 = matrix[i][j + 2]

                if (red & 1 == 0 and green & 1 == 0 and blue & 1 == 0 and
                        red2 & 1 == 0 and green2 & 1 == 0 and blue2 & 1 == 0 and
                        red3 & 1 == 0 and green3 & 1 == 0):
                    break


                b = (red & 0b00000001)
                b2 = (green & 0b00000001)
                b3 = (blue & 0b00000001)
                b4 = (red2 & 0b00000001)
                b5 = (green2 & 0b00000001)
                b6 = (blue2 & 0b00000001)
                b7 = (red3 & 0b00000001)
                b8 = (green3 & 0b00000001)


                p = (b << 1) | b2
                p2 = (p << 1) | b3
                p3 = (p2 << 1) | b4
                p4 = (p3 << 1) | b5
                p5 = (p4 << 1) | b6
                p6 = (p5 << 1) | b7
                p7 = (p6 << 1) | b8

                print(f"Pixel {i + 1}:")
                print(f"  Red   : {format(red, '08b')}")
                print(f"  Green : {format(green, '08b')}")
                print(f"  Blue  : {format(blue, '08b')}")
                print(f"Pixel {i + 2}:")
                print(f"  Red2   : {format(red2, '08b')}")
                print(f"  Green2 : {format(green2, '08b')}")
                print(f"  Blue2  : {format(blue2, '08b')}")
                print(f"Pixel {i + 3}:")
                print(f"  Red2   : {format(red3, '08b')}")
                print(f"  Green2 : {format(green3, '08b')}")
                print(f"  Blue2  : {format(blue3, '08b')}")



                text_area.insert("end", chr(p7))




    elif x == "2":
        print("\n2:")
        for i in range(load.height):
            for j in range(0, load.width - 1, 2):
                red, green, blue = matrix[i][j]
                red2, green2, blue2 = matrix[i][j + 1]
                if (red & 1 == 0 and green & 1 == 0 and blue & 1 == 0 and
                        red2 & 1 == 0 ):
                    break


                b = (red & 0b00000011)
                b2 = (green & 0b00000011)
                b3 = (blue & 0b00000011)
                b4 = (red2 & 0b00000011)


                p = (b << 2) | b2
                p2 = (p << 2) | b3
                p3 = (p2 << 2) | b4

                print(f"Pixel {i + 1}:")
                print(f"  Red   : {format(red, '08b')}")
                print(f"  Green : {format(green, '08b')}")
                print(f"  Blue  : {format(blue, '08b')}")
                print(f"Pixel {i + 2}:")
                print(f"  Red2   : {format(red2, '08b')}")
                print(f"  Green2 : {format(green2, '08b')}")
                print(f"  Blue2  : {format(blue2, '08b')}")


                text_area.insert("end", chr(p3))


    elif x == "3":
        print("\n3:")
        for i in range(load.height):
            for j in range(load.width - 1):
                red, green, blue = matrix[i][j]

                if (red & 1 == 0 and green & 1 == 0 and blue & 1 == 0 ):
                    break


                b = (red & 0b00000111)
                b2 = (green & 0b00000111)
                b3 = (blue & 0b00000011)



                p = (b << 3) | b2
                p2 = (p << 2) | b3

                print(f"Pixel {i + 1}:")
                print(f"  Red   : {format(red, '08b')}")
                print(f"  Green : {format(green, '08b')}")
                print(f"  Blue  : {format(blue, '08b')}")


                text_area.insert("end", chr(p2))



def display_img(matrix2):
    label = tk.Label(root, text="Modified images:")
    label.pack(side=tk.TOP,anchor='w', pady=1, padx=20)
    encoded_image = Image.fromarray(matrix2)

    image = encoded_image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack(side=tk.BOTTOM,anchor='w', pady=1, padx=20)



def Hide():
    global x, matrix,y
    message = text_area.get("1.0", tk.END).strip()
    if x == "1":
        matrix = onebit(imgpixel, message)
    elif x == "2":
        matrix = towbit(imgpixel, message)
    elif x == "3":
        matrix = threebit(imgpixel, message)
    text_area.delete("1.0", tk.END)
    y=0
    display_img(matrix)


def clear():
    text_area.delete("1.0", tk.END)

def save():
    name= ''.join(random.choice(string.ascii_lowercase) for _ in range(10)).capitalize()
    encoded_image = Image.fromarray(matrix)
    encoded_image.save(name+".bmp")
def show_text():
    content = text_area.get("1.0", tk.END).strip()
    messagebox.showinfo("Text Content", content)

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)





text_area = tk.Text(root, height=10, width=40)
text_area.pack(side=tk.TOP,anchor='e',pady=5)


button_frame = tk.Frame(root)
button_frame.pack(side=tk.RIGHT,anchor='w', padx=5)
button_load = tk.Button(button_frame, text="load", command=loed)
button_load.pack(side=tk.RIGHT,anchor='w', padx=5)
button_Restart = tk.Button(button_frame, text="Restart", command=restart_program)
button_Restart.pack(side=tk.RIGHT,anchor='w', padx=5)
button_save = tk.Button(button_frame, text="save", command=save)
button_save.pack(side=tk.RIGHT,anchor='w', padx=5)

button_clear = tk.Button(button_frame, text="clear", command=clear)
button_clear.pack(side=tk.RIGHT,anchor='w', padx=5)
button_Restore = tk.Button(button_frame, text="Restore", command=Restore)
button_Restore.pack(side=tk.RIGHT,anchor='w', padx=5)

button_hide = tk.Button(button_frame, text="Hide", command=Hide)
button_hide.pack(side=tk.RIGHT, anchor='w',padx=5)
options = ["1", "2", "3"]
selected_option = tk.StringVar()
selected_option.set(options[0])
dropdown = tk.OptionMenu(button_frame, selected_option, *options, command=show_selection)
dropdown.pack(side=tk.LEFT, pady=20)

root.mainloop()
