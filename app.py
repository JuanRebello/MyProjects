import tkinter
import sqlite3
import customtkinter as ctk
from datetime import datetime

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("Login e Registro")
        self.root.resizable(False, False)
        
        ctk.set_appearance_mode('dark')
        
        self.frame_login = ctk.CTkFrame(self.root)
        self.frame_registro = ctk.CTkFrame(self.root)

        self.criar_tela_login()
        self.criar_tela_registro()

        # Mostra a tela de login inicialmente
        self.mostrar_tela("login")

        # Conectar ao banco de dados
        self.conexao = self.conectar_db('funcionarios.db')
        self.criar_tabela(self.conexao)

    def criar_tela_login(self):
        label_login = ctk.CTkLabel(self.frame_login, text="Login", font=("Arial", 20))
        label_login.pack(pady=10)

        self.entry_usuario = ctk.CTkEntry(self.frame_login, placeholder_text="Usuário")
        self.entry_usuario.pack(pady=5)

        self.entry_senha = ctk.CTkEntry(self.frame_login, placeholder_text="Senha", show="*")
        self.entry_senha.pack(pady=5)

        botao_login = ctk.CTkButton(self.frame_login, text="Entrar", command=self.fazer_login)
        botao_login.pack(pady=10)

        link_registro = ctk.CTkButton(self.frame_login, text="Registrar-se", command=lambda: self.mostrar_tela("registro"))
        link_registro.pack()

        # Label para exibir mensagens de status
        self.label_mensagem_login = ctk.CTkLabel(self.frame_login, text="", text_color="red")
        self.label_mensagem_login.pack(pady=10)

    def criar_tela_registro(self):
        label_registro = ctk.CTkLabel(self.frame_registro, text="Registro", font=("Arial", 20))
        label_registro.pack(pady=10)

        self.entry_novo_usuario = ctk.CTkEntry(self.frame_registro, placeholder_text="Novo Usuário")
        self.entry_novo_usuario.pack(pady=5)

        self.entry_nova_senha = ctk.CTkEntry(self.frame_registro, placeholder_text="Nova Senha", show="*")
        self.entry_nova_senha.pack(pady=5)

        botao_registrar = ctk.CTkButton(self.frame_registro, text="Registrar", command=self.fazer_registro)
        botao_registrar.pack(pady=10)

        link_login = ctk.CTkButton(self.frame_registro, text="Já tenho uma conta", command=lambda: self.mostrar_tela("login"))
        link_login.pack()

        # Label para exibir mensagens de status
        self.label_mensagem_registro = ctk.CTkLabel(self.frame_registro, text="", text_color="red")
        self.label_mensagem_registro.pack(pady=10)

    def mostrar_tela(self, tela):
        if tela == "login":
            self.frame_registro.pack_forget()
            self.frame_login.pack(pady=20)
        else:
            self.frame_login.pack_forget()
            self.frame_registro.pack(pady=20)

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if self.verificar_usuario(usuario, senha):
            self.label_mensagem_login.configure(text="Login efetuado com sucesso!", text_color="green")
        else:
            self.label_mensagem_login.configure(text="Usuário ou senha incorretos.", text_color="red")

    def fazer_registro(self):
        novo_usuario = self.entry_novo_usuario.get()
        nova_senha = self.entry_nova_senha.get()
        data = datetime.now().strftime("%Y-%m-%d")
        
        if self.inserir_funcionario(novo_usuario, nova_senha, data):
            self.label_mensagem_registro.configure(text="Registrado com sucesso!", text_color="green")
        else:
            self.label_mensagem_registro.configure(text="Usuário já existe.", text_color="red")

    # Conectar-se a um ou criar um banco de dados
    def conectar_db(self, nome_db):
        conexao = sqlite3.connect(nome_db)
        return conexao

    # Criar tabela
    def criar_tabela(self, conexao):
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Funcionarios (
                Usuario TEXT PRIMARY KEY,
                Senha TEXT NOT NULL,
                Data TEXT NOT NULL
            );
        ''')
        conexao.commit()

    # Inserir dados em uma tabela
    def inserir_funcionario(self, usuario, senha, data):
        cursor = self.conexao.cursor()
        try:
            cursor.execute("INSERT INTO Funcionarios (Usuario, Senha, Data) VALUES (?, ?, ?)",
                        (usuario, senha, data))
            self.conexao.commit()
            return True  # Sucesso
        except sqlite3.IntegrityError:
            return False  # Usuário já existe

    # Verificar usuário e senha
    def verificar_usuario(self, usuario, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Funcionarios WHERE Usuario = ? AND Senha = ?", (usuario, senha))
        return cursor.fetchone() is not None

if __name__ == "__main__":
    app = ctk.CTk()
    interface = App(app)
    app.mainloop()
