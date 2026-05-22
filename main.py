strumento_musicale: str = "basso"
strumento_musicale = []
print (strumento_musicale)


# Riassegnazione della variabile in Python
# Variabile Booleana

online = True
print (online)

# Riassegnazione del Valore
# Booleana → Booleana
online = True
online = False
print (online)

# Stringa → Lista
accesso: str = "negato"
accesso = [1,2,3]
print (accesso)

# Lista → Stringa
band = ["basso", "batteria", "chitarra"]
band: str = "rock band"
print (band)

# Tuple → Stringa
coordinate: tuple = (10,20)
print (coordinate)

coordinate: tuple = (10,20)
coordinate: str = "punto A"
print (coordinate)

# Stessa Variabile, Tipi diversi... DA COMPLETARE!!
dato = "ciao"
dato = 100
dato = True
dato = ["Python", "Java"]
print (dato)

dato: str = "ciao"
dato: int = 100
dato: bool = True
dato: list = []
print (dato)

#----------------------------------------
# Variabili Primitive

# Stringa
nome: str = "Diego"

# Intero
eta: int = 31

# Decimale
altezza: float = 1.70

print (nome)
print (eta)
print (altezza)

#------------------------------------
# Variabili Complesse

# Lista
numeri_primi_minori_di_10: list  = [2,3,5,7]

# Matrice
temperature: list = [
    [18,22,25],    # Temp. Minime Weekend
    [28,31,34]     # Temp. Massime Weekend
]

# Dizionario
candidato: dict = {
    "nome": "Diego",     # Stringa
    "eta": 29,            # Intero
    "musicista": True    # Booleano
}

print (numeri_primi_minori_di_10)
print (temperature)
print (candidato)


