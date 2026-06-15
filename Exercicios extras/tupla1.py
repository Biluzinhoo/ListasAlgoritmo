def aprovados(alunos):
    aluno_aprovado = []
    for nome, nota in alunos:
        if nota >= 7:
            aluno_aprovado.append(nome)
    return aluno_aprovado

def main():
    alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)]
    print(aprovados(alunos))

main()