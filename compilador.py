def separador(linha):

    tipo_variavel = ['int', 'float', 'char']
    reservada_print = ['printf']
    simbolo_fim = [';']
    simbolo = ['=']

    # Declaração de Variável
    if(linha[0] in tipo_variavel):
        
        if(linha[1] not in tipo_variavel and linha[1] not in simbolo_fim):
            
            if(linha[2] in simbolo_fim):
                
                return 'v_declarado'
    
    # Atribuição de Variável
    if(linha[0] in variaveis):
        
        if(linha[1] == '='):
            
            if(linha[2] not in tipo_variavel and linha[2] not in simbolo):
                
                if(linha[3] in simbolo_fim):
                    
                    valores.append(linha[2])
                    
    if(linha[0] in reservada_print):
        
        if(linha[2] in variaveis):
            
            pos = variaveis.index(linha[2])
            
            if(linha[4] in simbolo_fim):
                
                return valores[pos]
   


texto = open('file.txt', 'r')
linhas = texto.readlines()

resultado = 0

global variaveis
global valores

variaveis = list()
valores = list()

for linha in linhas:
    
    linha = linha.split()
    
    # print(linha)
    retorno = separador(linha)
    # print(retorno)
    
    if(retorno != None and retorno != 'v_declarado'):
        
        print(retorno)
    
    
    if(retorno == 'v_declarado'):
                
        variaveis.append(linha[1])
        
    # valores.append(retorno)
    
# print(valores)
# print(variaveis)
    