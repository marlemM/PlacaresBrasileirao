campeonato = {}

while True:
    rodada = input("Insira a rodada (ou 'nada' para parar): ")
    if rodada.lower() == 'nada':
        break

    ano = input("Insira o ano do Campeonato Brasileiro: ")

    if ano not in campeonato:
        campeonato[ano] = {}

    placares = []
    while True:
        placar = input(f"Insira um placar para a rodada {rodada} do ano {ano} (ou 'nada' para parar): ")
        if placar.lower() == 'nada':
            break
        placares.append(placar)

    campeonato[ano][rodada] = placares

if len(campeonato) > 0:
    placares_geral = []

    with open("placares.txt", "w") as file:
        for ano, rodadas in campeonato.items():
            for rodada, placares in rodadas.items():
                placares_rodada = {}

                for placar in placares:
                    placares_rodada[placar] = placares_rodada.get(placar, 0) + 1

                placares_ordenados = sorted(placares_rodada.items(), key=lambda x: x[1], reverse=True)
                placar_mais_comum_rodada = placares_ordenados[0][0]

                print(f"Placar mais comum na rodada {rodada} do ano {ano}: {placar_mais_comum_rodada}")

                file.write(f"Rodada {rodada} do ano {ano}: Placar mais comum: {placar_mais_comum_rodada}\n")

                placares_geral.extend(placares)

        placares_geral_contagem = {}
        for placar in placares_geral:
            placares_geral_contagem[placar] = placares_geral_contagem.get(placar, 0) + 1

        placares_geral_ordenados = sorted(placares_geral_contagem.items(), key=lambda x: x[1], reverse=True)
        placar_mais_comum_geral = placares_geral_ordenados[0][0]

        print(f"\nPlacar mais comum no geral: {placar_mais_comum_geral}")

        file.write(f"Placar mais comum no geral: {placar_mais_comum_geral}\n")

else:
    print("Nenhuma rodada foi inserida.")
