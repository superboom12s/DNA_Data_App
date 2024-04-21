
protCD = (["UUU", "UUC"], ["UUA", "UUG"], ["UCU", "UCC", "UCA", "UCG"], ["UAU", "UAC"], ["UAA", "UAG"], ["UGU", "UGC"], ["UGA"], ["UGG"], ["CUU", "CUC", "CUA", "CUG"], ["CCU", "CCC", "CCA", "CCG"], ["CAU", "CAC"], ["CAA", "CAG"], ["CGU", "CGC", "CGA", "CGG"], ["AUU", "AUC", "AUA"], ["AUG"], ["ACU", "ACC", "ACA", "ACG"], ["AAU", "AAC"], ["AAA", "AAG"], ["AGU", "AGC"], ["AGA", "AGG"], ["GUU", "GUC", "GUA", "GUG"], ["GCU", "GCC", "GCA", "GCG"], ["GAU", "GAC"], ["GAA", "GAG"], ["GGU", "GGC", "GGA", "GGG"])
protRS = ("Phe", "Leu", "Ser", "Tyr", "Alto", "Cys", "Alto", "Trp", "Leu", "Pro", "His", "Gln", "Arg", "Ile", "Met", "Thr", "Asn", "Lys", "Ser", "Arg", "Val", "Ala", "Asp", "Glu", "Gly")

def corregir(texto):
    #elimina los espacios

    texto2 = list(texto)
    while texto.find(" ") != -1:
        texto2.pop(texto.find(" "))
        texto = ''.join(texto2)

    return texto.upper()

def trans(texto):

    def obtenerPosicionCaracter(caracter, codigo):
        return codigo.index(caracter)

    texto = corregir(texto)

    ADN1 = 'ATGC-UACG'
    ADN2 = 'UACG-ATGC'

    try:
        texto = texto.upper()
        Ftext = []
        for symbol in range(len(texto)):
            Ftext.append(ADN2[obtenerPosicionCaracter(texto[symbol], ADN1)])
        return ''.join(Ftext)

    except:
        print("Error introduciendo el tipo de valor")
        return "Error"

def dividirEnTres(texto):
    #divide la entrada en una lista de tres en tres caracteres
    texto = corregir(texto)
    resultado = [texto[i:i + 3] for i in range(0, len(texto), 3)]
    return resultado

def encontrarProt(texto):

    ARN_texto = dividirEnTres(tipo(texto, "ARNm"))
    ARN_texto = ARN_texto[0]

    for i in range(len(protRS)):
        if ARN_texto in protCD[i]:
            return protRS[i]
            break

    return "Ninguna"

def proteinList(texto):
    texto = corregir(texto)

    ARN_List = dividirEnTres(tipo(texto, "ARNm"))

    proteinas = []

    for ARN in ARN_List:
        proteinas.append(encontrarProt(ARN))

    return ' '.join(proteinas)

def tipo(texto, darTipo="tipo"):

    texto = corregir(texto)

    if texto.find("U") != -1:
        if darTipo == "tipo":
            return "ARNm"
        elif darTipo == "ADN":
            return trans(texto)
        else:
            return texto

    else:
        if darTipo == "tipo":
            return "ADN"
        elif darTipo == "ARNm":
            return trans(texto)
        else:
            return texto

def encontrarCodigo(texto):
    if texto in protRS:
        iter = 0
        for valor in protRS:
            if valor == texto:
                return ' '.join(protCD[iter])
                break
            else:
                iter += 1
    else:
        return "Ninguno"

def codigoList(texto, tipo="ADN"):

    codeList = texto.split(" ")
    codigos = []

    for prot in codeList:
        codigos.append(encontrarCodigo(prot))

    if tipo == "ARNm":
        return ' '.join(codigos)
    else:
        return trans(''.join(codigos))

def Datos(texto):
    print("Tipo:", tipo(texto))
    print("---------------------------------------------")
    print("ADN: ", tipo(texto, "ADN"))
    print("ARNm:", tipo(texto, "ARNm"))
    print("---------------------------------------------")
    print("\nProteinas correspondientes:", proteinList(texto))
    print("\n///////////////////////////////////////////\n")
    return ""



def ayuda():
    print("Ver. 1.0.0"
          "trans(Codigo) -> Si el valor introducido es ADN lo transforma a ARNm y viceversa"
          "dividirEnTres(Codigo) -> Divide en bloques un codigo de ADN o ARNm. Devuelve una lista."
          "encontrarProt(Codigo) -> Encuentra UNA proteina de un bloque de codigo (se convierte"
          "                         a ARNm de forma automatica)."
          "proteinList(Codigo) -> Transforma una tira de ADN (o varios ARNm en una sola tira) en"
          "                       todas las proteinas que contiene esa informacion."
          "tipo(Codigo, tipo[opcional]) -> Comprueba si el valor introducido es ADN o ARNm"
          "                                En caso de tener una segunda entrada traduce el codigo"
          "                                en un tipo especifico indicado por la segunda entrada."
          "                                Si no se puede determinar el tipo, devolvera ADN por defecto."
          "encontrarCodigo(Proteina) -> Indica el/los codigo(s) necesario(s) para obtener una proteina"
          "                             especifica (ARNm)."
          "codigoList(Proteinas, tipo[opcional]) -> Hace una lista del ADN necesario para obtener unas"
          "                                         proteinas especificas.\n"
          "                                         El tipo (opcional), por defecto es ADN, aunque se"
          "                                         puede seleccionar ARNm. En caso de ser ARNm, el"
          "                                         resultado viene separado por espacios."
          "Datos(Codigo) -> indica todos los datos de el codigo en la terminal")

def help():
    ayuda()

print(proteinList("AAATTa"))