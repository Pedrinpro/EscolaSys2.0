import sqlite3 as sql
from colorama import Fore, Style, init
import time
from tabulate import tabulate
import os
import pandas as pd
import google.generativeai as genai
import numpy as np
import csv

key = os.getenv('APIKEY')
genai.configure(api_key=key)
model = 'models/embedding-001'  # Defina o modelo aqui


D1 = {
    "title": "Sobre o Programa",
    "content": "Este programa foi desenvolvido para gerenciar informações de alunos de uma escola. Ele permite adicionar novos alunos, atribuir advertências, adicionar notas, visualizar listas de alunos, entre outras funcionalidades."
}

D2 = {
    "title": "Como Adicionar Alunos",
    "content": "Para adicionar um aluno, selecione a opção 'Adicionar Alunos' no menu principal. Você será solicitado a inserir informações como ID do aluno, nome, data de nascimento, escola de origem, nota, advertências, turno, sexo e turma. Após fornecer essas informações, o programa as armazenará para futuras consultas e gerenciamento."
}

D3 = {
    "title": "Como Atribuir Advertências",
    "content": "Para atribuir uma advertência a um aluno, escolha a opção 'Atribuir Advertência' no menu e informe o número do aluno. O sistema aumentará o número de advertências associadas ao aluno selecionado."
}

D4 = {
    "title": "Como Remover Advertências",
    "content": "Para remover uma advertência de um aluno, selecione a opção 'Remover Advertência' no menu e informe o número do aluno. O sistema diminuirá o número de advertências associadas ao aluno selecionado, desde que haja advertências disponíveis para remover."
}

D5 = {
    "title": "Como Adicionar Notas",
    "content": "Para adicionar uma nota a um aluno, escolha a opção 'Adicionar Nota' no menu e informe o número do aluno e a nova nota. O sistema atualizará a nota associada ao aluno selecionado."
}

D6 = {
    "title": "Como Visualizar a Lista de Alunos",
    "content": "Para visualizar a lista de todos os alunos cadastrados, selecione a opção 'Visualizar Lista de Alunos' no menu principal. O sistema exibirá uma tabela contendo todas as informações dos alunos, como ID, nome, data de nascimento, escola de origem, nota, advertências, turno, sexo e turma."
}

D7 = {
    "title": "Como Visualizar um Aluno Específico",
    "content": "Para visualizar os detalhes de um aluno específico, selecione a opção 'Visualizar Aluno Específico' no menu e informe o número do aluno desejado. O sistema exibirá todas as informações cadastradas para o aluno selecionado."
}

D8 = {
    "title": "Como Remover um Aluno",
    "content": "Para remover um aluno do sistema, selecione a opção 'Remover Aluno' no menu e informe o número do aluno a ser removido. O sistema excluirá todos os registros relacionados a esse aluno da base de dados."
}

D9 = {
    "title": "Encerrando o Programa",
    "content": "Para encerrar o programa de forma segura, selecione a opção 'Sair' no menu principal. O sistema solicitará confirmação antes de fechar completamente."
}

D10 = {
    "title": "Como Inserir Dados de Alunos",
    "content": "Para inserir os dados de um novo aluno no sistema, selecione a opção 'Adicionar Alunos' no menu principal e forneça as informações solicitadas, como nome, idade, data de nascimento, escola de origem, nota, advertências, turno, sexo e turma. O sistema armazenará esses dados para referência futura."
}

D11 = {
    "title": "Como Atualizar Informações de Alunos",
    "content": "Para atualizar informações de um aluno já cadastrado, escolha a opção 'Atualizar Aluno' no menu e informe o número de identificação do aluno. Em seguida, forneça as novas informações a serem atualizadas, como endereço, telefone, e-mail, etc. O sistema modificará os dados conforme especificado."
}

D12 = {
    "title": "Como Remover Alunos",
    "content": "Para remover um aluno do sistema, selecione a opção 'Remover Aluno' no menu e informe o número de identificação do aluno a ser removido. O sistema excluirá todos os registros relacionados a esse aluno da base de dados."
}

D13 = {
    "title": "Como Consultar Notas de Alunos",
    "content": "Para consultar as notas de um aluno específico, escolha a opção 'Consultar Notas' no menu e informe o número de identificação do aluno. O sistema exibirá as notas do aluno para análise."
}

D14 = {
    "title": "Como Registrar Frequência de Alunos",
    "content": "Para registrar a frequência de um aluno em aulas ou atividades, selecione a opção 'Registrar Frequência' no menu e informe o número de identificação do aluno. Em seguida, insira as datas de presença. O sistema manterá um registro de frequência para cada aluno."
}

D15 = {
    "title": "Como Realizar Buscas por Alunos",
    "content": "Para realizar buscas por alunos no sistema, utilize a opção 'Buscar Alunos' no menu e insira critérios de pesquisa, como nome, número de identificação, ou outras informações relevantes. O sistema retornará os resultados correspondentes à pesquisa realizada."
}

