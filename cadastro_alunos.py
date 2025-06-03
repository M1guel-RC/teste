def classificar_nota(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota >= 5:
        return "Regular"
    else:
        return "Insuficiente"

def main():
    alunos = {}

    while True:
        nome = input("Digite o nome do aluno: ").strip()
        try:
            nota = float(input(f"Digite a nota do(a) {nome}: "))
        except ValueError:
            print("Nota inválida! Tenta de novo com um número, beleza?")
            continue

        alunos[nome] = nota

        continuar = input("Quer cadastrar outro aluno? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\n--- Lista de Alunos e Classificações ---")
    for nome, nota in alunos.items():
        classificacao = classificar_nota(nota)
        print(f"{nome} - Nota: {nota} - Desempenho: {classificacao}")

if __name__ == "__main__":
    main()
