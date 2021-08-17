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


texto = open('file.txt', 'r')
linhas = texto.readlines()

global variaveis
variaveis = list()

for linha in linhas:
    
    linha = linha.split()
    declaracao(linha)
    atribuicao(linha)
    
print(variaveis)