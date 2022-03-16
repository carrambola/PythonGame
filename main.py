import tkinter
import world
def key(event):
    print(event.keycode)
window = tkinter.Tk()
window.geometry("500x500")
w = world.World(window, 20, 20)
w.generateOrganisms()
w.draw()
frame = tkinter.Frame(window, width = 400, height = 400)
frame.focus_set()
frame.bind('<KeyPress>', w.key)
frame.pack()
window.mainloop()
