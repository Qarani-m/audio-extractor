import customtkinter
import subprocess
from converter import Extractor
import time
import threading

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x700")
        self.title("Em Audio extractor")
        self.resizable(False, False)
        self.add_buttons()
        


    def add_buttons(self):
        self.button = self.button_(45,150,self.select_one,"Extract One","#dc143c")
        self.button.grid(row=200, column=0, padx=20, pady=10)
        self.button = self.button_(45,150,self.select_multiple,"Extract multiple","#dc143c")
        self.button.grid(row=700, column=0, padx=20, pady=10)
        self.button = self.button_(45,150,self.view_history,"View Histroy","#dc143c")
        self.button.grid(row=1400, column=300, padx=20, pady=10)


    def button_(self,height,width,command, text,fg_color):
        return customtkinter.CTkButton(self,command=command,fg_color=fg_color,height=height, width=width,text=text,)
        
            

    def select_one(self):
        file_name =customtkinter.filedialog.askopenfilename()
        extractor = Extractor(file_name)
        t2 = threading.Thread(target=extractor.moviepy_way)
        t2.start()

        extractor.moviepy_way()
    def select_multiple(self):
        file_names=customtkinter.filedialog.askdirect()
    def view_history(self):
        customtkinter.filedialog()



app = App()
app.mainloop()
