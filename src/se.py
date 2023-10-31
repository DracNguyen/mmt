def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)


    #icon
    image_icon1=PhotoImage(file="Image/send.png")
    window.iconphoto(False,iamge_icon1)
    
    Sbackground=PhotoImage(file="Image/sender.png")
    Label(window,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file="Image/id.png")
    Label(window,image=Mbackground,bg='#f4fdfe').place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x-140,y-290)

    Button(window,text="+ select file",width=10,height =1 ,font='arial 14 bold', bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold', bg="#000",fg="#fff").place(x=300,y=150)

    window.mainloop()