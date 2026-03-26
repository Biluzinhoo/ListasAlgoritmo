matricula = int(input("Informe sua matrícula no formato AASDDD: "))

ano = matricula // 10000
semestre = (matricula % 10000) // 1000


if semestre not in (1, 2):
    print("Erro: semestre inválido! Deve ser 1 ou 2.")
else:
    print(f"Ano: {ano:02d}")
    print(f"Semestre: {semestre}")

