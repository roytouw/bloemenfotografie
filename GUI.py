import matplotlib
matplotlib.use('Agg')
import tkinter as tk
import _thread

from PIL import ImageTk, Image
import time


class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.imagePanel = tk.Label(self.root)
        self.imagePanel.pack(side="bottom", fill="both", expand="yes")
        self.root.attributes("-fullscreen", True)

    def __del__(self):
        self.root.quit()

    def setImage(self, image):
        img = ImageTk.PhotoImage(image)
        self.imagePanel.config(image=img)
        self.imagePanel.image = img


def test(gui):
    time.sleep(2)
    newImage = Image.open("imgs/fust.jpg")
    newImage = newImage.resize((400, 400), Image.ANTIALIAS)
    gui.setImage(newImage)
    time.sleep(2)
    newImage = Image.open("imgs/fust2.jpg")
    newImage = newImage.resize((400, 400), Image.ANTIALIAS)
    gui.setImage(newImage)


if __name__ == "__main__":
    gui = GUI()
    _thread.start_new_thread(test, (gui, ))
    _thread.start_new_thread(gui.root.mainloop(), ())




