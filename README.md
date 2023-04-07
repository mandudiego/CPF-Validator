# Validador de CPF utilizando Python!

## Código comentado:

```python
def check_int(n): # Função para checar se a string representa um número inteiro
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
cont_regressiva = 10
cont_regressiva_2 = 11
result_soma = result_soma_2 = 0
while True: # Laço de repetição 
    cpf = input ('Insira seu CPF: ').replace('.', '') # Input para receber o CPF
    nove_digitos = cpf[:9] # Captura dos 9 primeiros dígitos
    cpf_sequencial = cpf == cpf[0] * len(cpf) # Teste lógico se o CPF é uma sequência de números (Ex: 999.999.999-99)
    if cpf: # Validação se foi inserido o CPF
        if cpf_sequencial: # Se o CPF for sequencial
            print('Dados sequenciais, digite novamente') # [ERRO] CPF Sequencial
        else: # Se não
            if check_int(cpf): # Validação se a string representa um número inteiro (se for inserido letras retorna erro)
                for num in nove_digitos: # Multiplicação regressiva do CPF
                    num_int = int(num) # Conversão de str para int --> Conversão feita para realização do cálculo
                    result_soma += num_int * cont_regressiva  # Multiplicação de cada dígito do CPF pela contagem regressiva de 10
                    cont_regressiva -= 1 # Contagem regressiva de 10 subtraindo 1 a cada laço realizado
                    
                primeiro_digito = (result_soma * 10) % 11 # Cálculo para definição do primeiro dígito validador

                if primeiro_digito > 9: # Se o primeiro dígito validador for maior que 9
                    primeiro_digito = 0 # O primeiro dígito vira 0
                    
                dez_digitos = nove_digitos + str(primeiro_digito) # Concatenação para ter os 10 dígitos
                
                # Realização do mesmo processo anterior para ter o segundo dígito validador
                
                for num_seg in dez_digitos: # Multiplicação regressiva do CPF (Agora com dez dígitos)
                    num_seg_int = int(num_seg) # Conversão de str para int --> Conversão feita para realização do cálculo
                    result_soma_2 += num_seg_int * cont_regressiva_2 # Multiplicação de cada dígito do CPF pela contagem regressiva de 10
                    cont_regressiva_2 -= 1 # Contagem regressiva de 10 subtraindo 1 a cada laço realizado
                    
                segundo_digito = (result_soma_2 * 10) % 11 # Cálculo para definição do segundo dígito validador

                if segundo_digito > 9: # Se o segundo dígito validador for maior que 9
                    segundo_digito = 0 # O segundo dígito vira 0
                    
                cpf_final = dez_digitos + str(segundo_digito) # Concatenação para ter o CPF completo

                if cpf == cpf_final: # Se o CPF inserido pelo usuário for igual ao CPF gerado via cálculo
                    print ('CPF Válido') # CPF Válidado
                    break
                else: # Caso contrário
                    print('CPF Inválido') # CPF Inválidado
                    break 
            else: # [ERRO] Foi inserido alguma letra
                print('Digite apenas números!')     
    else: # [ERRO] Nada foi inserido
        print('Você não inseriu nenhum dado.') 

```
