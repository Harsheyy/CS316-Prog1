
#!/usr/bin/python
import cgi

form = cgi.FieldStorage()

def main():
    initial = (form.getvalue('origunits')).lower()
    final = (form.getvalue('convunits')).lower()
    amount = (form.getvalue('numunits'))
    factor = (form.getvalue('convfactor'))

    words = ['parsec', 'lightyear', 'kilometer', 'xlarn', 'galacticyear', 'terrestrialyear', 'xarnyear', 'terrestrialminute']

    for i in words:
        if(initial != words[i] or final != words[i]):
           print("Error: (" +initial + " , " + final + ") are incorrect")

    if(isinstance(amount, int) != True):
        print("Error: Conversion amount value is incorrect")

    if(isinstance(factor, int) != True):
        print("Error: Conversion factor value is incorrect")

    if(amount == 0 or factor == 0):
        print("Error: Input is 0")

    if(initial == None or final == None or amount == None or factor == None):
        print("Error: Missing input")

    parsec = {"parsec": 1, "lightyear": 3.26, "xlarn": 0.1357367792}
    lightyear = {"lightyear": 1, "kilometer": 30860000000000000}
    kilometer = {"kilometer": 1, "lightyear": 3.24044069993519e-17}
    xlarn = {"xlarn": 1, "parsec": 7.3672}

    galacticyear = {"galacticyear":1, "terrestrialyear": 250000000}
    terrestrialyear = {"terrestrialyear": 1, "xarnyear": 0.794975753239526, "terrestrialminute": 525600}
    xarnyear = {"xarnyear": 1, "terrestrialyear": 1.2579}
    terrestrialminute = {"terrestrialminute": 1, "terrestrialyear": 1.9025875190258}

