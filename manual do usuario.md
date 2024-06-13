
Para criar um manual do usuário detalhado para o sistema EscolaSys, vamos abordar cada funcionalidade com mais detalhes. Aqui está o conteúdo do manual do usuário:

---

# Manual do Usuário - EscolaSys

Bem-vindo ao manual do usuário do EscolaSys, um sistema de gerenciamento escolar desenvolvido para facilitar a administração de dados de alunos. Este documento fornecerá instruções detalhadas sobre como utilizar todas as funcionalidades oferecidas pelo sistema.

## Índice

1. [Introdução](#introdução)
2. [Instalação](#instalação)
3. [Execução](#execução)
4. [Funcionalidades](#funcionalidades)
   - 4.1 [Adicionar Alunos](#adicionar-alunos)
   - 4.2 [Registrar Advertências](#registrar-advertências)
   - 4.3 [Remover Advertências](#remover-advertências)
   - 4.4 [Adicionar Notas aos Alunos](#adicionar-notas-aos-alunos)
   - 4.5 [Visualizar Lista de Alunos](#visualizar-lista-de-alunos)
   - 4.6 [Visualizar Informações de Aluno Específico](#visualizar-informações-de-aluno-específico)
   - 4.7 [Remover Aluno do Sistema](#remover-aluno-do-sistema)
   - 4.8 [Sair do Programa](#sair-do-programa)
5. [Considerações Finais](#considerações-finais)

---

## 1. Introdução <a name="introdução"></a>

O EscolaSys é uma aplicação de terminal desenvolvida em Python, utilizando SQLite para armazenar os dados dos alunos. Ele oferece uma interface intuitiva para facilitar a administração de informações escolares, como notas, advertências e detalhes pessoais dos alunos.

## 2. Instalação <a name="instalação"></a>

Para utilizar o EscolaSys, é necessário ter o Python instalado no seu computador. Além disso, certifique-se de ter as bibliotecas necessárias instaladas. Para instalar as dependências apenas execute o arquivo setup.exe

## 3. Execução <a name="execução"></a>

Para iniciar o EscolaSys, execute o arquivo `main.py` no terminal:

```bash
python main.py
```

Isso abrirá o menu principal do sistema, onde você poderá escolher entre várias opções de funcionalidades.

## 4. Funcionalidades <a name="funcionalidades"></a>

### 4.1 Adicionar Alunos <a name="adicionar-alunos"></a>

Esta funcionalidade permite cadastrar novos alunos no sistema. Ao selecionar esta opção no menu principal, você será solicitado a inserir as seguintes informações do aluno:

- ID
- Nome
- Data de nascimento
- Escola de origem
- Nota
- Advertências
- Turno
- Sexo
- Turma

Digite as informações conforme solicitado e pressione Enter para confirmar o cadastro do aluno.

### 4.2 Registrar Advertências <a name="registrar-advertências"></a>

Você pode registrar advertências para alunos específicos que precisam de acompanhamento disciplinar. Ao selecionar esta opção, informe o número do aluno desejado para adicionar a advertência.

### 4.3 Remover Advertências <a name="remover-advertências"></a>

Caso seja necessário remover uma advertência previamente registrada para um aluno, selecione esta opção e informe o número do aluno correspondente.

### 4.4 Adicionar Notas aos Alunos <a name="adicionar-notas-aos-alunos"></a>

Para manter o registro das notas dos alunos, utilize esta funcionalidade. Informe o número do aluno desejado e digite a nova nota para ser adicionada ao registro acadêmico do aluno.

### 4.5 Visualizar Lista de Alunos <a name="visualizar-lista-de-alunos"></a>

Esta opção exibe uma lista completa de todos os alunos cadastrados no sistema. Você pode visualizar os IDs e nomes de todos os alunos registrados.

### 4.6 Visualizar Informações de Aluno Específico <a name="visualizar-informações-de-aluno-específico"></a>

Para obter informações detalhadas sobre um aluno específico, selecione esta funcionalidade e informe o número do aluno desejado. Serão exibidas todas as informações disponíveis sobre esse aluno, incluindo notas, advertências e detalhes pessoais.

### 4.7 Remover Aluno do Sistema <a name="remover-aluno-do-sistema"></a>

Caso seja necessário remover um aluno do sistema, selecione esta opção e informe o número do aluno que deseja remover. Esta ação é irreversível, portanto, confirme a remoção com cuidado.

### 4.8 Sair do Programa <a name="sair-do-programa"></a>

Para encerrar o EscolaSys, selecione esta opção no menu principal. Isso fechará o programa e você retornará ao terminal.

## 5. Considerações Finais <a name="considerações-finais"></a>

Este manual do usuário fornece uma visão abrangente das funcionalidades do EscolaSys. Para informações mais detalhadas sobre cada funcionalidade e exemplos de uso, consulte a seção apropriada neste manual ou o documento de ajuda integrado ao sistema.

---

Este manual do usuário foi criado por Thiago para facilitar o uso eficiente do sistema EscolaSys.