"""
CPF: 511.258.158-17
Coletar a soma dos 9 primeiros dígitos do CPF
Multiplicar cada um dos valores por uma contagem regressiva começando de 10

Ex: 511.258.158-17 (511258158)
...10..9..8..7..6..5..4..3..2
*...5..1..1..2..5..8..1..5..8
...50..9..8..14.30.40.4.15.16

Somar os resultados:
50+9+8+14+30+40+4+15+16 = 186

Multiplicar o resultado por 10x
186 * 10 = 1860

Obter o resto da divisão da multiplicação por 11
1860 % 11 = 10

Se o resto da divisão for maior que 9:
... Resultado = 0
Se não:
... Resultado é o valor da conta (No ex: 10)

O digito verificador é = 1 (511258158-'1'7)
"""
def check_int(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
cont_regressiva = 10
cont_regressiva_2 = 11
result_soma = result_soma_2 = 0
while True:
    cpf = input ('Insira seu CPF: ').replace('.', '')
    nove_digitos = cpf[:9]
    cpf_sequencial = cpf == cpf[0] * len(cpf)
    if cpf:
        if cpf_sequencial:
            print('Dados sequenciais, digite novamente')
        else:     
            if check_int(cpf):
                for num in nove_digitos: # Multiplicação regressiva do CPF
                    num_int = int(num) # Conversão de str para int
                    result_soma += num_int * cont_regressiva  
                    cont_regressiva -= 1
                primeiro_digito = (result_soma * 10) % 11

                if primeiro_digito > 9:
                    primeiro_digito = 0
                dez_digitos = nove_digitos + str(primeiro_digito)

                for num_seg in dez_digitos:
                    num_seg_int = int(num_seg)
                    result_soma_2 += num_seg_int * cont_regressiva_2
                    cont_regressiva_2 -= 1
                segundo_digito = (result_soma_2 * 10) % 11

                if segundo_digito > 9:
                    segundo_digito = 0
                cpf_final = dez_digitos + str(segundo_digito)

                if cpf == cpf_final:
                    print(cpf_final)
                    print ('CPF Válido')
                    break
                else:
                    print(cpf_final)
                    print('CPF Inválido')
                    break 
            else:
                print('Digite apenas números!')     
    else:
        print('Você não inseriu nenhum dado.') 
