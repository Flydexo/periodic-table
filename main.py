from tkinter import Button, Label, Frame, Tk
from data import elements
from colors import darker
import urllib.request
import io
from webbrowser import open_new

root = Tk()
root.title("Tableau Périodique")
root.iconbitmap("./icon.ico")
root.geometry("1280x720")
mainframe = Frame(root,bg="#18181b",width=1280,height=720)
root.configure(bg="#18181b")
mainframe.grid(column=18,row=10,ipadx=5,ipady=5)
root.columnconfigure(0)
root.rowconfigure(0)

images = []

white = "#ffffff"
bg="#18181b"

def back(): 
    for widget in mainframe.winfo_children():
        widget.destroy()
    images = []
    display()


def click(i): 
    atom = elements[i]
    for widget in mainframe.winfo_children():
        widget.destroy()

    backbutton = Button(mainframe, text='Go Back', command=back,fg=bg,bg=white,font="Helvetica 12 bold",border=0,cursor="hand1")
    backbutton.place(x=24,y=24)
    name = Label(mainframe, text=atom["name"], font="Helvetica 24 bold",fg=white,bg=bg)
    name.place(x=24,y=72)
    symbol = Label(mainframe, text=atom["symbol"], font="Helvetica 24",fg=white,bg=bg)
    symbol.place(x=24+24*len(atom["name"]),y=72)
    summary = ""
    for i in range(int(len(atom["summary"]) / 80)+1):
        end = i*80+80
        if end >= len(atom["summary"]):
            end = len(atom["summary"])-1
        separator = ""
        if atom["summary"][end] != " " and atom["summary"][end-1]!= " ":
            separator = "-"
        if end == len(atom["summary"])-1:
            separator = "."
        summary+=atom["summary"][i*80:end]+separator+"\n"
    summary = Label(mainframe, justify="left",text=summary, font="Helvetica 18",fg=white,bg=bg)
    summary.place(x=24,y=124)
    root.update()
    z= Label(mainframe, text="Z="+str(atom["number"]), font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=summary.winfo_height()+summary.winfo_y())
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Electron configuration: "+str(atom["electron_configuration"]), font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Category: "+str(atom["category"]), font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Discovered by: "+str(atom["discovered_by"]), font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Named by: "+str(atom["named_by"]), font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Atomic mass: "+str(atom["atomic_mass"])+"u", font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Fusion: "+str(atom["melt"])+"K", font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    root.update()
    lastesty = z.winfo_y()+z.winfo_height()
    z = Label(mainframe, text="Source (click to copy): ", font="Helvetica 18",fg=white,bg=bg)
    z.place(x=24,y=lastesty+12)
    z = Label(mainframe, text="Source: "+atom["source"],font="Helvetica 18",fg="#34abeb",bg=bg,cursor="hand1")
    z.place(x=24,y=lastesty+12)
    z.bind('<Button-1>', lambda e,s=atom["source"]: openUrl(s))


def openUrl(s):
    open_new(s)

def display():
    for i in range(len(elements)):
        atom = elements[i]
        frame = Frame(mainframe, width=71,height=71,background="#"+atom["cpk-hex"],highlightthickness=5,highlightbackground=darker("#"+atom["cpk-hex"]))
        frame.grid(column=atom["xpos"],row=atom["ypos"])
        frame.bind("<Button-1>", lambda e,_i=i: click(_i))
        label = Label(frame, text=atom["symbol"],background="#"+atom["cpk-hex"],font="Helvetica 14 bold")
        label.place(x=25-len(atom["symbol"])*5,y=20)
        label.bind("<Button-1>",lambda e,_i=i: click(_i))

display()
root.mainloop()