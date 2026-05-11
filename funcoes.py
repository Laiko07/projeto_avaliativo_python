# funcoes.py

def calcular_upc(upc_atual):

    if upc_atual > 150:
        novo_upc = upc_atual * 1.08

    else:
        novo_upc = upc_atual * 0.96

    return novo_upc


def pegar_menor(valor_atual, menor_valor):

    if valor_atual < menor_valor:
        return valor_atual

    return menor_valor


def classificar_upc(upc, amarela, verde, vermelha):

    if 120 <= upc <= 180:
        verde += 1
        vermelha = 0

    elif upc < 250:
        amarela += 1
        vermelha = 0

    elif upc >= 250:
        vermelha += 1

    return amarela, verde, vermelha


def calcular_media(total, quantidade):

    return total / quantidade


def calcular_porcentagem(realizadas, total):

    return (realizadas / total) * 100


def mostrar_resultados(
    media,
    menor_upc,
    zona_verde,
    porcentagem,
    porc_verde
):

    print("\n" + "-"*100)

    print("\n\tRESULTADO DAS LEITURAS DA REFINARIA:\n")

    print(f"\tMédia das pressões: {media:.2f}")

    print(f"\tMenor UPC registrada: {menor_upc:.2f}")

    print(f"\tTotal de zonas verdes: {zona_verde}")

    print(f"\tPorcentagem em zona verde: {porc_verde:.2f}%")

    if porcentagem != 100:
        print(f"\tLeituras realizadas: {porcentagem:.2f}%")

    print("\n" + "-"*100)
