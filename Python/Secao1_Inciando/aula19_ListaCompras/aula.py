lista_compras = []
sair = False
opcao = ''
add_item = ''
while sair == False:
    print("\n" + "=" * 75 + "\n")
    
    print('Selecione uma opçpão: \n')
    opcao = input('[i] Inserir  [a] Apagar [l] Listar [s] Sair: ').lower()
    print("\n" + "=" * 75 + "\n")
    if opcao == 'i':
        add_item = input('Insira um item na lista: ')
        lista_compras.append(add_item)
    elif opcao == 'a':
        ind_apagar = input('Insira o indice o Item que deseja apagar: ')
        if int(ind_apagar) <= len(lista_compras):
            del lista_compras[int(ind_apagar) - 1]
            print('Item removido com sucesso!!')
        
        else:
            print('Item não consta na Lista!!')
    elif opcao == 'l':
        print('Id  -- Item')
        if len(lista_compras) > 0:
            for indice, item in enumerate(lista_compras):
                print(f'{indice + 1}   -- {item}')
        else:
            print('Lista vazia, favor inserir items!!!')
    elif opcao == 's':
        sair = True
        print('Até logo!')
        print("\n" + "=" * 75 + "\n")
    else:
        print('Opção inválida, tente novamente!!!')