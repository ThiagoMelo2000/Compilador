def declaracao(linha):
    
    reservada = ['int', 'float', 'char']
    block = ['for', 'if', 'scanf', 'printf']
    simbolos = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']
    tamanho = len(linha)
    controlador = 0
    
    if(linha[0] in reservada):
        
        if(linha[2] == ';'):
            
            if(linha[1] not in reservada and linha[1] not in simbolos):
                
                controlador = 1
                
            else:
                
                return 1
            
        if(linha[1] in reservada or linha[1] in simbolos):
            
            return 1
            
        if(linha[tamanho-1] != ';'):
            
            return 1
        
        else:
            
            controlador = 1
            
    if(controlador == 1):
        
        variaveis.append(linha[1])
            
    elif(linha[0] in block):
        
        return 0
    
    elif(linha[0] in variaveis):
        
        return 0
    
    elif(linha[0] == '}'):
        
        return 0
    
    else:
        
        return 1
        

def atribuicao(linha):
    
    reservada = ['int', 'float', 'char', 'for', 'if', 'scanf', 'printf']
    simbolos = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']
    operadores = ['+', '-', '*', '/']
    tamanho = len(linha)
    controle = 0
    
    if(linha[0] in variaveis):
        
        if(linha[tamanho-1] == ';'):
        
            if(linha[1] == '='):
                
                controle = 1
                
    if(linha[0] in reservada and linha[1] == '='):
        
        return 1
    
    if(linha[0] == '}'):
        
        return 0
    
    if(linha[1] == '=' and linha[0] not in reservada and linha[0] not in variaveis):
        
        return 1
                
    if(controle == 1):
        
        for i in range(2, tamanho-1):
                    
            if(i % 2 == 0):
                
                if(linha[i] not in reservada and linha[i] not in simbolos):
                    
                    # -----------------------------------------------------------
                    # Fazer a conversão para outra linguagem
                    # -----------------------------------------------------------
                    ...
                    
                else:
                    
                    return 1
                
            elif(i % 2 != 0):
                
                if(linha[i] in operadores):
                    
                    # -----------------------------------------------------------
                    # Fazer a conversão para outra linguagem
                    # -----------------------------------------------------------
                    ...
                    
                else:
                    
                    return 1
                
       
def leitura(linha):
    
    tipo_leitura = ['%d', '%c', '%f']
    tamanho = len(linha)
    controle = 0
    posicao = 0
    controle2 = 0
    controle3 = 0
    
    if(linha[0] == 'scanf'):
        
        if(linha[1] == '(' and linha[2] == '"' and linha[4] == '"' and linha[5] == ',' and 
           linha[6] == '&' and linha[8] == ')' and linha[9] == ';'):
            
            if(linha[3] in tipo_leitura):
                
                if(linha[7] in variaveis):
                    
                    ...
                    
                else:
                    
                    return 1
                
            else:
            
                return 1
                
        else:
            
            return 1
        
    if(linha[0] == 'printf'):
        
        if(linha[1] == '(' and linha[2] == '"' and linha[tamanho-2] == ')' and linha[tamanho-1] == ';'):
            
            for i in range(3, tamanho-1):
                
                if(linha[i] == '"'):
                    
                    posicao = i
                    break
                
                if(linha[i] in tipo_leitura):
                    
                    controle = 1
                    
            if(controle == 1):
                    
                for i in range(posicao + 1, tamanho-2):
                    
                    if(controle2 == 0):
                        
                        if(linha[i] == ','):
                                                        
                            controle2 = 1
                            controle3 = 1
                            
                        else:
                            
                            return 1
                    
                    elif(controle3 == 1):
                        
                        
                        controle3 = 0
                        
                        if(linha[i] in variaveis):
                            
                            controle2 = 0
                            
                        else:
                            
                            return 1
                    
        else:
            
            return 1
        
             
