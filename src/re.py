def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)


    #icon
    image_icon1=PhotoImage(file="Image/receive.png")
    main.iconphoto(False,iamge_icon1)

    main.mainloop()