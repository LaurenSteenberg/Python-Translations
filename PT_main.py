#Take in 2 cmd line args, [0] is txt file written by user; 
#       [1] language that represents the desired map file

#Call Artur’s function with (argos[0], args[1])

#Artur’s function will return a long string of python
#        executable code that can be run with exec()

if __name__=="__main__":
    file_name=(input("1.: "))
    language=(input("2.: "))
    #maps python executable keywords to desired language
    new_code = preprocessor_test(file_name, language) 
    exec(new_code)

