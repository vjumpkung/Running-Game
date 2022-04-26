import tkinter as tk
from verify import Authenticate
from main import main

auth = Authenticate()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Running Game")
        self.geometry("640x320")
        self.resizable(0,0)
        
        # Frame 1
        self.pack_frame = tk.Frame(self)
        self.pack_frame.pack(pady=10)
        
        # Title
        self.label = tk.Label(self.pack_frame, text='Running Game', font=("Ubuntu", 48))
        self.label.pack()
        
        # Frame 2
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(pady=10)
        
        # login label
        self.logintxt = tk.Label(self.grid_frame, text='Username', font=("Ubuntu Mono", 24))
        self.logintxt.grid(row=0, column=0, padx=10)
                
        # login
        self.get_login = tk.StringVar()
        self.textbox = tk.Entry(self.grid_frame, width=20, font=("Ubuntu Mono", 24), textvariable=self.get_login)
        self.textbox.grid(row=0, column=1)
        
        # Frame 3
        self.grid_frame2 = tk.Frame(self)
        self.grid_frame2.pack(pady=10)
        
        # password label
        self.passtxt = tk.Label(self.grid_frame2, text='Password', font=("Ubuntu Mono", 24))
        self.passtxt.grid(row=0, column=0, padx=10)
    
        # password
        self.get_password = tk.StringVar()
        self.textbox2 = tk.Entry(self.grid_frame2, width=20, font=("Ubuntu Mono", 24), show="*", textvariable=self.get_password)
        self.textbox2.grid(row=0, column=1)
        
        # Frame 4
        self.pack_frame2 = tk.Frame(self)
        self.pack_frame2.pack(pady=10)
        
        # sign in
        self.button = tk.Button(self.pack_frame2, text='Sign in', font=("Ubuntu Mono", 16))
        self.button['command'] = self.button_clicked
        self.button.pack(side=tk.LEFT, padx=5)
        
        # sign up
        self.button2 = tk.Button(self.pack_frame2, text='Sign UP', font=("Ubuntu Mono", 16))
        self.button2['command'] = self.button_clicked2
        self.button2.pack(side=tk.LEFT, padx=5)
        
        # Frame 5
        self.pack_frame3 = tk.Frame(self)
        self.pack_frame3.pack(pady=10)
        
        # Check Login status
        self.status = tk.StringVar()
        self.status.set("")
        self.status_check = tk.Label(self.pack_frame3, textvariable = self.status)
        self.status_check.pack()
        
    def show_menu(self):
        
        # Frame 7
        self.pack_frame7 = tk.Frame(self)
        self.pack_frame7.pack(pady=10)
        
        # Title
        self.label2 = tk.Label(self.pack_frame7, text=f'Welcome {self.username}', font=("Ubuntu", 36))
        self.label2.pack()
                
        # Frame 6
        self.frame_logout = tk.Frame(self)
        self.frame_logout.pack(pady=10)
        
        # sign out
        self.lo_button = tk.Button(self.frame_logout, text='Logout', font=("Ubuntu Mono", 16))
        self.lo_button['command'] = self.lg_out
        self.lo_button.pack(side=tk.LEFT, padx=5)
        
        # play game
        self.p_button = tk.Button(self.frame_logout, text='PLAY', font=("Ubuntu Mono", 16))
        self.p_button['command'] = self.play_game
        self.p_button.pack(side=tk.LEFT, padx=5)
        
    def clear_text(self):
        self.after(5000, lambda: self.status.set(""))
        
    def button_clicked(self):
        self.username = self.textbox.get()
        if auth.login(self.textbox.get(), self.textbox2.get()):
            self.textbox.delete(0, 'end')
            self.textbox2.delete(0, 'end')
            self.status.set("complete")
            self.grid_frame.pack_forget()
            self.grid_frame2.pack_forget()
            self.pack_frame2.pack_forget()
            self.pack_frame3.pack_forget()
            self.show_menu()
        else:
            self.status.set("Not found in database")
        self.clear_text()

    def button_clicked2(self):
        if auth.register(self.textbox.get(), self.textbox2.get()):
            self.status.set("Register Complete , you can login now")
        else:
            self.status.set("You are already registered")
        self.clear_text()
        
    def lg_out(self):
        self.frame_logout.pack_forget()
        self.pack_frame7.pack_forget()
        self.grid_frame.pack(pady=10)
        self.grid_frame2.pack(pady=10)
        self.pack_frame2.pack(pady=10)
        self.pack_frame3.pack(pady=10)

    def play_game(self):
        self.withdraw()
        main()
        self.deiconify()

if __name__ == "__main__":
    app = App()
    app.mainloop()