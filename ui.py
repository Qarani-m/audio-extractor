import customtkinter
import subprocess
from extractor import Extractor
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
        self.button.place(x=450-75,y=10, )
        self.button = self.button_(45,150,self.view_history,"View Histroy","#dc143c")
        self.button.place(x=900-170,y=10, )
    def button_(self,height,width,command, text,fg_color):
        return customtkinter.CTkButton(self,command=command,fg_color=fg_color,height=height, width=width,text=text,)
    def select_one(self):
        files=[]
        file_name =customtkinter.filedialog.askopenfilename()
        Saving_file.handle_files(file_name)

    def select_multiple(self):
        files=[]
        file_names=customtkinter.filedialog.askopenfilenames()
        for file in file_names:
            Saving_file.handle_files(file)
            threading.Thread(target=Saving_file.handle_files,args=(file,)).start()


    def view_history(self):
        customtkinter.filedialog()



app = App()
app.mainloop()