D16 = {
    "title": "Como Gerenciar Turmas",
    "content": "Para gerenciar turmas de alunos, escolha a opção 'Gerenciar Turmas' no menu e utilize as funcionalidades fornecidas para adicionar, remover ou modificar informações relacionadas às turmas."
}

D17 = {
    "title": "Como Exportar Dados",
    "content": "Para exportar dados do sistema para outros formatos, como CSV ou Excel, escolha a opção 'Exportar Dados' no menu e selecione o formato desejado. O sistema gerará um arquivo com os dados selecionados para download ou uso externo."
}

D18 = {
    "title": "Como Importar Dados",
    "content": "Para importar dados de outro sistema ou fonte externa, escolha a opção 'Importar Dados' no menu e selecione o arquivo contendo os dados a serem importados. O sistema processará e integrará os dados importados ao sistema atual."
}

D19 = {
    "title": "Como Configurar Preferências do Usuário",
    "content": "Para configurar preferências pessoais no sistema, como idioma, tema, ou outras opções, acesse o menu de configurações e selecione as opções desejadas. O sistema aplicará as configurações conforme especificado pelo usuário."
}

D20 = {
    "title": "Como Realizar Backup de Dados",
    "content": "Para realizar backup dos dados armazenados no sistema, escolha a opção 'Realizar Backup' no menu e selecione o local de armazenamento desejado. O sistema criará uma cópia dos dados para proteção contra perda de informações."
}

D21 = {
    "title": "Como Restaurar Dados",
    "content": "Para restaurar dados a partir de um backup anterior, escolha a opção 'Restaurar Backup' no menu e selecione o arquivo de backup apropriado. O sistema recuperará os dados salvos anteriormente."
}

D22 = {
    "title": "Como Emitir Relatórios de Desempenho",
    "content": "Para emitir relatórios de desempenho de alunos, escolha a opção 'Emitir Relatórios' no menu e selecione os critérios de análise desejados, como período, turma, ou disciplina. O sistema gerará relatórios detalhados para análise."
}

documents = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18 ,D19, D20, D21, D22]


df = pd.DataFrame(documents)
df.columns = ['Title', 'Text']
df


def embed_fn(title, text, model):
    return genai.embed_content(model=model,
                               content=text,
                               task_type="retrieval_document",
                               title=title)["embedding"]

df['Embeddings'] = df.apply(lambda row: embed_fn(row['Title'], row['Text'], model), axis=1)


def ajuda(model):
    query = input("Faça sua pergunta> ")
    passage = acha(query, df, model)
    # Geração de resposta usando outro modelo generativo
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 35,
        "candidate_count": 1,
    }
    safety_settings = {
        "HATE": "BLOCK_NONE",
        "HARASSMENT": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE"
    }
    model_2 = genai.GenerativeModel("gemini-1.0-pro")
    prompt = f"Imagine que você é um professor super instruído e foi solicitado a explicar detalhadamente o seguinte trecho: '{passage}'. Elabore uma explicação abrangente abordando o contexto, principais ideias, detalhes relevantes e possíveis significados implícitos ou conexões com outros conceitos."
    response = model_2.generate_content(prompt)
    print(response.text)
    print("Feito por gemini-Google")
    logo()
    MENU()

def acha(query, dataframe, model):
    query_embedding = genai.embed_content(model=model,
                                          content=query,
                                          task_type="retrieval_query")
    dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])
    idx = np.argmax(dot_products)
    return dataframe.iloc[idx]['Text']


init(autoreset=True)
def color_text(text, color):
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE
    }
    
    # Pega a cor desejada do dicionário ou usa branco se a cor não for válida
    chosen_color = colors.get(color.lower(), Fore.WHITE)
    
    # Imprime o texto com a cor escolhida
    print(f"{chosen_color}{text}{Style.RESET_ALL}")

def logo():
    color_text("""
░██████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░░░░░░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
╚█████╗░██║░░╚═╝███████║██║░░██║██║░░██║██║░░░░░█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
░╚═══██╗██║░░██╗██╔══██║██║░░██║██║░░██║██║░░░░░╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
██████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝███████╗░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░░╚██╗
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝

Contato para erros e sugestões [+55 21-99885-7949]""", "blue")

def MENU():
    color_text("[01] Adicionar alunos;", 'green')
    color_text("[02] Dar uma(1) advertência ao aluno;", "red")
    color_text("[03] Remover uma(1) advertência do aluno;", 'blue')
    color_text("[04] Adicionar nota ao aluno;", 'yellow')
    color_text("[05] Ver lista com todos os alunos;", "white")
    color_text("[06] Ver um aluno em específico", "blue")
    color_text("[07] Remover um aluno", "red")
    color_text("[08] AjudaIA", "green")
    color_text("[09] transformar csv em db", 'blue')
    color_text("[10] transvormar db em csv", 'yellow')
    color_text('[00] sair', 'cyan')
    o = input("escolha a opção: ")
    if o == '01' or o == '1':
        add()
    elif o == '02' or o == '2':
        adv()
    elif o == '03' or o == '3':
        Radv()
    elif o == '04' or o == '4':
        nta()
    elif o == '05' or o == '5':
        ver()
    elif o == '06' or o == '6':
        ver_Es()
    elif o == '07' or o == '7':
        dele()
    elif o =='08' or o =='8':
        ajuda(model)  
    elif o == '09' or o =='9':
        csvtodb()
    elif o == '10':
        csv()
    elif o == '00' or o == '0':
        quit()

