import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

from tkinter import *
from PIL import Image, ImageTk
'''
def showVotes(root, frame1):
    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35, 35)))
    bjpImg = Label(frame1, image=bjpLogo)
    bjpImg.image = bjpLogo
    bjpImg.grid(row=2, column=0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((25, 38)))
    congImg = Label(frame1, image=congLogo)
    congImg.image = congLogo
    congImg.grid(row=3, column=0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45, 30)))
    aapImg = Label(frame1, image=aapLogo)
    aapImg.image = aapLogo
    aapImg.grid(row=4, column=0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40, 35)))
    ssImg = Label(frame1, image=ssLogo)
    ssImg.image = ssLogo
    ssImg.grid(row=5, column=0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((35, 25)))
    notaImg = Label(frame1, image=notaLogo)
    notaImg.image = notaLogo
    notaImg.grid(row=6, column=0)

    Label(frame1, text="BJP              :       ", font=('Helvetica', 12, 'bold')).grid(row=2, column=1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row=2, column=2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row=3, column=1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row=3, column=2)

    Label(frame1, text=" AAP               :          ", font=('Helvetica', 12, 'bold')).grid(row=4, column=1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row=4, column=2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Helvetica', 12, 'bold')).grid(row=5, column=1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold')).grid(row=5, column=2)

    Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold')).grid(row=6, column=1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row=6, column=2)

    frame1.pack()
    root.mainloop()

'''
def showVotes(root, frame1):
    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 16, 'bold')).grid(row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    parties = ['BJP', 'Cong', 'AAP', 'Shiv Sena', 'NOTA']
    votes = [result['bjp'], result['cong'], result['aap'], result['ss'], result['nota']]

    fig, ax = plt.subplots(figsize=(4, 4))  # Adjust the figure size here
    ax.bar(parties, votes)
    ax.set_xlabel('Parties')
    ax.set_ylabel('Votes')
    ax.set_title('Vote Count')

    # Create a Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=1, rowspan=5, columnspan=2)

    # Hide the toolbar
    toolbar = canvas.get_tk_widget().children['!toolbar']
    toolbar.pack_forget()

    frame1.pack()
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    frame1 = tk.Frame(root)
    showVotes(root, frame1)



'''def showVotes(root, frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    # Resize image using PIL and then pass it to ImageTk.PhotoImage
    bjp_img = Image.open("img/bjp.png").resize((35, 35), Image.ANTIALIAS)
    bjp_logo = ImageTk.PhotoImage(bjp_img)
    bjp_img_label = Label(frame1, image=bjp_logo)
    bjp_img_label.grid(row=2, column=0)

    cong_img = Image.open("img/cong.jpg").resize((25, 38), Image.ANTIALIAS)
    cong_logo = ImageTk.PhotoImage(cong_img)
    cong_img_label = Label(frame1, image=cong_logo)
    cong_img_label.grid(row=3, column=0)

    aap_img = Image.open("img/aap.png").resize((45, 30), Image.ANTIALIAS)
    aap_logo = ImageTk.PhotoImage(aap_img)
    aap_img_label = Label(frame1, image=aap_logo)
    aap_img_label.grid(row=4, column=0)

    ss_img = Image.open("img/ss.png").resize((40, 35), Image.ANTIALIAS)
    ss_logo = ImageTk.PhotoImage(ss_img)
    ss_img_label = Label(frame1, image=ss_logo)
    ss_img_label.grid(row=5, column=0)

    nota_img = Image.open("img/nota.jpg").resize((35, 25), Image.ANTIALIAS)
    nota_logo = ImageTk.PhotoImage(nota_img)
    nota_img_label = Label(frame1, image=nota_logo)'Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTa            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()'''


'''def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25,38),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45,30),Image.ANTIALIAS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40,35),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)


    Label(frame1, text="BJP              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" AAP               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()'''

'''from PIL import Image, ImageTk

def showVotes(root, frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25,38),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45,30),Image.ANTIALIAS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40,35),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)


    Label(frame1, text="BJP              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" AAP               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()'''



'''
if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    showVotes(root,frame1)
'''