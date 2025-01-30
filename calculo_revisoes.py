from datetime import datetime, timedelta

def calcular_revisoes(data_estudo_str):
    # Converter string para objeto de data/hora
    data_estudo = datetime.strptime(data_estudo_str, "%Y-%m-%d %H:%M")
    
    # Calcular datas das revisões
    revisao_1 = data_estudo + timedelta(hours=6)  # Primeira revisão no mesmo dia
    revisao_2 = data_estudo + timedelta(days=1)  # 24 horas depois
    revisao_3 = data_estudo + timedelta(weeks=1)  # 1 semana depois
    revisao_4 = data_estudo + timedelta(weeks=4)  # 1 mês depois
    
    # Retornar as datas formatadas
    return {
        "Estudo inicial": data_estudo.strftime("%d/%m/%Y %H:%M"),
        "Revisão 1 (mesmo dia)": revisao_1.strftime("%d/%m/%Y %H:%M"),
        "Revisão 2 (24h depois)": revisao_2.strftime("%d/%m/%Y %H:%M"),
        "Revisão 3 (1 semana depois)": revisao_3.strftime("%d/%m/%Y %H:%M"),
        "Revisão 4 (1 mês depois)": revisao_4.strftime("%d/%m/%Y %H:%M")
    }

# Exemplo de uso
data_estudo = "2025-02-01 10:00"  # Substitua pela data e hora desejadas
revisoes = calcular_revisoes(data_estudo)

for key, value in revisoes.items():
    print(f"{key}: {value}")