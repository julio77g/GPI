# Bayardo Guerrero
# importar librerias para expresiones regulares y manejo de archivos
import re 
import fileinput
# Descripcion
#
# Input : Archivo de entrada de datos en la carpeta data archivo imput_1.txt
#
# Output : Muestra en la consola los resultados solicitados en el pdf
 # Creamos la clase principal con ubjeto como parametro
class RomanNum(object):

    def get_roman_num(self, RomanStr): #creamos la funcion
        # Descripcion : recibimos la cadena de simbolos(num Romanos y devolvemos el valor correspondiente) 
        #
        # Input :cadena de numeros romanos
        #
        # Output : cadena de valores numericos
        if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'\
        , RomanStr) != None:
            NumDic = {"pattern":"", "retNum":0}#asignamos a un diccionario la clave y el valor
            RomanPattern = {  
                "0":('', '', '', 'M'),             #          1000
                "1":('CM', 'CD', 'D', 'C', 100), #900 400 500 100
                "2":('XC', 'XL', 'L', 'X', 10), #90 40 50 10
                "3":('IX', 'IV', 'V', 'I', 1)#9 4 5 1
                }
            i = 3
            NumItems = sorted(RomanPattern.items())#ordena el diccionario para devolver la tupla

            for RomanItem in NumItems:
                if RomanItem[0] != '0':# verifica valores M o de mil
                    PatStr = NumDic["pattern"].join(['', RomanItem[1][0]])
                    if re.search(PatStr, RomanStr) != None:
                        #Determinamos si la cadena de num romanos tiene una secuencia valida
                        NumDic["retNum"] += 9*RomanItem[1][4]
                        NumDic["pattern"] = PatStr
                    else:
                        PatStr = NumDic["pattern"].join(['', RomanItem[1][1]])
                        if re.search(PatStr, RomanStr) != None:
                            NumDic["retNum"] += 4*RomanItem[1][4]
                            NumDic["pattern"] = PatStr
                        else:
                            PatStr = NumDic["pattern"].\
                            join(['', RomanItem[1][2]])
                            if re.search(PatStr, RomanStr) != None:
                                NumDic["retNum"] += 5*RomanItem[1][4]
                                NumDic["pattern"] = PatStr

                if NumDic["pattern"] == '':
                    NumDic["pattern"] = '^'
                TempStr = ''
                Sum = 0
                for k in range(0, 4):
                    pstr = RomanItem[1][3].\
                    join(['', '{']).join(['', str(k)]).join(['', '}'])
                    PatStr = NumDic["pattern"].join(['', pstr])
                    if re.search(PatStr, RomanStr) != None:
                        Sum = k*(10**i)
                        TempStr = PatStr
                if TempStr != '':
                    NumDic["pattern"] = TempStr
                else:
                    NumDic["pattern"] = PatStr
                NumDic['retNum'] += Sum
                i -= 1

            return NumDic['retNum']
        else:
            print ('La cadena no es un número romano válido.')

    def str_resolve(self, InputLine):# funcion para leer archivo de entrada
        
        RomanArray = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        if InputLine[-1] in RomanArray:
            InputLine_array = InputLine.split(' ')
            WordDic[InputLine_array[0]] = InputLine_array[2]
            return
        elif InputLine[-1] == 's':
            InputLine_array = InputLine.split(' ')
            TempStr = ''
            for i in range(len(InputLine_array)-4):
                TempStr += WordDic[InputLine_array[i]]
            TempNum = self.get_roman_num(TempStr)
            CoinDic[InputLine_array[-4]] = \
            int(InputLine_array[-2])/int(TempNum)
            return
        elif InputLine[-1] == '?':
            InputLine_array = InputLine.split(' ')
            if InputLine_array[1] == 'much':
                TempStr1 = ''
                TempStr3 = ''
                for i in range(3, len(InputLine_array)-1):
                    TempStr3 += InputLine_array[i]+' '
                    TempStr1 += WordDic[InputLine_array[i]]
                return TempStr3+"is "+str(self.get_roman_num(TempStr1))
            elif InputLine_array[1] == 'many':
                TempStr2 = ''
                TempStr4 = ''
                for i in range(4, len(InputLine_array)-2):
                    TempStr4 += InputLine_array[i]+' '
                    TempStr2 += WordDic[InputLine_array[i]]
                return TempStr4+InputLine_array[-2]+' is '\
                + str(CoinDic[InputLine_array[-2]]*\
                self.get_roman_num(TempStr2)) + ' Credits'

if __name__ == "__main__":

    WordDic = {}#Definimos un diccionario para texto y num romanos
    CoinDic = {}#Diccionario para valor de las monedas

    for Line in fileinput.input("../test/input_1.txt"):
        StrLine = Line[:-1]#eliminamos el salto de linea del final del archivo
        try:
            Roma = RomanNum()
            str_return = Roma.str_resolve(StrLine)
            if str_return:
                print (str_return)
        except:
            print ("I have no idea what you are talking about")
