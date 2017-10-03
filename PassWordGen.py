from appJar import gui
import random

app = gui('PA$$GEN 1.0', '308x283')
app.setFont(20)
app.setBg("lightgrey")
# app.addImage("Password Gen", "insert folder path for PassGen Image")

def generate_password(btn):
    symbols = ['@', '#', '$', '%']
    numbers = str(range(0, 11))
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    lowercase2 = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    uppercase2 = ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    ambiguous_char = ['{', '}', '[', ']', '(', ')']
    ambiguous_char2 = ['~', ',', ';', ':', '.', '<', '>']
    password = [random.choice(symbols),
                random.choice(numbers),
                random.choice(lowercase),
                random.choice(lowercase2),
                random.choice(uppercase),
                random.choice(uppercase2),
                random.choice(ambiguous_char),
                random.choice(ambiguous_char2),
                random.choice(symbols),
                random.choice(numbers),
                random.choice(lowercase),
                random.choice(lowercase2),
                random.choice(uppercase),
                random.choice(uppercase2),
                random.choice(ambiguous_char),
                random.choice(ambiguous_char2)]

    getOptionBox = app.getOptionBox("How many characters:")
    random.shuffle(password)

    if getOptionBox == '6':
        app.setEntry("entry1", ''.join(password[0:6]))
        app.setMeter("Strength", 9.09090909091, text="Weak")
        app.setMeterFill("Strength", "red")
    elif getOptionBox == '7':
        app.setEntry("entry1", ''.join(password[0:7]))
        app.setMeter("Strength", 18.1818181818, text="Weak")
        app.setMeterFill("Strength", "red")
    elif getOptionBox == '8':
        app.setEntry("entry1", ''.join(password[0:8]))
        app.setMeter("Strength", 27.27272727273, text="Weak")
        app.setMeterFill("Strength", "red")
    elif getOptionBox == '9':
        app.setEntry("entry1", ''.join(password[0:9]))
        app.setMeter("Strength", 36.36363636364, text="Weak")
        app.setMeterFill("Strength", "red")
    elif getOptionBox == '10':
        app.setEntry("entry1", ''.join(password[0:10]))
        app.setMeter("Strength", 45.45454545455, text="Strong")
        app.setMeterFill("Strength", "green")
    elif getOptionBox == '11':
        app.setEntry("entry1", ''.join(password[0:11]))
        app.setMeter("Strength", 54.54545454546, text="Strong")
        app.setMeterFill("Strength", "green")
    elif getOptionBox == '12':
        app.setEntry("entry1", ''.join(password[0:12]))
        app.setMeter("Strength", 63.63636363637, text="Strong")
        app.setMeterFill("Strength", "green")
    elif getOptionBox == '13':
        app.setEntry("entry1", ''.join(password[0:13]))
        app.setMeter("Strength", 72.72727272728, text="Stronger")
        app.setMeterFill("Strength", "green")
    elif getOptionBox == '14':
        app.setEntry("entry1", ''.join(password[0:14]))
        app.setMeter("Strength", 81.81818181819, text="Stronger")
        app.setMeterFill("Strength", "green")
    elif getOptionBox == '15':
        app.setEntry("entry1", ''.join(password[0:15]))
        app.setMeter("Strength", 90.9090909091, text="Stronger")
        app.setMeterFill("Strength", "green")
    elif getOptionBox == '16':
        app.setEntry("entry1", ''.join(password[0:16]))
        app.setMeter("Strength", 100.00000000001, text="Strongest")
        app.setMeterFill("Strength", "orange")

CharRange = list(range(6, 17))
app.addLabelOptionBox("How many characters:", CharRange)
app.addEntry("entry1")
app.addButton("Generate", generate_password)
app.addMeter("Strength")
app.setMeter("Strength", 0, text="")
app.setMeterFill("Strength", "green")

app.go()
