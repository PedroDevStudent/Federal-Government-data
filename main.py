#Importar pandas e "muda" o nome para pd
import pandas as pd

#Usado para verificar e não permitir a execução de um comando main, caso importado de 'pandas' 
if __name__ == '__main__': 
    
    #Coleta de todos os dados a serem analizados e armazenar em variáveis para facilitar a escrita do código
    Url2022=(r"despesas2022.csv")
    Url2018=(r"despesas2018.csv")
    Url2019=(r"despesas2019.csv")
    Url2020=(r"despesas2020.csv")
    Url2021=(r"despesas2021.csv")
    
    #Leitura dos arquivos csv pelo pandas, e armazenamento das mesmas em variáveis fixas
    Eco2022=pd.read_csv(Url2022, sep=";", decimal=",")
    Eco2021=pd.read_csv(Url2021, sep=";", decimal=",")
    Eco2020=pd.read_csv(Url2020, sep=";", decimal=",")
    Eco2019=pd.read_csv(Url2019, sep=";", decimal=",")
    
    #Função Menu, responsável por mostrar ao usúario todas as possíbilidades de programa para o usuário
    def menu():
        print("""   
                                            Menu Principal
                    0 - Sair do programa
                    1 - Valores pagos, empenhados e líquidos do ano de 2022
                    2 - Valores pagos, empenhados e líquidos do ano de 2021
                    3 - Valores pagos, empenhados e líquidos do ano de 2020
                    4 - Valores pagos, empenhados e líquidos do ano de 2019
                    5 - Quantidade de contratos anuais por gestão""")
    
    #Função para calcular a soma dos Valores Pagos
    def calculateSumValorPago(y):
        soma=0
        for i in range(len(Eco2022['Valor Pago'])):
            Num=float(y['Valor Pago'][i].replace(".", "").replace(",",".").replace("-",""))
            soma+=Num
        soma=round(soma,2)
        soma=format(soma).replace(".",",")
        return soma

    #Função para calcular a soma dos Valores Empenhados
    def calculateSumValorEmpenhado(y):
        soma=0
        for i in range(len(Eco2022['Valor Empenhado'])):
            Num=float(y['Valor Empenhado'][i].replace(".", "").replace(",",".").replace("-",""))
            soma+=Num
        soma=round(soma,2)
        soma=format(soma).replace(".",",")
        return soma
    
    def calculateSumValorLiquidado(y):
        soma=0
        for i in range(len(Eco2022['Valor Liquidado'])):
            Num=float(y['Valor Liquidado'][i].replace(".", "").replace(",",".").replace("-",""))
            soma+=Num
        soma=round(soma,2)
        soma=format(soma).replace(".",",")
        return soma
    
    #Chamar a função e coletar a opção
    menu()
    option=int(input("Insira uma opção!  "))
    
    #Condições do menu
    while( option != 0):
        if(option==1):
            print(f'O valor Empenhado no ano de 2022 é de: R$ {calculateSumValorEmpenhado(Eco2022)}')
            print(f'O valor Pago no ano de 2022 é de: R$ {calculateSumValorPago(Eco2022)}')
            print(f'O valor Liquidado no ano de 2022 é de: R$ {calculateSumValorLiquidado(Eco2022)}')
            
        elif(option==2):
            print(f'O valor Empenhado no ano de 2022 é de: R$ {calculateSumValorEmpenhado(Eco2021)}')
            print(f'O valor Pago no ano de 2022 é de: R$ {calculateSumValorPago(Eco2021)}')
            print(f'O valor Liquidado no ano de 2022 é de: R$ {calculateSumValorLiquidado(Eco2021)}')
        
        elif(option==3):
            print(f'O valor Empenhado no ano de 2022 é de: R$ {calculateSumValorEmpenhado(Eco2020)}')
            print(f'O valor Pago no ano de 2022 é de: R$ {calculateSumValorPago(Eco2020)}')
            print(f'O valor Liquidado no ano de 2022 é de: R$ {calculateSumValorLiquidado(Eco2020)}')
        
        elif(option==4):
            print(f'O valor Empenhado no ano de 2022 é de: R$ {calculateSumValorEmpenhado(Eco2019)}')
            print(f'O valor Pago no ano de 2022 é de: R$ {calculateSumValorPago(Eco2019)}')
            print(f'O valor Liquidado no ano de 2022 é de: R$ {calculateSumValorLiquidado(Eco2019)}')
        
        elif(option==5):
            print(f"No ano de 2022, foram realizados {len(Eco2022)} contratos")
            print(f"No ano de 2021, foram realizados {len(Eco2021)} contratos")
            print(f"No ano de 2020, foram realizados {len(Eco2020)} contratos")
            print(f"No ano de 2019, foram realizados {len(Eco2019)} contratos")
            print(f'E o total de contratos na gestão foi: {len(Eco2022)+len(Eco2021)+len(Eco2020)+len(Eco2019)}')
        else:
            print('[ERRO] por favor insira uma opção valida! ')
        
        #Retorna a função menu, novamente
        menu()
        option=int(input("Insira uma opção!  "))
    
    print('Obrigado! ')
    exit()
