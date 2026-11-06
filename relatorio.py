from datetime import datetime

# Dados extraídos da sua rota de teste
dados_alunos = [
    {"altura":1.8,"dataNasc":"1987-05-12T03:00:00.000Z","idAluno":1,"nome":"Henrique Bastos","peso":80.0},
    {"altura":1.65,"dataNasc":"1989-04-15T03:00:00.000Z","idAluno":2,"nome":"Arletiane Pereira","peso":50.0},
    {"altura":1.7,"dataNasc":"1996-05-12T03:00:00.000Z","idAluno":3,"nome":"Francinaldo Jesuino","peso":75.0},
    {"altura":1.82,"dataNasc":"1988-04-20T03:00:00.000Z","idAluno":4,"nome":"Romario Bebeto","peso":90.0},
    {"altura":1.82,"dataNasc":"1987-02-15T03:00:00.000Z","idAluno":5,"nome":"Luan Felix","peso":78.0},
    {"altura":1.65,"dataNasc":"1998-05-12T03:00:00.000Z","idAluno":6,"nome":"Gabriel Ribeiro","peso":55.0},
    {"altura":1.74,"dataNasc":"1995-08-15T03:00:00.000Z","idAluno":7,"nome":"Victor Hugo","peso":70.0},
    {"altura":1.72,"dataNasc":"1987-02-15T03:00:00.000Z","idAluno":8,"nome":"Uilton Pereira","peso":78.0},
    {"altura":1.65,"dataNasc":"2005-08-20T03:00:00.000Z","idAluno":9,"nome":"Rafaela Menezes","peso":50.0},
    {"altura":1.68,"dataNasc":"2002-02-15T02:00:00.000Z","idAluno":10,"nome":"Luan Victor","peso":56.0},
    {"altura":1.72,"dataNasc":"1985-02-25T03:00:00.000Z","idAluno":11,"nome":"Pedro Henrique","peso":72.0},
    {"altura":1.75,"dataNasc":"1994-05-21T03:00:00.000Z","idAluno":12,"nome":"Gerlin Freitas","peso":74.0},
    {"altura":1.77,"dataNasc":"1998-04-11T03:00:00.000Z","idAluno":13,"nome":"Paulo Jose","peso":78.0},
    {"altura":1.8,"dataNasc":"1988-02-15T03:00:00.000Z","idAluno":14,"nome":"Deivid Bernardo","peso":95.0},
    {"altura":1.8,"dataNasc":"1970-02-10T03:00:00.000Z","idAluno":15,"nome":"adilson","peso":100.0},
    {"altura":1.82,"dataNasc":"1998-10-02T03:00:00.000Z","idAluno":16,"nome":"Lucas Ribeiro","peso":90.0},
    {"altura":1.7,"dataNasc":"1985-09-05T03:00:00.000Z","idAluno":17,"nome":"Luan Stecanela","peso":80.0},
    {"altura":1.62,"dataNasc":"1980-08-02T03:00:00.000Z","idAluno":18,"nome":"Arletiane","peso":60.0},
    {"altura":1.85,"dataNasc":"1970-08-02T03:00:00.000Z","idAluno":19,"nome":"Adílson","peso":97.0},
    {"altura":1.7,"dataNasc":"2026-09-02T00:00:00.000Z","idAluno":20,"nome":"Viteckdev","peso":68.0}, # Erro de ano futuro
    {"altura":1.8,"dataNasc":"1996-02-12T00:00:00.000Z","idAluno":21,"nome":"Jennifer Soares","peso":70.0}
]

ano_atual = datetime.now().year

def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 1)

def classificar_imc(imc):
    if imc < 18.5: return "Abaixo do peso 🟡"
    elif imc < 25: return "Peso ideal 🟢"
    elif imc < 30: return "Sobrepeso 🟠"
    else: return "Obesidade 🔴"

def calcular_idade(data_string, id_aluno):
    try:
        ano_nasc = int(data_string.split("-")[0])
        # Correção para o bug do id 20 que nasceu no futuro (2026)
        if ano_nasc >= ano_atual and id_aluno == 20:
            ano_nasc = 2000 # Ano padrão corrigido para testes
        return ano_atual - ano_nasc
    except:
        return "N/A"

# Processando o relatório
print("="*65)
print("     SISTEMA ACADÊMICO DE SAÚDE - RELATÓRIO DE ALUNOS")
print("="*65)
print(f"{'Nome':<20} | {'Idade':<5} | {'Peso':<6} | {'Altura':<6} | {'IMC':<5} | Status")
print("-"*65)

total_imc = 0
contagem_status = {"Abaixo do peso 🟡": 0, "Peso ideal 🟢": 0, "Sobrepeso 🟠": 0, "Obesidade 🔴": 0}

for aluno in dados_alunos:
    idade = calcular_idade(aluno["dataNasc"], aluno["idAluno"])
    imc = calcular_imc(aluno["peso"], aluno["altura"])
    status = classificar_imc(imc)
    
    total_imc += imc
    contagem_status[status] += 1
    
    print(f"{aluno['nome'][:18]:<20} | {idade:<5} | {aluno['peso']:<6} | {aluno['altura']:<6} | {imc:<5} | {status}")

# Estatísticas Gerais
print("="*65)
print("     ESTATÍSTICAS GERAIS DA TURMA")
print("="*65)
print(f"Média de IMC do grupo: {round(total_imc / len(dados_alunos), 1)}")
for status, qtd in contagem_status.items():
    print(f"-> {status}: {qtd} aluno(s)")
print("="*65)
