import tkinter
from PIL import Image, ImageTk
import numpy as np

class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.label = tkinter.Label(text="your image here", compound="top")
        self.label.pack(side="top", padx=8, pady=8)
        self.iteration=0
        self.UpdateImage(1)

    def UpdateImage(self, delay, event=None):
        # this is merely so the display changes even though the image doesn't
        self.iteration += 1
        self.image = self.get_image()
        self.label.configure(image=self.image, text="Iteration %s" % self.iteration)
        # reschedule to run again in 1 second
        self.after(delay, self.UpdateImage, 1)


    def get_image(self):
        # this is where you get your image and convert it to
        # a Tk PhotoImage. For demonstration purposes I'll
        # just return a static image
        array = np.random.rand(240*3,320*3) * 255
        img =  ImageTk.PhotoImage(image=Image.fromarray(array))
        return img

if __name__ == "__main__":
    app=App()
    app.mainloop()
