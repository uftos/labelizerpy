from tkinter import *
from PIL import Image, ImageDraw, ImageTk
   
def done():
    root.destroy()

def activate_paint(e):
    global lastx, lasty, numberHistory
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y
    numberHistory+=1
    history.append([])

def paint(e):
    global lastx, lasty, label
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill=color[(label-1)%9],width=3)
    draw.line((lastx, lasty, x, y), fill=label, width=3)
    history[numberHistory].append((lastx, lasty, x, y))
    lastx, lasty = x, y

def previous():
    global history, numberHistory
    if history:
       for lastx, lasty, x, y in history[numberHistory]:
           draw.line((lastx, lasty, x, y), fill="black", width=3)

       history.pop()
       numberHistory-=1

def changeLabel(event):
    global label
    if event.num == 5 or event.delta == -120:
        label -= 1
    if event.num == 4 or event.delta == 120:
        label += 1
    print(label)

def labelizer(image):
    global cv, draw, label, root, history, numberHistory, color
    color=["yellow","red","blue","white","pink","orange","purple","brown","green"]
    label=0
    history=[]
    numberHistory=-1
    root = Tk() 
    cv = Canvas(root, width = image.width, height = image.height)      
    cv.pack()      
    photo = ImageTk.PhotoImage(image)
    cv.create_image(0,0, anchor=NW, image=photo)      
    image1 = Image.new('L', (image.width, image.height), 'black')
    draw = ImageDraw.Draw(image1)
    cv.bind('<1>', activate_paint)
    cv.bind('<MouseWheel>', changeLabel)
    cv.bind('<Button-4>', changeLabel)
    cv.bind('<Button-5>', changeLabel)
    btn_save = Button(text="done", command=done)
    btn_save.pack()
    btn_previous = Button(text="previous", command=previous)
    btn_previous.pack()
    mainloop()
    return image1
