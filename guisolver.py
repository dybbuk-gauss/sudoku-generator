


import tkinter
###for Gui
from functools import partial


cellbtnlist= []
modbtnlist = []

tk = tkinter.Tk()
tk.geometry("600x350+300+300")
tk.resizable(False,False)

indexes_to_collapse = []
entropy_list = []





def reset_color_state():
    for btn in cellbtnlist:
        btn['bg'] = "SystemButtonFace"


def add_coord_through_button(row,col):
    
    global tgt


    bgchanelist = set()
    tgt = cellbtnlist[col*9+row]
    cell_entropy = entropy_list[col*9+row]

    x_start = 0
    y_start = 0

    if row < 3:
        pass
    elif row < 6:
        x_start = 3
    elif row < 9:
        x_start = 6

    if col < 3:
            pass
    elif col < 6:
        y_start = 3
    elif col < 9:
        y_start = 6

    reset_color_state()


    for y in range(3):
        for x in range(3):
            bgchanelist.add(cellbtnlist[x_start+x+(y_start+y)*9])
            ##cellbtnlist[x_start+x+(y_start+y)*9]["bg"] = 'azure2'
    for x in range(9):
        bgchanelist.add(cellbtnlist[x+col*9])
        bgchanelist.add(cellbtnlist[x*9+row])
    

    for cell in list(bgchanelist):
        cell["bg"] = 'azure3'
        if cell['text'] != " ":
            print('candidate remove {t} from cell ({r},{c})'.format(t=int(cell['text']) ,r= row,c= col ))

            ## 엔트로피 제거를 여기서하면 안됨.
            if int(cell['text']) in cell_entropy:
                cell_entropy.remove(int(cell['text']))
    print(cell_entropy)

    tgt['bg'] = "green"
    
    for b in modbtnlist:
        if int(b['text']) in cell_entropy:
            b["state"] = tkinter.ACTIVE
        else:
            b["bg"] = "red4"

def set_cell(num):
    global tgt

    tgt["text"]="{i}".format(i=num)

    tgt = -1
    for b in modbtnlist:
        b["state"] = tkinter.DISABLED
        b["bg"] = "SystemButtonFace"
    reset_color_state()



if __name__ == "__main__":
    


    pixel = tkinter.PhotoImage(width=1, height=1)
    
    tlbl = tkinter.Label(tk,image=pixel, bg='gray', height=1)
    blbl = tkinter.Label(tk,image=pixel, bg='gray', height=1)
    rlbl = tkinter.Label(tk,image=pixel, bg='gray', width=1)
    llbl = tkinter.Label(tk,image=pixel, bg='gray', width=1)

    tlbl.grid(row=0,column=0,columnspan=10,sticky=tkinter.NSEW)
    

    for y in range(9):
        for x in range(9):
            btn = tkinter.Button(tk, text= " ", width= 3, height=1, command=partial(add_coord_through_button,x,y))
            btn.grid(row=x+1,column=y+1,padx=2,pady=2,ipadx=1,ipady=1)
            cellbtnlist.append(btn)
            entropy_list.append([ 1, 2, 3, 4, 5, 6, 7, 8, 9])

    

    llbl.grid(row=0,column=0, rowspan=12, sticky=tkinter.NSEW)

    blbl.grid(row=11,column=0,columnspan=10,sticky=tkinter.NSEW)
    rlbl.grid(row=0,column=11, rowspan=12, sticky=tkinter.NSEW)

    ###init entropy







    for y in range(3):
        for x in range(3):
            btn = tkinter.Button(tk, text= "{i}".format(i=x + y*3 + 1), width= 3, height=1, command=partial(set_cell,x + y*3 + 1))
            btn["state"] = tkinter.DISABLED
            btn.grid(row=y+1,column=x+12,padx=2,pady=2,ipadx=1,ipady=1)
            ###btn.place(x=350+35*(x%3),y=50+35*((int)(x/3)))
            modbtnlist.append(btn)

    tk.mainloop()



