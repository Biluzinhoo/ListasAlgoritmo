def anagrama_frases(frase1, frase2):
    def limpar(frase):
        return sorted(c for c in frase.lower() if c.isalpha())

    return limpar(frase1) == limpar(frase2)

def main():
    f1 = "William Shakespeare"
    f2 = "I am a weakish speller"
    print(anagrama_frases(f1, f2))          

    f3 = "Slot machines"
    f4 = "Cash lost in me"
    print(anagrama_frases(f3, f4))         

    f5 = "Python é legal"
    f6 = "Java é melhor"
    print(anagrama_frases(f5, f6))         

main()