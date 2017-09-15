#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi, cgitb


def Print_output(initial, final, amount, factor): 
    conv_list={
    "parsec": {"parsec": 1, "lightyear": 3.26, "xlarn": 0.1357367792},
    "lightyear": {"lightyear": 1, "kilometer": 30860000000000000},
    "kilometer": {"kilometer": 1, "lightyear": 3.24044069993519e-17},
    "xlarn": {"xlarn": 1, "parsec": 7.3672},
    "galacticyear": {"galacticyear":1, "terrestrialyear": 250000000},
    "terrestrialyear": {"terrestrialyear": 1, "xarnyear": 0.794975753239526, "terrestrialminute": 525600},
    "xarnyear": {"xarnyear": 1, "terrestrialyear": 1.2579},
    "terrestrialminute": {"terrestrialminute": 1, "terrestrialyear": 1.9025875190258}
    }
    
    for key1,value1 in conv_list.items():
        if key1==initial:
            for key2, value2 in value1.items():
                if key2==final:
                  print ("Original Units: " + initial + "\n")         
                  print ("Conversion Units: " + final)
                  print ("Conversion Value: " +str(amount))
                  print ("Conversion Factor: " + str(factor)) 
                  print (str(amount) +" " + initial + " equals " +" " + str(amount * value2) +" "+ final) 
                 
def Check_input(factor, amount):
    num_flag=False
    if(amount == None or factor == None):
                print("Error: Missing input ")
    else:
        try:
            if((isinstance(float(amount), float) or (isinstance(int(amount), int))) and (isinstance(float(factor), float) or (isinstance(int(factor), int)))):
                
    
                if(round(float(amount),0) ==0  or round(float(factor),0) == 0):
                    print("Error: Input is 0 ")
                else:
                    num_flag=True
        except ValueError:
	    print "One of your conversion values is a string"
    return num_flag


       
def main():
    
    form=cgi.FieldStorage()  
	
    initial = (form.getvalue('origunits'))
    final = (form.getvalue('convunits'))
    amount = (form.getvalue('numunits'))
    factor = (form.getvalue('convfactor'))
      

    words = ['parsec', 'lightyear', 'kilometer', 'xlarn', 'galacticyear', 'terrestrialyear', 'xarnyear', 'terrestrialminute']
   
    unit_flag1=False
    unit_flag2=False
   
    if (initial==None or final==None): 
        print("Error: Missing input")
    else:
        for i in range(len(words)):
            if(initial.lower() == words[i]):
	        unit_flag1=True 
                initial=initial.lower() 
            if (final.lower() == words[i]):
	        unit_flag2=True
                final=final.lower()
        if (unit_flag2==False or unit_flag1==False):
            print("Error: ( "+ initial+" , " + final + " ) are incorrect ")
    
    num_flag=Check_input(factor, amount)
   
    if (num_flag==True and unit_flag1==True and unit_flag2==True):
        factor=float(factor)
        amount=float(amount)
        Print_output(initial, final, amount, factor)

main()