def add():
    connect = sql.connect('data.db')
    cursor = connect.cursor()
    id_aluno = input("Digite o ID do aluno: ")
    nm = input("Digite o nome do aluno a ser matriculado: ")
    ns = input("Digite a data de nascimento do aluno (YYYY-MM-DD): ")
    hi = input("De que escola ele veio? ")
    nt = input("Qual a nota dele? ")
    ad = input("Quantas advertências ele tem? ")
    tr = input("Qual o turno? ")
    sx = input("Qual o sexo? ")
    tu = input("Qual a turma? ")

    try:
        cursor.execute('''
        INSERT INTO alunos (id, nome, nascimento, escola_de_origem, nota, advertencia, turno, sexo, turma)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_aluno, nm, ns, hi, nt, ad, tr, sx, tu))
        
        connect.commit()
        print(Fore.YELLOW + f"Aluno {nm} foi matriculado com sucesso!")
    except sql.Error as e:
        print(Fore.RED + f"Erro ao matricular aluno: {e}")
    finally:
        connect.close()
        time.sleep(3)
        logo()
        MENU()

def adv():
    def add(advertencias_id):
        connect = sql.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''
        UPDATE alunos
        SET advertencia = advertencia + 1
        WHERE id = ?
        ''', (advertencias_id,))
        connect.commit()
        connect.close()
    num = input("Qual o numero do aluno que irá levar advertência? ")
    add(num)
    color_text(f"Advertência adicionada ao aluno com ID {num}.", "yellow")
    time.sleep(2)
    logo()
    MENU()

def Radv():
    def unadd(advertencias_id):
        connect = sql.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''
        UPDATE alunos
        SET advertencia = advertencia - 1
        WHERE id = ?
        ''', (advertencias_id,))
        connect.commit()
        connect.close()
    
    num = input("Qual o numero do aluno que irá perder uma advertência? ")
    unadd(num)
    color_text(f"Advertência removida do aluno com ID {num}.", "yellow")
    time.sleep(3)
    logo()
    MENU()

def nta():
    def update_nota(aluno_ID, nova_Nota):
        connect = sql.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''
            UPDATE alunos
            SET nota = ?
            WHERE id = ?
        ''',        (nova_Nota, aluno_ID))
        connect.commit()
        connect.close()
        color_text(f"A nota do aluno com número {aluno_ID} foi atualizada para {nova_Nota}.", "yellow")
    
    v = input("Qual o número do aluno? ")
    n = input("Qual a nova nota do aluno? ")
    update_nota(v, n)
    time.sleep(3)
    logo()
    MENU()


def quit():
    color_text("Deseja realmente sair? [S/N]", "red")
    e = input("> ")
    if e == 's' or e == 'S': 
        color_text("[+] Um momento...", "magenta")
        time.sleep(3)
        exit()
    else:
        logo()
        MENU()

def ver():
    connect = sql.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM alunos")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    connect.close()
    print(tabulate(rows, headers=col_names, tablefmt="pretty"))
    input("pressione enter para voltar ao menu: ")
    logo()
    MENU()

def ver_Es():
    num = input("Qual o número do aluno que você deseja ver? ")
    connect = sql.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (num,))
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    connect.close()
    print(tabulate(rows, headers=col_names, tablefmt="pretty"))
    time.sleep(3)
    logo()
    MENU()

def delete(l):
    connect = sql.connect('data.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?', (l,))
    connect.commit()
    connect.close()
    color_text(f"Aluno com id {l} foi removido", 'yellow')
    time.sleep(3)
    logo()
    MENU()

def dele():
    t = input("Qual o número do aluno que você deseja remover? ")
    delete(t)
    time.sleep(3)
    logo()
    MENU()

def csv():
    csv_file = input("Como você quer o nome do arquivo? ")

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(rows)
    print(f'Dados exportados com sucesso para {csv_file}')
    conn.close()
def csvtodb():
    conn = sqlite3.connect('data.db')  # Substitua 'data.db' pelo nome do seu banco de dados SQLite
    cursor = conn.cursor()
    csv_file = input("Qual arquivo você quer converter? ")
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
         cursor.execute("INSERT INTO alunos (id, nome, nascimento, escola_de_origem, nota, advertencia, turno, sexo, turma) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        row)
    conn.commit()
    print(f'Dados importados com sucesso do arquivo {csv_file} para a tabela alunos.')
    conn.close()

logo()
MENU()
