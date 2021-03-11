#Frontend

from tkinter import *
import tkinter.messagebox
import GameBack

class Game:
    def __init__(self, root):
        self.root=root
        self.root.title("Online Game Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="black")

        Game_Name=StringVar()
        Game_ID=StringVar()
        Release_Year=StringVar()
        Developer=StringVar()
        Genre=StringVar()
        Platform=StringVar()
        Mode=StringVar()
        Rating=StringVar()

        #Fuctions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Online Game Registration System", "Are you sure?")
            if iExit>0:
                root.destroy()
            return

        def clcdata():
            self.txtGame_ID.delete(0,END)
            self.txtGame_Name.delete(0,END)
            self.txtRelease_Year.delete(0,END)
            self.txtDeveloper.delete(0,END)
            self.txtGenre.delete(0,END)
            self.txtPlatform.delete(0,END)
            self.txtRating.delete(0,END)
            self.txtMode.delete(0,END)

        def adddata():
                if(len(Game_ID.get())!=0):
                    GameBack.AddGameRec(Game_ID.get(),Game_Name.get(),Release_Year.get(),Developer.get(),Genre.get(),Platform.get(),Mode.get(),Rating.get())
                    GameList.delete(0,END)
                    GameList.insert(END,(Game_ID.get(),Game_Name.get(),Release_Year.get(),Developer.get(),Genre.get(),Platform.get(),Mode.get(),Rating.get()))

        def disdata():
            GameList.delete(0,END)
            for row in GameBack.ViewGameData():
                GameList.insert(END, row, str(""))

        def Gamerec(event):
            global sd
            searchGame=GameList.curselection()[0]
            sd=GameList.get(searchGame)

            self.txtGame_ID.delete(0,END)
            self.txtGame_ID.insert(END,sd[1])
            self.txtGame_Name.delete(0,END)
            self.txtGame_Name.insert(END,sd[2])
            self.txtRelease_Year.delete(0,END)
            self.txtRelease_Year.insert(END,sd[3])
            self.txtDeveloper.delete(0,END)
            self.txtDeveloper.insert(END,sd[4])
            self.txtGenre.delete(0,END)
            self.txtGenre.insert(END,sd[5])
            self.txtPlatform.delete(0,END)
            self.txtPlatform.insert(END,sd[6])
            self.txtMode.delete(0,END)
            self.txtMode.insert(END,sd[7])
            self.txtRating.delete(0,END)
            self.txtRating.insert(END,sd[8])

        def deldata():
            if(len(Game_ID.get())!=0):
                GameBack.DeleteGameRec(sd[0])
                clcdata()
                disdata()

        def searchdb():
            GameList.delete(0,END)
            for row in GameBack.SearchGameData(Game_ID.get(),Game_Name.get(),Release_Year.get(),Developer.get(),Genre.get(),Platform.get(),Mode.get(),Rating.get()):
                GameList.insert(END, row, str(""))

        def updata():
            if(len(Game_ID.get())!=0):
                GameBack.DeleteGameRec(sd[0])
            if(len(Game_ID.get())!=0):
                GameBack.AddGameRec(Game_ID.get(),Game_Name.get(),Release_Year.get(),Developer.get(),Genre.get(),Platform.get(),Mode.get(),Rating.get())
                GameList.delete(0,END)
                GameList.insert(END,(Game_ID.get(),Game_Name.get(),Release_Year.get(),Developer.get(),Genre.get(),Platform.get(),Mode.get(),Rating.get()))

        #Frames
        MainFrame=Frame(self.root, bg="black")
        MainFrame.grid()

        TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="Online Game Registration System", bg="black", fg="orange")
        self.TFrame.grid() 

        BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Game Info_\n", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Game Details_\n", fg="white")
        DFrameR.pack(side=RIGHT)

        #Labels & Entry Box

        self.lblGame_ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Game ID:", padx=2, pady=2, bg="black", fg="orange")
        self.lblGame_ID.grid(row=0, column=0, sticky=W)
        self.txtGame_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Game_ID, width=39, bg="black", fg="white")
        self.txtGame_ID.grid(row=0, column=1) 

        self.lblGame_Name=Label(DFrameL, font=('Arial', 18, 'bold'), text="Game Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblGame_Name.grid(row=1, column=0, sticky=W) 
        self.txtGame_Name=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Game_Name, width=39, bg="black", fg="white")
        self.txtGame_Name.grid(row=1, column=1)

        self.lblRelease_Year=Label(DFrameL, font=('Arial', 18, 'bold'), text="Release Year:", padx=2, pady=2, bg="black", fg="orange")
        self.lblRelease_Year.grid(row=2, column=0, sticky=W) 
        self.txtRelease_Year=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Release_Year, width=39, bg="black", fg="white")
        self.txtRelease_Year.grid(row=2, column=1)

        self.lblDeveloper=Label(DFrameL, font=('Arial', 18, 'bold'), text="Developer:", padx=2, pady=2, bg="black", fg="orange")
        self.lblDeveloper.grid(row=3, column=0, sticky=W) 
        self.txtDeveloper=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Developer, width=39, bg="black", fg="white")
        self.txtDeveloper.grid(row=3, column=1)

        self.lblGenre=Label(DFrameL, font=('Arial', 18, 'bold'), text="Genre:", padx=2, pady=2, bg="black", fg="orange")
        self.lblGenre.grid(row=4, column=0, sticky=W) 
        self.txtGenre=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Genre, width=39, bg="black", fg="white")
        self.txtGenre.grid(row=4, column=1)

        self.lblPlatform=Label(DFrameL, font=('Arial', 18, 'bold'), text="Platform ", padx=2, pady=2, bg="black", fg="orange")
        self.lblPlatform.grid(row=5, column=0, sticky=W) 
        self.txtPlatform=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Platform, width=39, bg="black", fg="white")
        self.txtPlatform.grid(row=5, column=1)

        self.lblMode=Label(DFrameL, font=('Arial', 18, 'bold'), text="Mode ", padx=2, pady=2, bg="black", fg="orange")
        self.lblMode.grid(row=6, column=0, sticky=W) 
        self.txtMode=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Mode, width=39, bg="black", fg="white")
        self.txtMode.grid(row=6, column=1)

        self.lblRating=Label(DFrameL, font=('Arial', 18, 'bold'), text="Rating (Out of 5):", padx=2, pady=2, bg="black", fg="orange")
        self.lblRating.grid(row=7, column=0, sticky=W) 
        self.txtRating=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Rating, width=39, bg="black", fg="white")
        self.txtRating.grid(row=7, column=1)

        #ListBox & ScrollBar
        sb=Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        GameList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
        GameList.bind('<<ListboxSelect>>', Gamerec)
        GameList.grid(row=0, column=0, padx=8)
        sb.config(command=GameList.yview)

        #Buttons
        self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
        self.btnadd.grid(row=0, column=0)

        self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=disdata)
        self.btndis.grid(row=0, column=1)

        self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=clcdata)
        self.btnclc.grid(row=0, column=2)

        self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=searchdb)
        self.btnse.grid(row=0, column=3)

        self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=deldata)
        self.btndel.grid(row=0, column=4)

        self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=updata)
        self.btnup.grid(row=0, column=5)

        self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iExit)
        self.btnx.grid(row=0, column=6)


if __name__=='__main__':
    root=Tk()
    datbase=Game(root)
    root.mainloop()