####para leer los json de los archivos de texto y escribirlos###
import json
import re

#shameless copy paste from json/decoder.py
FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)

class ConcatJSONDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        s_len = len(s)

        objs = []
        end = 0
        while end != s_len:
            obj, end = self.raw_decode(s, idx=_w(s, end).end())
            end = _w(s, end).end()
            objs.append(obj)
        return objs

###############################################

###funcion para leer un json de un archivo
def Readjsonfile(jsonfile):
    configjson = json.load(open(jsonfile), cls=ConcatJSONDecoder)
    return(configjson)

###funcion para guardar un json en un archivo
def Writejsonfile(jsonfile,jsondata):
    #######borra el archivo antes de escribirle####
    open(jsonfile, 'w').close()
    #####lo guarda en un archivo diferente##########
    with open(jsonfile, 'w') as fp:
        json.dump(jsondata, fp)

