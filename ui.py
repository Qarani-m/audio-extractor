import customtkinter
from file_handler import Saving_file
import threading
from tkVideoPlayer import TkinterVideo

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x700")
        self.title("Em Audio extractor")
        self.file_name=""
        # t1 = 
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
# play the video
    def video_player(self):
        videoplayer = TkinterVideo(master=self, scaled=True,keep_aspect=False)
        videoplayer.set_size((100,100))
        videoplayer
        videoplayer.load(self.file_name)
        videoplayer.place(x=100,y=200)
        videoplayer.play() 
    def select_one(self):
        files=[]
        self.file_name =customtkinter.filedialog.askopenfilename()
        t1 = threading.Thread(target=self.video_player)
        t1.start()
        t1 = threading.Thread(target=self.video_player)
        t1.start()
        t2= threading.Thread(target =Saving_file.handle_files,args=(self.file_name,))
        t2.start()
        # Saving_file.handle_files(self.file_name)

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
