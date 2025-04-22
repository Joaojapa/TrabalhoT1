# -*- coding: utf-8 -*-
"""
Trabalho T1 - Aprendizagem de Máquina
Disciplina: Aprendizagem de Máquina

Integrantes:
# - João Vitor Campos Pires - 2324290064

Fontes consultadas:
- Tabela de IOF regressivo em investimentos (https://www.bb.com.br/site/investimentos/iof/?utm_source=chatgpt.com)
- Tabela de Imposto de Renda regressivo (https://www.sencon.com.br/blog/tabela-de-ir-sobre-investimentos?utm_source=chatgpt.com)
"""

from tabulate import tabulate 

def get_iof_rate(days: int) -> float:
    iof_table = {
        1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
        11: 63, 12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36, 20: 33,
        21: 30, 22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
    }
    return iof_table.get(days, 0.0)

def get_ir_rate(days: int) -> float:
    if days <= 180:
        return 22.5
    elif days <= 360:
        return 20.0
    elif days <= 720:
        return 17.5
    else:
        return 15.0

def calculate_yield(initial_amount: float, days: int, annual_rate: float = 14.15) -> float:
    return initial_amount * (annual_rate / 100) * (days / 365)

def calculate_taxes_and_final(initial_amount: float, days: int) -> dict:
    rendimento_bruto = calculate_yield(initial_amount, days)
    iof_rate = get_iof_rate(days)
    iof_tax = rendimento_bruto * (iof_rate / 100)
    rendimento_pos_iof = rendimento_bruto - iof_tax

    ir_rate = get_ir_rate(days)
    ir_tax = rendimento_pos_iof * (ir_rate / 100)
    rendimento_liquido = rendimento_pos_iof - ir_tax
    valor_final = initial_amount + rendimento_liquido

    return {
        'rendimento_bruto': rendimento_bruto,
        'iof_rate': iof_rate,
        'iof_tax': iof_tax,
        'rendimento_pos_iof': rendimento_pos_iof,
        'ir_rate': ir_rate,
        'ir_tax': ir_tax,
        'rendimento_liquido': rendimento_liquido,
        'valor_final': valor_final
    }

def main() -> None:
    try:
        valor_inicial = float(input("Informe o valor inicial para investimento (use ponto para decimais): R$ "))
        dias = int(input("Informe o tempo de aplicação em dias: "))
    except ValueError:
        print("Entrada inválida. Certifique-se de informar um número para valor e dias.")
        return

    resultados = calculate_taxes_and_final(valor_inicial, dias)


    tabela = [
        ["Valor investido", f"R$ {valor_inicial:.2f}"],
        ["Tempo de aplicação", f"{dias} dias"],
        ["Taxa anual", "14,15%"],
        ["Rendimento bruto", f"R$ {resultados['rendimento_bruto']:.2f}"],
        [f"IOF ({resultados['iof_rate']}%)", f"R$ {resultados['iof_tax']:.2f}"],
        ["Rendimento após IOF", f"R$ {resultados['rendimento_pos_iof']:.2f}"],
        [f"IR ({resultados['ir_rate']}%)", f"R$ {resultados['ir_tax']:.2f}"],
        ["Rendimento líquido", f"R$ {resultados['rendimento_liquido']:.2f}"],
        ["Valor final líquido", f"R$ {resultados['valor_final']:.2f}"]
    ]

    print("\n===== Resultado da Aplicação =====\n")
    print(tabulate(tabela, headers=["Descrição", "Valor"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
