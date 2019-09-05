from guizero import App, Text, TextBox, PushButton


def welcome_user():
    secondMessage.value = "Welcome " + userName.value;
    
app = App(title="Hello world" )
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="purple")
userName = TextBox(app)
update_text = PushButton(app, command=welcome_user, text= "Enter")

secondMessage = Text(app, text="", size=20, color="green")

def program():
    thirdMessage.value = "Hello " + userName.value;
    userName = TextBox(app) 
    update_text = PushButton(app, command=program, text= "start movement test")
    thirdMessage = Text(app, text="", size=20, color="red")
    

app.display()
