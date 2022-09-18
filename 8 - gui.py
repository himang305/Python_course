from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Welcome to LearningWhilePracticing")
window.geometry("400x150")

lbl = Label(window, text="Hello World", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Please enter your name")
lbl2.grid(column=0, row=1)

txt = Entry(window, width=20)
txt.grid(column=1, row=1)

def GreetUser():
    userName = txt.get()
    print("Cancel button is clicked")   # print in console
    messagebox.showinfo("LearingWhilePracticing", "Hello, " + userName)


btn = Button(window, text="Click Me",bg="yellow",fg="red",command=GreetUser)
btn.grid(column=2, row=1)


window.mainloop()

#evey line in here would be blocked
#until the window is closed




class WidgetsDemo:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Widgets Demo")  # Set a title

        # Add a check button, and a radio button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text="Bold",
                              variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
                            variable=self.v2, value = 1,
                            command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text="Yellow",
                               bg="yellow", variable=self.v2, value=2,
                               command = self.processRadiobutton)
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        # Add a label, an entry, a button, and a message to frame1
        frame2 = Frame(window)  # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text="Get Name",
                           command=self.processButton)
        message = Message(frame2, text="It is a widgets demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        # Add text
        text = Text(window)  # Create and add text to the window
        text.pack()
        text.insert(END,
                    "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END,
                    "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")

        window.mainloop()  # Create an event loop

    def processCheckbutton(self):
        print("check button is "
              + ("checked " if self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow")
              + " is selected ")

    def processButton(self):
        print("Your name is " + self.name.get())

WidgetsDemo() # Create GUI