def aprovado(notas):
    media = sum(notas)/len(notas)
    return media  

def main():
    notas = []
    while True: 
        nota = input("Escreva suas notas: ")
        if nota == "":
            break
        notas.append(float(nota))
    if aprovado(notas) > 7:
        print("Aprovado")
    elif aprovado(notas) == 7:
        print("Na média")
    else:
        print("Está abaixo da média")
main()
    