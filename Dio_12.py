# Desafio DIO - Banco 1.0

# Variáveis
deposito = 0
saldo = 0
saque = 0
extrato_deposito = ''
deposito_vazio = '\nNão contém depósitos'
extrato_saque = ''
saque_vazio = '\nNão contém saques'
qtd_saque = 3

# Ciclo principal
while True:
    # Apresentação de Menu
    try:
        menu = int(input(f"""
..............................
$          Banco DIO         $
..............................
1 - Depósito
2 - Saque
3 - Extrato
4 - Encerrar
Opção: """))

        if menu < 1 or menu > 4:
            raise ValueError
    except:
        print('Opção inválida. Tente novamente.')

    # Opções do menu
    else:

        # Opção de Deposito
        if menu == 1:

            try:
                deposito = float(input("""
..............................
$   Banco DIO - Deposito     $
..............................
Valor a ser depositado: R$: """))

                # Condicionais de deposito
                if deposito < 0:
                    raise Exception
            
            except ValueError:
                print('\nErro na operação.\nEncerrando operação.')
                continuar = input('Tecle enter para continuar:')
            
            except Exception:
                print('\nErro na operação.\nValor indicado é negativo.')
                continuar = input('Tecle enter para continuar:')

            else:
                extrato_deposito += f'\nDeposito: R${deposito:.2f}'
                saldo += deposito

                print()
                print(f'Deposito realizado com sucesso.\nValor depositado: R${deposito:.2f}')
                print(f'Saldo atual: R${saldo:.2f}')
                print()
                continuar = input('Tecle enter para continuar:')
        
        # Opção de Saque
        elif menu == 2:
            try:
                saque = int(input("""
..............................
$     Banco DIO - Saque      $
..............................
Valor de saque: R$: """))

                # Condicionais de saque
                if qtd_saque == 0:
                    raise Exception

                if saque > 500:
                    raise Exception
                
                if saque > saldo:
                    raise Exception

            except ValueError:
                print('\nErro na operação.\nEncerrando operação.')
                
                continuar = input('Tecle enter para continuar:')

            except Exception:
                if qtd_saque == 0:
                    print('\nErro na operação.\nLimite de saques alcançados.')
                elif saque > 500:
                    print('\nErro na operação.\nLimite por saque de R$500,00')
                elif saque > saldo:
                    print('\nErro na operação.\nSaldo insuficiente.')
                
                continuar = input('Tecle enter para continuar:')
            
            else:
                extrato_saque += f'\nSaque: R${saque:.2f}'
                saldo -= saque
                qtd_saque -= 1

                print()
                print(f'Saque realizado com sucesso.\nValor Sacado: R${saque:.2f}')
                print(f'Saldo atual: R${saldo:.2f}')
                print()
                continuar = input('Tecle enter para continuar:')
                

        # Opção de Extrato
        elif menu == 3:
            print(f"""
..............................
$    Banco DIO - Extrato     $
..............................

Valores depositados: {deposito_vazio if not extrato_deposito else extrato_deposito}
------------------------------
Valores sacados: {saque_vazio if not extrato_saque else extrato_saque}
------------------------------
Saldo em conta: R${saldo:.2f}
                  """)
            continuar = input('Tecle enter para continuar:')
        
        # Opção de encerramento do programa
        elif menu == 4:
            print(f"""
..............................
$   Banco DIO - Encerrando   $
..............................
""")
            print('Programa encerrado')
            break