def condicional(linha, contador_if):
    
    simbolos_1 = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']
    reservada = ['int', 'float', 'char']
    simbolos = ['==', '>=', '<=', '!=']
    operador = ['&&', '||']
    controlador = 0
    
    tamanho = len(linha)
    if(linha[0] == 'if'):
        
        contador_if = 1
        
        if(linha[1] == '(' and linha[tamanho-2] == ')' and linha[tamanho-1] == '{'):
                        
            for i in range(2, tamanho-2):
                                
                if(linha[2] in variaveis):
                    
                    if(controlador == 0):
                                        
                        if(linha[i] in variaveis):
                            
                            controlador += 1
                            
                        else:
                            
                            return 1
                            
                    elif(controlador == 1):
                        
                        if(linha[i] in simbolos):
                            
                            controlador += 1
                            
                        else:
                            
                           return 1
                        
                    elif(controlador == 2):
                        
                        if(linha[i] in variaveis):
                            
                            controlador += 1
                            
                        if(linha[i] in reservada):
                            
                           return 1
                       
                        if(linha[i] in simbolos_1):
                            
                            return 1
                        
                        if(linha[i] not in simbolos):
                            
                            if(linha[i] not in operador):
                                
                                if(linha[i] not in reservada):
                                    
                                    if(linha[i] not in variaveis):
                            
                                        controlador += 1
                               
                    elif(controlador == 3):
                        
                        if(linha[i] in operador):
                            
                            controlador = 0
                            
                        else:
                            
                            return 1

                if(linha[2] not in variaveis):
                    
                    return 1
            
def repeticao(linha):
    
    proibido = ['int', 'float', 'char', '.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ', '==', '>=', '<=', '!=']
    cont_for = ['++', '--']
    simbolos_for = ['>=', '<=', '<', '>', '=']
    
    if(linha[0] == 'for'):
        
        if(len(linha) < 12):
            
            return 1
        
        if(linha[1] == '(' and linha[12] == ')' and linha[13] == '{'):
            
            if(linha[2] in variaveis and linha[6] == linha[2] and linha[10] == linha[2]):
                
                if(linha[3] == '=' and linha[7] in simbolos_for):
                    
                    if(linha[4] not in proibido and linha[8] not in proibido):
                        
                        if(linha[4] in variaveis or linha[4].isnumeric()):
                            
                            if(linha[8] in variaveis or linha[8].isnumeric()):
                        
                                if(linha[5] == ';' and linha[9] == ';'):
                            
                                    if(linha[11] in cont_for):
                                        
                                        ...
                                        
                                    else:
                                        
                                        return 1
                                    
                                else:
                                        
                                    return 1
                                
                            else:
                                    
                                    return 1
                                
                        else:
                                
                            return 1
                            
                    else:
                                
                        return 1
                        
                else:
                            
                    return 1
                    
            else:
                                
                return 1
                
        else:
                                
            return 1
    

texto = open('file.txt', 'r')
linhas = texto.readlines()

contador_if = 0
global variaveis
variaveis = list()

for linha in linhas:
    
    linha = linha.split()
    ret_declaracao = declaracao(linha)
    ret_atrib = atribuicao(linha)
    ret_leitura = leitura(linha)
    ret_cond = condicional(linha, contador_if)
    ret_rep = repeticao(linha)
    
    if(ret_declaracao == 1):
        
        print('Erro declaração')
        print(' '.join(linha))
        break
    
    elif(ret_atrib == 1):
        
        print('Erro atribuição')
        print(' '.join(linha))
        break
    
    elif(ret_leitura == 1):
        
        print('Erro leitura')
        print(' '.join(linha))
        break
    
    elif(ret_cond == 1):
        
        print('Erro condição')
        print(' '.join(linha))
        break
    
    elif(ret_rep == 1):
        
        print('Erro repetição')
        print(' '.join(linha))
        break
    
    else:
        pass

proibido = ['%d', '%c', '%f', '&&', '||', '{', 'int', 'float', 'char', 'scanf', '&', '.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ', '==', '>=', '<=', '!=', ';', '"']
tipos = ['int', 'float', 'char', 'double', 'boolean']
concat = []
content = list()

