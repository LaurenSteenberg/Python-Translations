# import re
import tokenize
import io
# KEY_MAP = {
#     "grir": "print",
#     "qani": "while",
#     "ete": "if",
#     "urish": "else",
#     "veradarcru": "return",
#     "sahmanel": "def"
# }
# KEY_MAP = {
#     "imprimir": "print",
#     "mientras": "while",
#     "si": "if",
#     "demas": "else",
#     "devolver": "return",
#     "definir": "def"
# }
KEY_MAP = {
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

# def preprocessor_test(source_code, keyword_map):
#     f_p = open(source_code, "r")
#     user_code = f_p.read()
#     f_p.close()
    
#     for keyWord in keyword_map:
#         user_code = re.sub(r'\b' + re.escape(keyWord) + r'\b', re.escape(keyword_map[keyWord]), user_code)
#     return user_code

def transform_line(line, start, end, new_word):

    list_look = line.split(line[start : end],1)
    
    return f"{new_word}".join(list_look)


def preprocessor_test(source_code, keyword_map):
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


exec(preprocessor_test("test_p.py", KEY_MAP))



