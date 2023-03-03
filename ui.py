import customtkinter
from file_handler import Saving_file
import threading
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
from tkinter import*


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x700")
        self.title("Em Audio extractor")
        self.file_name=""
        self.resizable(False, False)
        self.add_buttons()
    def add_buttons(self):
        self.button = self.button_(45,150,self.select_one,"Extract One","#dc143c")
        self.button.grid(row=200, column=0, padx=20, pady=10)
        self.button = self.button_(45,150,self.select_multiple,"Extract multiple","#dc143c")
        self.button.place(x=450-75,y=10, )
        self.button = self.button_(45,150,self.view_history,"View Histroy","#dc143c")
        self.button.place(x=900-170,y=10, )
        self.button = self.button_(45,150,self.clip_video,"Clip Video","#dc143c")
        self.button.place(x=390-200,y=70, )
        self.button = self.button_(45,150,self.clip_video,"Clip Video","#dc143c")
        self.button.place(x=750-200,y=70, )
        self.button = self.button_(45,150,self.select_multiple,"Extract multiple","#dc143c")
        self.button.place(x=450-75,y=150, )
        self.button = self.button_(45,150,self.view_history,"View Histroy","#dc143c")
        self.button.place(x=900-170,y=150, )
        self.button = self.button_(45,150,self.view_history,"View Histroy","#dc143c")
        self.button.place(x=20,y=150, )
    def button_(self,height,width,command, text,fg_color):
        return customtkinter.CTkButton(self,command=command,fg_color=fg_color,height=height, width=width,text=text,)
    def video_player(self):
        width =500
        height=450
        frame = Frame(self, height=height, width=500, bg="#dc143c")
        frame.place(x=20,y=220, )
        my_label = Label(frame, width=500, height=height)
        my_label.pack()
        player = tkvideo(self.file_name, my_label, loop=1, size=(500, height))
        player.play()
        my_label.pack_propagate(0)
    def select_one(self):
        self.file_name =customtkinter.filedialog.askopenfilename()
        t1 = threading.Thread(target=self.video_player)
        t1.start()
        t2= threading.Thread(target =Saving_file.handle_files,args=(self.file_name,))
        t2.start()
    def select_multiple(self):
        file_names=customtkinter.filedialog.askopenfilenames()
        for file in file_names:
            Saving_file.handle_files(file)
            threading.Thread(target=Saving_file.handle_files,args=(file,)).start()
    def view_history(self):
        customtkinter.filedialog()
    def clip_video(self):
        pass
app = App()
app.mainloop()