from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta

def calcular_revisoes(data_estudo_str, timezone_str="America/Sao_Paulo"):
    try:
        # Definir o timezone com base na entrada
        fuso_horario = pytz.timezone(timezone_str)
    except pytz.UnknownTimeZoneError:
        return f"Erro: O fuso horário '{timezone_str}' não é válido. Por favor, insira um fuso horário correto."

    try:
        # Converter string para objeto de data/hora e aplicar timezone
        data_estudo = datetime.strptime(data_estudo_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return "Erro: A data fornecida não está no formato correto. Use o formato 'AAAA-MM-DD HH:MM'."

    # Aplicar o timezone
    data_estudo = fuso_horario.localize(data_estudo)

    # Calcular datas das revisões
    revisao_1 = data_estudo + timedelta(hours=6)
    revisao_2 = data_estudo + timedelta(days=1)
    revisao_3 = data_estudo + timedelta(weeks=1)
    revisao_4 = data_estudo + relativedelta(months=1)

    # Retornar as datas formatadas
    return {
        "Estudo inicial": data_estudo.strftime("%d/%m/%Y %H:%M"),
        "Revisão 1 (mesmo dia)": revisao_1.strftime("%d/%m/%Y %H:%M"),
        "Revisão 2 (24h depois)": revisao_2.strftime("%d/%m/%Y %H:%M"),
        "Revisão 3 (1 semana depois)": revisao_3.strftime("%d/%m/%Y %H:%M"),
        "Revisão 4 (1 mês depois)": revisao_4.strftime("%d/%m/%Y %H:%M")
    }

# Exemplo de uso
timezone_str = input("Digite o fuso horário (ex: America/Sao_Paulo): ")
data_estudo_str = input("Digite a data de estudo (ex: 2025-02-01 11:00): ")

revisoes = calcular_revisoes(data_estudo_str, timezone_str)

# Se o retorno for um erro, ele vai exibir a mensagem
if isinstance(revisoes, str):
    print(revisoes)
else:
    for key, value in revisoes.items():
        print(f"{key}: {value}")
from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta

def calcular_revisoes(data_estudo_str, timezone_str="America/Sao_Paulo"):
    try:
        # Definir o timezone com base na entrada
        fuso_horario = pytz.timezone(timezone_str)
    except pytz.UnknownTimeZoneError:
        return f"Erro: O fuso horário '{timezone_str}' não é válido. Por favor, insira um fuso horário correto."

    try:
        # Converter string para objeto de data/hora e aplicar timezone
        data_estudo = datetime.strptime(data_estudo_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return "Erro: A data fornecida não está no formato correto. Use o formato 'AAAA-MM-DD HH:MM'."

    # Aplicar o timezone
    data_estudo = fuso_horario.localize(data_estudo)

    # Calcular datas das revisões
    revisao_1 = data_estudo + timedelta(hours=6)
    revisao_2 = data_estudo + timedelta(days=1)
    revisao_3 = data_estudo + timedelta(weeks=1)
    revisao_4 = data_estudo + relativedelta(months=1)

    # Retornar as datas formatadas
    return {
        "Estudo inicial": data_estudo.strftime("%d/%m/%Y %H:%M"),
        "Revisão 1 (mesmo dia)": revisao_1.strftime("%d/%m/%Y %H:%M"),
        "Revisão 2 (24h depois)": revisao_2.strftime("%d/%m/%Y %H:%M"),
        "Revisão 3 (1 semana depois)": revisao_3.strftime("%d/%m/%Y %H:%M"),
        "Revisão 4 (1 mês depois)": revisao_4.strftime("%d/%m/%Y %H:%M")
    }

# Exemplo de uso
timezone_str = input("Digite o fuso horário (ex: America/Sao_Paulo): ")
data_estudo_str = input("Digite a data de estudo (ex: 2025-02-01 11:00): ")

revisoes = calcular_revisoes(data_estudo_str, timezone_str)

# Se o retorno for um erro, ele vai exibir a mensagem
if isinstance(revisoes, str):
    print(revisoes)
else:
    for key, value in revisoes.items():
        print(f"{key}: {value}")
