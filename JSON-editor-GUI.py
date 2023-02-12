from tkinter import *
from tkinter import filedialog
# def submit():
#     file = filedialog.asksaveasfile(defaultextension='.txt',
#                                     filetypes=[
#                                         ("All files",".*")
#                                     ])
#     input = text.get('1.0',END)
#     file.write(input)
#     file.close()

def getFile():
    global path
    path = filedialog.askopenfilename()
    file = open(path,'rt')
    fileText.insert('1.0',file.read().replace(" ",""))
    file.close()
    file = open(path,'rt')
    file.close()
    if file == "":
        file.close()
        file = open(path, "w")
        file.write("{")
        file.close()
    
    getFileName(path)
def getFileName(way):
    # path = filedialog.askopenfilename()
    i = 1
    filename = ""
    while i < len(way):
        # print(len(way))
        # print(way[len(way) - i])
        if way[len(way) - i] != "/":
            filename = filename + way[len(way) - i]
        if way[len(way) - i] == "/":
            break
        i+=1
    text.insert('1.0', filename [::-1])
    
def submit():
    inputName = nameEntry.get('1.0',END)
    inputValue = valueEntry.get('1.0',END)
    if inputName != "" or inputValue != "":
        # print(inputName.replace("\n",""))
        # print(inputValue.replace("\n",""))
        file = open(path,"r")
        line = file.read().replace("}",",")
        file.close()
        if line == "":
            line = "{"
        # line =f"{line} \"{inputName.replace("\n","")}\" : \"{inputValue.replace("\n","")}\""
        line = line + "\"" + inputName.replace("\n","") + "\"" + ":" + "\"" + inputValue.replace("\n","") + "\""
        line = line + "}"
        file = open(path,"w")
        readFile = open(path, "r")
        file.write(f"{readFile.read()} {line}")
        file.close()
        file = open(path,'rt')
        fileText.insert('1.0',file.read().replace(" ",""))
        file.close()

root = Tk()
root.geometry('400x400')
root.title("JSON Editor")
img=PhotoImage(file="./JSON.png")
root.iconphoto(False,img)
filechose = Button(root,text="Open",command=getFile,width=20)
text = Text(root, width = 20, height = 1, wrap = WORD)
fileText = Text(root,width=20,height=3)
nameLabel = Label(root, text = "Name of propertie")
fileContents = Label(root, text = "File contents")
nameEntry = Text(root,width=20, height = 1)
valueLabel = Label(root, text = "Value of propertie")
valueEntry = Text(root,width=20, height = 1)
submitButton = Button(root, text = "Submit", command=submit)
# filename = Entry(root)
filechose.grid(row=0, column=1)
text.grid(row=0, column=2)
fileText.grid(row=1, column=2)
fileContents.grid(row=1, column=1)
nameLabel.grid(row=2, column=1)
nameEntry.grid(row=2, column=2)
valueLabel.grid(row=3, column=1)
valueEntry.grid(row=3, column=2)
submitButton.grid(row=4, column=1)

root.mainloop()
