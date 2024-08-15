
# Aplicação de Login e Registro de Usuários

Este projeto é uma aplicação de interface gráfica de usuário (GUI) desenvolvida em Python que implementa um sistema de login e registro. Utiliza `CustomTkinter` para a interface gráfica e `SQLite3` para armazenamento de dados. A aplicação permite que novos usuários se registrem e que usuários existentes façam login de forma segura, com feedback visual diretamente na interface.

## Funcionalidades

- **Registro de Usuário**: Novos usuários podem criar contas fornecendo um nome de usuário e senha. Os dados são armazenados de forma persistente em um banco de dados SQLite.
- **Login de Usuário**: Usuários registrados podem fazer login usando suas credenciais. A aplicação verifica as informações de login e fornece feedback sobre o sucesso ou falha da tentativa.
- **Feedback em Tempo Real**: Mensagens são exibidas na interface para informar o usuário sobre o status das operações, como "Registro bem-sucedido" ou "Usuário já existe".

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada para desenvolver a aplicação.
- **CustomTkinter**: Biblioteca para criar interfaces gráficas modernas e estilizadas.
- **SQLite3**: Sistema de gerenciamento de banco de dados leve e embutido para armazenamento de dados dos usuários.

## Pré-requisitos

- Python 3.x
- Biblioteca `CustomTkinter`

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/JuanRebello/MyProjects

2. **Navegue até o diretório do projeto:**
   ```bash
   cd seu-repositorio

3. **Instale as dependências:**
   ```bash
   pip install customtkinter

## Uso

1. **Execute a aplicação:**
   ```bash
   python app.py

2. **Registro de Usuário:**
   - Acesse a aba "Registro" e insira um nome de usuário e senha.
   - Caso o nome de usuário já exista, uma mensagem indicará que o registro não foi possível.
     
3. **Login de Usuário:**
   - Acesse a aba "Login" e forneça suas credenciais para entrar no sistema.
   - O sistema irá confirmar o login com uma mensagem apropriada.
   