for linha in linhas:
    
    linha = linha.split()
    
    if(ret_declaracao != 1 and ret_atrib != 1 and ret_leitura != 1 and ret_cond != 1 and ret_rep != 1):
        
        if(linha[0] != 'for' and linha[0] != 'if'):
            
            if(linha[0] == 'printf'):
                
                content.append('print')
        
                for i in range(len(linha)):
                        
                    if(linha[i] == '('):
                        
                        content.append("(f'")
                                        
                    elif(linha[i] in variaveis):
                        
                        content.append('{' + linha[i] + '}')
                        
                    elif(linha[i] == ')'):
                        
                        content.append("')")
                        
                    elif(linha[i] not in proibido and linha[i] != 'printf'):
                        
                        content.append(linha[i])
                        
                    elif(linha[i] == ';'):
                        
                        print(''.join(content))
                        content.clear()

                    else:
                        pass
                
            elif(linha[0] in tipos and linha[2] == '='):
                
                for i in range(len(linha)-2):
                    
                    if(linha[i] != ';'):
                    
                        content.append(linha[i+1])
                
                print(' '.join(content))
                content.clear()
                
            elif(linha[0] in variaveis):
                
                for i in range(len(linha)-1):
                    
                    content.append(linha[i])
                
                print(' '.join(content))
                content.clear()
                
            elif(linha[0] == 'scanf'):
                
                content.append(linha[7] + ' = input()')
                
                print(' '.join(content))
                content.clear()
                
        elif(linha[0] == 'for' or linha[0] == 'if'):
            
            if(linha[0] == 'printf'):
                
                content.append('print')
        
                for i in range(len(linha)):
                        
                    if(linha[i] == '('):
                        
                        content.append("(f'")
                                        
                    elif(linha[i] in variaveis):
                        
                        content.append('{' + linha[i] + '}')
                        
                    elif(linha[i] == ')'):
                        
                        content.append("')")
                        
                    elif(linha[i] not in proibido and linha[i] != 'printf'):
                        
                        content.append(linha[i])
                        
                    elif(linha[i] == ';'):
                        
                        print(''.join(content))
                        content.clear()

                    else:
                        pass
                
            elif(linha[0] in tipos and linha[2] == '='):
                
                for i in range(len(linha)-2):
                    
                    if(linha[i] != ';'):
                    
                        content.append(linha[i+1])
                
                print(' '.join(content))
                content.clear()
                
            elif(linha[0] in variaveis):
                
                for i in range(len(linha)-1):
                    
                    content.append(linha[i])
                
                print(' '.join(content))
                content.clear()
                
            elif(linha[0] == 'scanf'):
                
                content.append(linha[7] + ' = input()')
                
                print(' '.join(content))
                content.clear()
                
            elif(linha[0] == 'for'):
                
                content.append('for ')
                
                if(linha[2] in variaveis):
                        
                    content.append(linha[2] + ' in range(' + linha[8] + '):')
                    
                elif(linha[len(linha)-1] == '{'):
                    
                    content.append('\n')
                
                print(''.join(content))
                content.clear()
                        
            elif(linha[0] == 'if'):
                
                content.append('')
                content.append('if')
                
                for i in range(len(linha)):
                    
                    # print(linha[14])
                    
                    if(linha[i] == '('):
                        
                        content.append('(')
                        
                    elif(linha[i] in variaveis):
                        
                        content.append(linha[i])
                        
                    elif(linha[i] == ')'):
                        
                        content.append("):")
                        
                    elif(linha[i] not in proibido and linha[i] != 'if'):
                        
                        content.append(linha[i])
                        
                    elif(linha[i] == '>='):
                        
                        content.append('>=')
                        
                    elif(linha[i] == '<='):
                        
                        content.append('<=')
                        
                    elif(linha[i] == '!='):
                        
                        content.append('!=')
                        
                    elif(linha[i] == '=='):
                        
                        content.append('==')
                        
                    elif(linha[i] == '&&'):
                        
                        content.append('and')
                        
                    elif(linha[i] == '||'):
                        
                        content.append('or')
                        
                    else:
                        pass
                        
                print(''.join(content))
                content.clear()
                
            content.append('\t')
