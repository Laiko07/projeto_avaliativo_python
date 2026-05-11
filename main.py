# main.py

import funcoes as f

print("\nBem-vindo ao sistema da Refinaria Delta-9")

total_leituras = int(input("Informe o total de leituras que serão feitas no turno: "))

while total_leituras <= 0:
    print("Valor inválido, tente novamente.")
    total_leituras = int(input("Informe o total de leituras: "))

verde = 0
amarela = 0
vermelha = 0

menor_valor = 999999
leituras_feitas = 0
soma = 0

print("\n" + "-"*100)

for i in range(total_leituras):

    valor_atual = float(input(f"\nLeitura {i+1} - Digite a pressão: "))

    valor_novo = f.calcular_upc(valor_atual)

    print(f"UPC ajustada: {valor_novo:.2f}")

    soma += valor_novo

    menor_valor = f.pegar_menor(valor_novo, menor_valor)

    amarela, verde, vermelha = f.classificar_upc(
        valor_novo,
        amarela,
        verde,
        vermelha
    )

    leituras_feitas += 1

    if vermelha == 2:
        print("\n" + "-"*100)
        print("\nERRO DETECTADO:")
        print("Duas leituras consecutivas na Zona Vermelha.")
        print("Escoamento interrompido por segurança.")
        break

media = f.calcular_media(soma, leituras_feitas)

porc_realizadas = f.calcular_porcentagem(
    leituras_feitas,
    total_leituras
)

porc_verde = f.calcular_porcentagem(
    verde,
    leituras_feitas
)

f.mostrar_resultados(
    media,
    menor_valor,
    verde,
    porc_realizadas,
    porc_verde
)

input("\nPressione ENTER para encerrar...")
