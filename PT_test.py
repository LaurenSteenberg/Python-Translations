# import re
import tokenize
import io
# Spanish Dictionary 
KEY_MAP_SPA = {
    "como" :"as",
    'y':'and',
    "declarar" : "assert",
   "dejar" : "break",
    "clase" : "class",
    "continuar" : "continue",
    "borrar" : "del",
    "osi" : "elif",
    "otro" : "else",
    "-" : "except",
    "Falso" : "False",
    "finalmente" : "finally",
    "por" : "for",
    "de" : "from",
    "mundial" :"global",
    "si" : "if",
    "Nada" : "None",
    "deatras" : "nonlocal",
    "no" : "not",
    "o" : "or",
    "pasar" : "pass",
    "imprimir" : "print",
    "levantar" : "raise",
    "regressar" : "return",
    "Verdad" : "True",
    "tratar" : "try",
    "cuando" : "while",
    "con" : "with"

}
tranducir={
    'y':'and',
           "declarar" : "assert",
           "dejar" : "break",
           "clase" : "class",
           "continuar" : "continue",
           "borrar" : "del",
           "osi" : "elif",
           "otro" : "else",
           "-" : "except",
           "Falso" : "False",
           "finalmente" : "finally",
           "por" : "for",
           "de" : "from",
           "mundial" :"global",
           "si" : "if",

           
           "Nada" : "None",
           "deatras" : "nonlocal",
           "no" : "not",
           "o" : "or",
           "pasar" : "pass",
           "levantar" : "raise",
           "regressar" : "return",
           "Verdad" : "True",
           "tratar" : "try",
           "cuando" : "while",
           "con" : "with"

           }

# Armenian Dictionary 
KEY_MAP_ARM = {
    "տպել": "print",
    "Õ¿ÕºÕ¥Õ¬": "print",

    "մինչդեռ": "while",
    "Õ´Õ«Õ¶Õ¹Õ¤Õ¥Õ¼": "while",

    "եթե": "if",
    "Õ¥Õ©Õ¥": "if",

    "համար": "for",

    
    "ուրիշ": "else",
    "Õ¸Ö‚Ö€Õ«Õ·": "else",
    
    "վերադարձ": "return",
    "Õ¾Õ¥Ö€Õ¡Õ¤Õ¡Ö€Õ±": "return",
    
    "սահմանել": "def",
    "Õ½Õ¡Õ°Õ´Õ¡Õ¶Õ¥Õ¬": "def"
}

def transform_line(line, start, end, new_word):
    # Purpose - Replaces single word in a given line with a given word

    # Parameters -
    #     line: (STRING) a string where the replacement should happen
    #     start: (INTEGER) a beginning index of the word
    #     end: (INTEGER) an end index of the word
    #     new_word: (STRING) the new line that has to be placed in the space

    # Return - The new line where the word is replaced
    list_look = line.split(line[start : end],1)
    
    return f"{new_word}".join(list_look)


def preprocessor_test(source_code, keyword_map):
    # Purpose - It takes a source code and it translates the keywords written in different language into an executable code.
    
    # Parameters -
    #    source_code: (STRING) Name of the file that contains the initial raw code. Either TXT or PY
    #    keyword_map: (DICTIONARY) Name of the language dictionary that the user wants the code to be translated from
    # Return - The translated code as a string. 
    f_p = open(source_code, "r")
    output_string = ''
    for line in f_p:
        tokens = list(tokenize.generate_tokens(io.StringIO(line).readline))
        new_line = line
        for member in tokens: #member[0] 
            if member[0] == 1 and member[1] in keyword_map: #recocnizes if keyword is type NAME and present in dict
                position=new_line.find(member[1])
                new_line = transform_line(new_line,  position,  position+len(member[1]),  keyword_map[member[1]]) #sends specific characters start and end locations on line
        output_string += new_line
    f_p.close()
    return output_string

if __name__=="__main__":
    file_name=(input("1.: "))
    translation_file=(input("2.: "))
    translated_dict={}
    fp = open(translation_file)
    for line in fp:
        line = line.split(",")=
        translated_dict[line[0]]=line[1][:-1]
    #maps python executable keywords to desired language
    new_code = preprocessor_test(file_name, translated_dict) 
    exec(new_code)


