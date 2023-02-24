import customtkinter
import subprocess
from converter import Extractor
from file_handler import Saving_file
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
        
    def handle_files():
        pass

    def select_one(self):
        files=[]
        file_name =customtkinter.filedialog.askopenfilename()
        file=Saving_file(file_name).save()
        extractor = Extractor(file_name,file[0],file[1])
        t2 = threading.Thread(target=extractor.moviepy_way)
        t2.start()

        extractor.moviepy_way()
    def select_multiple(self):
        file_names=customtkinter.filedialog.askopenfilenames()
        print(file_names)
    def view_history(self):
        customtkinter.filedialog()



app = App()
app.mainloop()
