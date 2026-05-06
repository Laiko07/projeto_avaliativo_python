import funcoes as f

print("\nBem-vindo ao sistema da Refinaria Delta-9")

total_leituras = int(input("Informe o total de leituras que serão feitas no turno: "))

verde = 0
amarela = 0
vermelha = 0
menor_valor = 400
leituras_feitas = 0
soma = 0

while total_leituras <= 0:
    print("Valor inválido, tente novamente.")
    total_leituras = int(input("\nInforme o total de leituras: "))

print("\n" + "-"*100)

for i in range(total_leituras):
    
    if vermelha != 2:
        valor_atual = float(input(f"\nLeitura {i+1} - Digite a pressão: "))

        valor_novo = f.calcular_upc(valor_atual)
        menor_valor = f.pegar_menor(valor_novo, menor_valor)

        if valor_novo > 120:
            soma += valor_novo
            amarela, verde, vermelha = f.classificar_upc(valor_novo, amarela, verde, vermelha)
        
        else:
            print("\n" + "-"*100)
            print("\nERRO DETECTADO:")
            print("Fluido cristalizado devido à baixa pressão. Escoamento interrompido.")
            
            leituras_feitas += 1
            break
    
    if vermelha == 2:
        print("\n" + "-"*100)
        print("\nERRO DETECTADO:")
        print("Alta pressão detectada. Sistema interrompido por segurança.")
        break

    leituras_feitas += 1


porc = f.calcular_porcentagem(leituras_feitas, total_leituras)
media = f.calcular_media(soma, leituras_feitas)

f.mostrar_resultados(media, menor_valor, verde, porc)

input("\nPressione ENTER para encerrar...")
