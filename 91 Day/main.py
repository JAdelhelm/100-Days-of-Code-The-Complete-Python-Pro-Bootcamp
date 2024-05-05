# Desktop App to upload images and add a watermark
#%%
from PIL import Image, ImageTk, ImageFont, ImageDraw
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import PyPDF3
import pyttsx3
import pdfplumber

class PDFtoAudio(tk.Tk):
    def __init__(self, title, size, watermark):
        super().__init__()
        self.size = size
        self.watermark = watermark

        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(width=size[0], height=size[1])

        self.title(title)

        self.finalText = "No PDF-Text extracted"

        self.upload_button()
        self.save_button()

    def upload_button(self):
        self.button_1 = tk.Button(self, text='Open PDF', command=self.upload_pdf, width=20)
        self.button_1.place(relx=.3, rely=.9)

        # button.place(x=400, y=700)

    def upload_pdf(self, event=None):
        self.file = filedialog.askopenfilename()
        # Extract the filename of original
        self.extracted_filename = self.file.split("/")[-1].split(".")[0]
        # print("FILENAME: ", self.file.split("/")[-1])
        # File here
        book = open(self.file, 'rb')
        pdfReader = PyPDF3.PdfFileReader(book)
        pages = pdfReader.numPages
        finalText = ""

        self.processing = tk.Label(self, text="Processing file...")
        self.processing.configure(font=("Times New Roman", 32, "bold"))
        self.processing.place(relx=.35, rely=.5)

        with pdfplumber.open(self.file) as pdf:
            for i in range(0, pages):
                page = pdf.pages[i]
                text = page.extract_text()
                finalText += text

        self.processing["text"] = "Sucessfully added PDF!"

        self.finalText = finalText


    def save_button(self):
        self.button_3 = tk.Button(self, text='Save Audiobook', command=self.SaveAudio, width=20)
        self.button_3.place(relx=.6, rely=.9)
        # button.place(x=600, y=700)



    def SaveAudio(self):
        # filename = filedialog.asksaveasfile(mode="wb")
        directory_path = filedialog.askdirectory()
        # print(directory_path)
        # print()
        if directory_path: # asksaveasfile return `None` if dialog closed with "cancel".
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')   
            engine.setProperty('voice', voices[1].id)
            engine.save_to_file(self.finalText, f"{directory_path}/{self.extracted_filename}.mp3")
            engine.runAndWait()
            try: self.processing["text"] = "Sucessfully saved!"
            except: pass



if __name__ == "__main__":
    app = PDFtoAudio(title="Audio to PDF", size=(1200, 800), watermark="Copyright")
    app.mainloop()