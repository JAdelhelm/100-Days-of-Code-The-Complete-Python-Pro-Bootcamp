# Desktop App to upload images and add a watermark
#%%
from PIL import Image, ImageTk, ImageFont, ImageDraw
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

class WaterMarkApp(tk.Tk):
    def __init__(self, title, size, watermark):
        super().__init__()
        self.size = size
        self.watermark = watermark

        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(width=size[0], height=size[1])

        self.title(title)

        self.upload_button()
        self.watermark_button()
        self.save_button()

    def upload_button(self):
        self.button_1 = tk.Button(self, text='Open Picture', command=self.upload_picture, width=20)
        self.button_1.place(relx=.3, rely=.9)

        # button.place(x=400, y=700)
    def watermark_button(self):
        self.button_2 = tk.Button(self, text='Add Watermark', command=self.add_watermark, width=20)
        self.button_2.place(relx=.45, rely=.9)
        # button.place(x=600, y=700)

    def save_button(self):
        self.button_3 = tk.Button(self, text='Save Picture', command=self.SavePicture, width=20)
        self.button_3.place(relx=.6, rely=.9)
        # button.place(x=600, y=700)

    def upload_picture(self, event=None):
        filename = filedialog.askopenfilename()
        self.img = Image.open(filename)
        # img.show()
        self.add_picture()

    def add_picture(self):
        try: self.panel.destroy()
        except: pass # No panel

        img_width_resize = self.img.width
        img_height_resize = self.img.height
        while img_width_resize*1.3 > self.size[0] or img_height_resize*1.3 > self.size[1]:
            img_width_resize = img_width_resize // 1.2
            img_height_resize = img_height_resize // 1.2

        img_size = (int(img_width_resize), int(img_height_resize))
        
        # By storing img_tk as self.img_tk, you ensure that it persists beyond the scope of the AddPicture method and is accessible throughout the lifetime of your WaterMarkApp instance.
        self.img_tk = ImageTk.PhotoImage(image=self.img.resize(img_size))
        self.panel = tk.Label(self, image=self.img_tk)
        # self.panel.grid(row=0, column=2)
        self.panel.pack(fill=None, expand=True)
        # panel.place(x=350, y=100)


    def add_watermark(self):

        image = self.img


        fontsize = 1 

        img_fraction = 0.7
        font = ImageFont.truetype("arial.ttf", fontsize)
        
        while font.getbbox(self.watermark)[2] < img_fraction*image.size[0] and font.getbbox(self.watermark)[3] < img_fraction*image.size[1]:
            fontsize += 1
            font = ImageFont.truetype("arial.ttf", fontsize-1)


        txt = Image.new('RGBA', image.size, (255,255,255,0))

        d = ImageDraw.Draw(txt)    
        # Mid Position of picture
        d.text((image.width // 2, image.height // 2),  self.watermark, anchor="ms", fill=(0, 0, 0, 110), font=font)
    

        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        if txt.mode != 'RGBA':
            txt = txt.convert('RGBA')
        combined = Image.alpha_composite(image, txt.rotate(30))    

        # combined.save("foo.png")
        self.img = combined
        self.add_picture()



    def SavePicture(self):
        filename = filedialog.asksaveasfile(mode="wb", defaultextension=".png")
        if filename: # asksaveasfile return `None` if dialog closed with "cancel".
            self.img.save(filename)



if __name__ == "__main__":
    app = WaterMarkApp(title="Watermark-PictureApp", size=(1200, 800), watermark="Copyright")
    app.mainloop()