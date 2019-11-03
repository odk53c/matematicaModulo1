# Create by ODK53C


casas_70m2 = 650
casas_110m2 = 820
ap_65m2 = 550
ap_90m2 = 750

qt_casas_70m2 = int(input('Quantas casas de 70m² estão alugadas este mês ? '))
qt_casas_110m2 = int(input('Quantas casas de 110m² estão alugadas este mês ? '))
qt_ap_65m2 = int(input('Quantos apartamentos de 65m² estão alugados este mês ? '))
qt_ap_90m2 = int(input('Quantas apartamentos de 90m² estão alugados este mês ? '))

total_casas_70m2 = casas_70m2 * qt_casas_70m2
total_casas_110m2 = casas_110m2 * qt_casas_110m2
total_ap_65m2 = ap_65m2 * qt_ap_65m2
total_ap_90m2 = ap_90m2 * qt_ap_90m2

total_rec_alugueis = total_casas_70m2 + total_casas_110m2 + total_ap_65m2 + total_ap_90m2

salario_funcionarios = float(input('Qual é o valor total dos salarios dos funcionarios ? '))
despesas_de_aluguel_de_espaco = float(input('Digite o valor do total dos custos de aluguel de espaço:  '))
despesas_equip_escritorio = float(input('Digite o valor das despesas com equipamentos de escritorio: '))
porcentagem = float(input('Quantos por cento gostaria de guardar para a reserva de emergencia? '))
reserva_de_emergencia = (total_rec_alugueis * porcentagem) / 100

fechamento_mes = (total_rec_alugueis - despesas_equip_escritorio - despesas_de_aluguel_de_espaco - salario_funcionarios - reserva_de_emergencia)


resultado = ('Este mês a imobiliaria possui alugadas {} casas de 70m², {} casas de 110m², {} apartamentos de 65m² e '
             '{} apartamentos de 90m². Total recebido dos alugueis {}, foi separado {} para a reserva de emergencia,'
             ' \nas despesas com equipamentos de escritorio ficou no valor de {} e os salarios dos funcionarios {}.'
             '\nApós pagar os funcionarios, as despesas e separar para reserva de emergencia {}% a empresa ficou com {} '.format(qt_casas_70m2, qt_casas_110m2, qt_ap_65m2, qt_ap_90m2,
                                                                                                                                 total_rec_alugueis,reserva_de_emergencia, despesas_equip_escritorio, salario_funcionarios, porcentagem, fechamento_mes))
print(resultado)