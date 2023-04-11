import mysql.connector

#LOGIN/CADASTRO
def cadastrar(usuario, senha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'INSERT INTO login (usuario, senha) VALUES ("{usuario}", "{senha}")'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def login(usuario, senha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM  login WHERE (usuario= "{usuario}" AND senha= "{senha}")'
    cursor.execute(comando)

    reposta = cursor.fetchall()

    cursor.close()
    conexao.close()
    
    return reposta 

#VELAS
def setVela(produto, peso_cera, preco_cera, preco_cera_total, essencia1, peso_essencia1, preco_essencia1_total, essencia2, 
            peso_essencia2, preco_essencia2_total, essencia3, peso_essencia3, preco_essencia3_total):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'INSERT INTO velas (produto, peso_cera, preco_cera, preco_cera_total, essencia1, peso_essencia1, preco_essencia1_total, \
                essencia2, peso_essencia2, preco_essencia2_total, essencia3, peso_essencia3, preco_essencia3_total) \
                VALUES ("{produto}", "{peso_cera}", "{preco_cera}", "{preco_cera_total}", "{essencia1}", "{peso_essencia1}", "{preco_essencia1_total}",\
                "{essencia2}", "{peso_essencia2}", "{preco_essencia2_total}", "{essencia3}", "{peso_essencia3}", "{preco_essencia3_total}")'
    
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def delVela(linha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    #Comandos para restaurar o id dentro do banco de dados
    comando1 = f'DELETE FROM velas WHERE id_produto = ("{linha}")'
    comando2 = 'SET  @num := 0'
    comando3 = 'UPDATE velas SET id_produto = @num:= (@num+1)'
    comando4 = 'ALTER TABLE velas AUTO_INCREMENT =1'

    cursor.execute(comando1)
    conexao.commit()
    cursor.execute(comando2)
    conexao.commit()
    cursor.execute(comando3)
    conexao.commit()
    cursor.execute(comando4)
    conexao.commit()

    cursor.close()
    conexao.close()

def listaVelas():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando  = f'SELECT * FROM velas'

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resposta

def setUpdateVela(produto, peso_cera, preco_cera, preco_cera_total, essencia1, peso_essencia1, preco_essencia1_total, essencia2, 
    peso_essencia2, preco_essencia2_total, essencia3, peso_essencia3, preco_essencia3_total, linha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor2 = conexao.cursor()
    comando = f'UPDATE velas SET produto = "{produto}", peso_cera = "{peso_cera}", preco_cera = "{preco_cera}", preco_cera_total = "{preco_cera_total}", \
                essencia1 = "{essencia1}", peso_essencia1 = "{peso_essencia1}", preco_essencia1_total = "{preco_essencia1_total}", \
                essencia2 = "{essencia2}", peso_essencia2 = "{peso_essencia2}", preco_essencia2_total = "{preco_essencia2_total}", \
                essencia3 = "{essencia3}", peso_essencia3 = "{peso_essencia3}", preco_essencia3_total = "{preco_essencia3_total}" WHERE id_produto = {linha}'
    
    cursor2.execute(comando)
    conexao.commit()

    cursor2.close()
    conexao.close()

#ESSENCIAS
def listaEssencias():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )
    cursor = conexao.cursor()

    comando = f'SELECT * FROM essencias'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno


def getValorEssencia(essencia):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'SELECT (preco_g) FROM essencias WHERE Nome LIKE ("{essencia}")'

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close

    return resposta

def delEssencia(linha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )
    cursor = conexao.cursor()

    comando1 = f'DELETE FROM essencias WHERE idessencias = ("{linha}")'
    comando2 = 'SET  @num := 0'
    comando3 = 'UPDATE essencias SET idessencias = @num:= (@num+1)'
    comando4 = 'ALTER TABLE essencias AUTO_INCREMENT =1'

    cursor.execute(comando1)
    conexao.commit()
    cursor.execute(comando2)
    conexao.commit()
    cursor.execute(comando3)
    conexao.commit()
    cursor.execute(comando4)
    conexao.commit()

    cursor.close()
    conexao.close()

def setEssencia(nome, preco):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor(nome, preco)

    comando = f'INSERT INTO essencias (Nome, preco_g) VALUES ("{nome}", "{preco}")'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def setUpdateEssencia(nome, preco, linha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'UPDATE essencias SET Nome = "{nome}", preco_g = {preco} WHERE idessencias = {linha}'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

#ITENS

def setItens(nome, preco, tipo):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'INSERT INTO itens (nome, preco, tipo) VALUES ("{nome}", "{preco}", "{tipo}")'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def itensPesquisa(nome):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'SELECT (preco) FROM itens WHERE nome LIKE ("{nome}")'

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close

    return resposta

def listaItens():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens ORDER BY tipo'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def delItem(nome):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )
    cursor = conexao.cursor()

    comando1 = f'DELETE FROM itens WHERE nome = ("{nome}")'
    comando2 = 'SET  @num := 0'
    comando3 = 'UPDATE itens SET iditens = @num:= (@num+1)'
    comando4 = 'ALTER TABLE itens AUTO_INCREMENT =1'

    cursor.execute(comando1)
    conexao.commit()
    cursor.execute(comando2)
    conexao.commit()
    cursor.execute(comando3)
    conexao.commit()
    cursor.execute(comando4)
    conexao.commit()

    cursor.close()
    conexao.close()

def setUpdateItens(nome, preco, linha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'UPDATE itens SET nome = "{nome}", preco = {preco} WHERE iditens = {linha}'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def buscarId(nome):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT iditens FROM itens WHERE nome LIKE ("{nome}")'
    
    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno 

def listaComboPotes():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Pote")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def listaComboPavios():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Pavio")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def listaComboIlhos():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Ilhos")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def listaComboEtiquetas():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Etiqueta")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def listaComboAdesivos():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Adesivo")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def listaComboOutros():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Outros")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def listaComboDiversos():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM itens WHERE tipo LIKE ("Diversos")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def calculo_valor_itens(nome):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT preco FROM itens WHERE nome LIKE ("{nome}")'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def cadastro_pacote(nome, vela, pote, pavio, ilhos, etiqueta, adesivo, outros, diversos, preco_custo, preco_venda):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'INSERT INTO pacotes (nome, vela, pote, pavio, ilhos, etiqueta, adesivo, outros, diversos, preco_custo, preco_venda) \
                VALUES ("{nome}", "{vela}", "{pote}", "{pavio}", "{ilhos}", "{etiqueta}", "{adesivo}", "{outros}", "{diversos}", {preco_custo}, {preco_venda})'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def listaPacotes():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM pacotes'

    cursor.execute(comando)
    retorno = cursor.fetchall()

    cursor.close()
    conexao.close()

    return retorno

def delPacote(nome):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )
    cursor = conexao.cursor()

    comando1 = f'DELETE FROM pacotes WHERE nome = ("{nome}")'
    comando2 = 'SET  @num := 0'
    comando3 = 'UPDATE pacotes SET idpacotes = @num:= (@num+1)'
    comando4 = 'ALTER TABLE pacotes AUTO_INCREMENT =1'

    cursor.execute(comando1)
    conexao.commit()
    cursor.execute(comando2)
    conexao.commit()
    cursor.execute(comando3)
    conexao.commit()
    cursor.execute(comando4)
    conexao.commit()

    cursor.close()
    conexao.close()

def setUpdatepacote(nome, vela, pote, pavio, ilhos, etiqueta, adesivo, outros, diversos, preco_custo, linha):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'UPDATE pacotes SET nome = "{nome}", vela = "{vela}", pote = "{pote}", pavio = "{pavio}", ilhos = "{ilhos}", etiqueta = "{etiqueta}", \
                adesivo = "{adesivo}", outros = "{outros}", diversos = "{diversos}", preco_custo = {preco_custo} WHERE idpacotes = {linha}'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def listaPacotesValorProduto(nome):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT preco_custo, preco_venda FROM pacotes WHERE nome LIKE ("{nome}")'

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resposta

def salvar_pedido(nome, dia, mes, ano, produtos, custo, venda):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )

    cursor = conexao.cursor()

    comando = f'INSERT INTO pedidos (nome, dia, mes, ano, produtos, custo, venda) VALUES ("{nome}", "{dia}", "{mes}", "{ano}", "{produtos}", "{custo}", "{venda}")'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def listaPedidos():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM pedidos'

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resposta

def delPedido(id_pedido):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare"
    )
    cursor = conexao.cursor()

    comando1 = f'DELETE FROM pedidos WHERE id_pedido = ("{id_pedido}")'
    comando2 = 'SET  @num := 0'
    comando3 = 'UPDATE pedidos SET id_pedido = @num:= (@num+1)'
    comando4 = 'ALTER TABLE pedidos AUTO_INCREMENT =1'

    cursor.execute(comando1)
    conexao.commit()
    cursor.execute(comando2)
    conexao.commit()
    cursor.execute(comando3)
    conexao.commit()
    cursor.execute(comando4)
    conexao.commit()

    cursor.close()
    conexao.close()

def relatorio(mes, ano):
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "calmare",
    )

    cursor = conexao.cursor()

    comando = f'SELECT * FROM pedidos WHERE mes = "{mes}" AND ano = "{ano}"'

    cursor.execute(comando)
    resposta = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resposta