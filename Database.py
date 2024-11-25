import psycopg2
import time

class Database():

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",        
            database="stockcontrol", 
            user="ricardo",     
            password="ricardo"  
        )
        self.cursor = self.conn.cursor()
        time.sleep(2)

    def getProdutos(self) -> list[tuple] | str:
        """
        Busca todos os produtos 

        Retorna:
        - list[tuple]: Produtos
        - str: Mensagem de erro

        """
        try:
            self.cursor.execute("SELECT * FROM produtos")
            produtos = self.cursor.fetchall()
            if produtos == None:
                raise Exception("Nenhum produto encontrado")
            return produtos
        except Exception as e:
            return e

    def getProdutoPorID(self, id:int) -> tuple | str:
        """
        Busca produto por ID

        Parametro:
        - int: id a ser buscado

        Retorna:
        - tuple: Produto
        - str: Mensagem de erro
        """
        try:
            if id < 1:
                raise Exception("ID invalido")
            
            self.cursor.execute(f"SELECT * FROM produtos WHERE id = {id}")
            produto = self.cursor.fetchone()

            if produto == None:
                raise Exception("Produto nao encontrado")
            return produto
        except Exception as e:
            return e
        
    def getProdutoPorNome(self, nome:str) -> list[tuple] | tuple | str:
        """
        Busca todos os produtos que contenham esse nome 

        Parametro:
        - str: nome a ser buscado

        Retorna:
        - list[tuple]: Produtos (quando mais de um produto tem o mesmo nome)
        - tuple: Produto
        - str: Mensagem de erro
        """
        try:
            if nome == None:
                raise Exception("Nome invalido")
            
            self.cursor.execute(f"SELECT * FROM produtos WHERE nome = '{nome}'")
            produtos = self.cursor.fetchall()

            if produtos == None:
                raise Exception("Produto nao encontrado")
            return produtos
        except Exception as e:
            return e
        
    def getUsuarioPorNome(self, nome: str) -> tuple:
        """
        Busca usuario por nome

        Parametro:
        - nome (str): nome a ser buscado

        Retorna:
        - tuple: Usuario
        - str: Mensagem de erro
        """
        try:
            if nome == None:
                raise Exception("Nome invalido")
            
            self.cursor.execute(f"SELECT * FROM usuarios WHERE nome = {nome}")
            usuario = self.cursor.fetchone()

            if usuario == None:
                raise Exception("Usuario nao encontrado")
            return usuario
        except Exception as e:
            return e
        
    def verificarNomeESenha(self, login: str, senha: str) -> bool:
        """
        Verifica se nome e senha estao corretos

        Parametro:
        - login (str): login a ser buscado
        - senha (str): senha a ser buscado

        Retorna:
        - bool: True se existe, False se nao existe
        - str: Mensagem de erro
        """
        try:
            if login == None or senha == None:
                raise Exception("Parametros invalidos")
            
            self.cursor.execute(f"SELECT * FROM usuarios WHERE login = {login} AND senha = {senha}")
            usuario = self.cursor.fetchone()

            if usuario == None:
                return False
            
            return True

        except Exception as e:
            return e

    def finalizarServidor(self):
        """
        Metodo para finalizar a conexao com o banco de dados
        """
        self.cursor.close()
        self.conn.close()