import tokenize
import io

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
        for member in tokens:
            if member[0] == 1 and member[1] in keyword_map:
                new_line = transform_line(new_line,member[2][1],member[3][1],keyword_map[member[1]])
        output_string += new_line
    f_p.close()
    return output_string

if __name__=="__main__":
    file_name=(input("1.: "))   #the script the user wrote
    language=(input("2.: "))    #the name of the language csv file to be used in translation
    #reads dictionary from language csv
    f = open(language+".csv", "r")
    lang_dict= {}
    for line in f:
        line_elems=line.strip().split(",")
        lang_dict[line_elems[0]]=line_elems[1]
    f.close()
    #maps python executable keywords to desired language
    new_code = preprocessor_test(file_name, lang_dict) 
    exec(new_code)





