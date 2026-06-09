def anagrama(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

def main():
    print(anagrama("amor", "roma"))       
    print(anagrama("Listen", "Silent"))    
    print(anagrama("python", "java"))      
    print(anagrama("aab", "abb"))          

main()