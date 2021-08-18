def declaracao(linha):
    
    reservada = ['int', 'float', 'char']
    simbolos = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']
    
    if(linha[0] in reservada):
        
        if(linha[2] == ';'):
            
            if(linha[1] not in reservada and linha[1] not in simbolos):
                
                variaveis.append(linha[1])
        

def atribuicao(linha):
    
    reservada = ['int', 'float', 'char']
    simbolos = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']
    operadores = ['+', '-', '*', '/']
    tamanho = len(linha)
    controle = 0
    
    if(linha[0] in variaveis):
        
        if(linha[tamanho-1] == ';'):
        
            if(linha[1] == '='):
                
                controle = 1
                
    if(controle == 1):
        
        for i in range(2, tamanho-1):
                    
            if(i % 2 == 0):
                
                if(linha[i] not in reservada and linha[i] not in simbolos):
                    
                    # print('Variavel')
                    # -----------------------------------------------------------
                    # Fazer a conversão para outra linguagem
                    # -----------------------------------------------------------
                    ...
                    
                else:
                    
                    print('Erro')
                
            elif(i % 2 != 0):
                
                if(linha[i] in operadores):
                    
                    # print('2')
                    # -----------------------------------------------------------
                    # Fazer a conversão para outra linguagem
                    # -----------------------------------------------------------
                    ...
                    
                else:
                    
                    print('Erro')
            
            # print(i)
            
            
def leitura(linha):
    
    tipo_leitura = ['%d', '%c', '%f']
    
    if(linha[0] == 'scanf'):
        
        if(linha[1] == '(' and linha[2] == '"' and linha[4] == '"' and linha[5] == ',' and 
           linha[6] == '&' and linha[8] == ')' and linha[9] == ';'):
            
            if(linha[3] in tipo_leitura):
                
                if(linha[7] in variaveis):
                    
                    # print('1')
                    ...
                    
                else:
                    pass
                
    if(linha[0] == 'printf'):
        
        if(linha[1] == '(' and linha[2] == '"' and linha[4] == '"' and linha[5] == ','  and linha[7] == ')' and linha[8] == ';'):
            
            if(linha[3] in tipo_leitura):
                
                if(linha[6] in variaveis):
                    
                    # print('1')
                    ...
                    
def condicional(linha, contador_if):
    
    reservada = ['int', 'float', 'char']
    simbolos = ['==', '>=', '<=', '!=']
    operador = ['&&', '||']
    controlador = 0
    
    tamanho = len(linha)
    if(linha[0] == 'if'):
        
        contador_if = 1
        
        if(linha[1] == '(' and linha[tamanho-2] == ')' and linha[tamanho-1] == '{'):
            
            # print(contador_if)
            
            for i in range(2, tamanho-2):
                
                # --------------------------
                # Erro no if
                # --------------------------
                
                if(controlador == 0):
                
                    if(linha[i] in variaveis):
                        
                        print(controlador)
                        controlador += 1
                    
                if(controlador == 1):
                    
                    if(linha[i] in simbolos):
                        
                        print(controlador)
                        controlador += 1
                    
                   
                      
                if(controlador == 2):
                    
                    if(linha[i] not in simbolos):
                        
                        if(linha[i] not in operador):
                            
                            if(linha[i] not in reservada):
                        
                                print(controlador)
                                controlador += 1
                        
                    if(linha[i] in variaveis):
                        
                        print(controlador)
                        controlador += 1
                        print(controlador)
                        
                    if(linha[i] in reservada):
                        
                        print('erro')
                        break
                        
                if(controlador == 3):
                    
                    if(linha[i] in operador):
                        
                        controlador = 0
        
    if(contador_if == 1):
        
        if(linha[0] == 'else' and linha[1] == '{'):
            ...
    

texto = open('file.txt', 'r')
linhas = texto.readlines()

# global contador_if
contador_if = 0
global variaveis
variaveis = list()

for linha in linhas:
    
    linha = linha.split()
    declaracao(linha)
    atribuicao(linha)
    leitura(linha)
    condicional(linha, contador_if)
    
    
print(linhas[11])    
print(variaveis)