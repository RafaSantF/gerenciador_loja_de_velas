from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt5 import QtCore
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import ConexoesBD
import ResetFields

app = QtWidgets.QApplication([])
programa = uic.loadUi("login.ui")
programa2 = uic.loadUi("inicio.ui")
programa3 = uic.loadUi("cadastrar_pacote.ui")
programa4 = uic.loadUi("cadastrar_pedido.ui")
programa5 = uic.loadUi("relatorio.ui")
programa6 = uic.loadUi("montar_produtos.ui")
programa6_alterar_essencia = uic.loadUi("alterar_essencia.ui")
programa6_alterar_vela = uic.loadUi("alterar_vela.ui")
programa6_alterar_item = uic.loadUi("alterar_item.ui")
programa7 = uic.loadUi("diversos_concreto.ui")
programa3_alterar_pacote = uic.loadUi("alterar_pacote.ui")
programa4_inserir_produto_pedido = uic.loadUi("inserir_produto_pedido.ui")
programa4_alterar_produto_pedido = uic.loadUi("alterar_produto_pedido.ui")
programa4_salvar_pedido = uic.loadUi("salvar_pedido.ui")

#IMAGENS DA TELA DE LOGIN
programa.background.setPixmap(QPixmap("background.jpg"))
programa.logo.setPixmap(QPixmap("LOGO_circular.png"))
programa.icone_usuario.setPixmap(QPixmap("icone_usuario.png"))
programa.icone_senha.setPixmap(QPixmap("icone_senha.png"))
programa.frame_cadastro.setVisible(False) #Metodo para ocultar o frame de cadastro ao abrir a aplicacao.
programa.usuario_login.setFocus()

#IMAGENS DA TELA INICIO
programa2.titulo_inicio.setPixmap(QPixmap("titulo_janela.png"))
programa2.icone_velas.setPixmap(QPixmap("icone_velas.png"))
programa2.icone_cliente.setPixmap(QPixmap("icone_cliente.png"))
programa2.icone_relatorio.setPixmap(QPixmap("icone_relatorio.png"))
programa2.icone_caixa.setPixmap(QPixmap("icone_caixa.png"))

#IMAGENS DA TELA MONTAR PRODUTOS
programa6.icone_montar_velas.setPixmap(QPixmap("icone_montar_velas.png"))
programa6.icone_montar_essencias.setPixmap(QPixmap("icone_montar_essencias.png"))
programa6.icone_montar_itens.setPixmap(QPixmap("icone_montar_itens.png"))
programa6.icone_escolher_diversos.setPixmap(QPixmap("icone_diversos.png"))

#IMAGENS DA TELA MONTAR PEDIDO
programa4.icone_montar_pedido.setPixmap(QPixmap("icone_pedido.png"))
programa4.icone_historico_pedido.setPixmap(QPixmap("icone_historico_pedido.png"))

#LOGIN
def abrir_frame_cadastro():
    programa.frame_cadastro.show()
    programa.usuario_cadastrar.setFocus()
    ResetFields.resetLogin(programa)
    
def salvar_cadastro():
    usuario = programa.usuario_cadastrar.text()
    senha = programa.senha_cadastrar.text()
    senha_adm = programa.senha_adm_cadastrar.text()

    if usuario == "" or senha == "" or senha_adm == "":
        QMessageBox.about(programa, "Mensagem","Preencha todos os campos.")
    elif senha_adm != "810404":
        QMessageBox.about(programa, "Mensagem","Senha de ADMINISTRADOR incorreta!")
        programa.senha_adm_cadastrar.clear()
    else:
        #Cadastrando 
        ConexoesBD.cadastrar(usuario, senha)
        programa.frame_cadastro.close()
        ResetFields.resetCadastro(programa)
        QMessageBox.about(programa, "Mensagem","Cadastro efetuado com sucesso.")  

def botao_login_voltar():
    programa.frame_cadastro.close()
    ResetFields.resetCadastro(programa)

def botao_login():
    usuario = programa.usuario_login.text()
    senha = programa.senha_login.text()

    if usuario == "" or senha == "":
        QMessageBox.about(programa, "Mensagem","Preencha todos os campos.")
    else:
        executar = ConexoesBD.login(usuario, senha)
        if executar != []:
            programa.close()
            programa2.show()
        else:
            QMessageBox.about(programa, "Mensagem","USUARIO OU SENHA INCORRETOS")

    ResetFields.resetLogin(programa)

#FUNCINALIDADE COMBOBOX MONTAR VELAS
def lista_combobox():
    resposta = ConexoesBD.listaEssencias()
    lista = [""] #As aspas geram uma primeira linha em branco dentro da combobox, permitindo tambem selecionar 'vazio'.
    for i in resposta:
        lista.append(i[1]) #Como nao e obtido o valor das essencias, e obtido apenas o primeiro termo(ind = 0) de cada tupla (essencia, valor).
    
    return lista #Nao esquecer que para ser utilizada como lista a funcao deve RETORNAR uma lista

#FUNCIONALIDADE COMBOBOX VELA
def combobox_pacote_vela():
    resposta = ConexoesBD.listaVelas()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX POTE
def combobox_pacote_pote():
    resposta = ConexoesBD.listaComboPotes()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX PAVIO
def combobox_pacote_pavio():
    resposta = ConexoesBD.listaComboPavios()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX ILHOS
def combobox_pacote_ilhos():
    resposta = ConexoesBD.listaComboIlhos()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX OUTROS
def combobox_pacote_outros():
    resposta = ConexoesBD.listaComboOutros()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX DIVERSOS
def combobox_pacote_diversos():
    resposta = ConexoesBD.listaComboDiversos()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX ETIQUETA
def combobox_pacote_etiqueta():
    resposta = ConexoesBD.listaComboEtiquetas()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX ADESIVO
def combobox_pacote_adesivo():
    resposta = ConexoesBD.listaComboAdesivos()
    lista = [""] 
    for i in resposta:
        lista.append(i[1]) 
    
    return lista 

#FUNCIONALIDADE COMBOBOX PACOTES
def combobox_lista_pacotes():
    resposta = ConexoesBD.listaPacotes()
    lista = [""]
    for i in resposta:
        lista.append(i[1])
    
    return lista

#INICIO
def botao_cadastrar_pacote():
    programa3.show()   
    programa3.frame_cadastrar_pacote.show()
    programa3.frame_lista_pacotes.close()
    programa3.pacote_custo.setText("0.00")
    programa3.pacote_venda.setText("0.00")
    programa3.pacote_margem.clear()
    programa3.pacote_margem.setText("0.00")
    programa3.pacote_vela.clear()
    programa3.pacote_vela.addItems(combobox_pacote_vela())
    programa3.pacote_pote.clear()
    programa3.pacote_pote.addItems(combobox_pacote_pote())
    programa3.pacote_pavio.clear()
    programa3.pacote_pavio.addItems(combobox_pacote_pavio())
    programa3.pacote_ilhos.clear()
    programa3.pacote_ilhos.addItems(combobox_pacote_ilhos())
    programa3.pacote_etiqueta.clear()
    programa3.pacote_etiqueta.addItems(combobox_pacote_etiqueta())
    programa3.pacote_adesivo.clear()
    programa3.pacote_adesivo.addItems(combobox_pacote_adesivo())
    programa3.pacote_outros.clear()
    programa3.pacote_outros.addItems(combobox_pacote_outros())
    programa3.pacote_diversos.clear()
    programa3.pacote_diversos.addItems(combobox_pacote_diversos())

def botao_cadastrar_pedido():
    programa4.show()   
    programa4.frame_pedidos_inicio.show()
    lista_produtos_pedido.clear()
    programa4.tabela_produtos_pedido.setRowCount(0)
    programa4.tabela_produtos_pedido.setColumnWidth(0, 315)
    programa4.tabela_produtos_pedido.setColumnWidth(1, 110)
    programa4.tabela_produtos_pedido.setColumnWidth(2, 110)
    programa4.tabela_produtos_pedido.setHorizontalHeaderLabels(["Produto", "Custo", "Venda"])
    programa4.ecobag_pedido.clear()
    programa4.cartoes_pedido.clear()
    programa4.tag_pedido.clear()
    programa4.caixa_pedido.clear()
    programa4.frame_montar_pedido.close()
    programa4.frame_lista_pedidos.close()
def botao_relatorio():
    programa5.show()    
def botao_montar_produtos():
    programa6.show()   
    programa6.frame_montar_produtos.show()
    ResetFields.resetCombobox(programa6, lista_combobox()) #Prepara o cadastro de velas previamente 

#MONTAR PRODUTOS 
def botao_montar_velas():
    programa6.frame_montar_produtos.close()
    programa6.frame_montar_itens.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.close()
    programa6.frame_montar_velas.show()
    programa6.frame_cadastrar_nova_vela.show()
    ResetFields.resetCombobox(programa6, lista_combobox())

def botao_voltar_montarprod_velas():
    programa6.frame_montar_velas.close()
    programa6.frame_montar_itens.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.close()
    programa6.frame_montar_produtos.show()
    programa6.frame_lista_velas.close()
    programa6.frame_cadastrar_nova_vela.show()

    #Limpando campos apos clique do botao
    ResetFields.resetVelas(programa6, lista_combobox())

def botao_cadastrar_nova_vela():
    programa6.frame_lista_velas.close()
    ResetFields.resetCombobox(programa6, lista_combobox())
    programa6.frame_cadastrar_nova_vela.show()

def botao_salvar_nova_vela():
        if (programa6.produto.text() == "" or programa6.cera_g.text() == "" or programa6.cera_p.text() == ""):
            QMessageBox.about(programa6,"Mensagem" ,"Preencha todos os campos.")
        elif (programa6.combo_essencia_vela1.currentText() == "" and programa6.essencia1_g.text() != ""\
            or programa6.combo_essencia_vela1.currentText() != "" and programa6.essencia1_g.text() == ""):
            QMessageBox.about(programa6,"Mensagem" ,"Essencia e peso devem estar ambos preenchidos ou vazios.")
        elif (programa6.combo_essencia_vela2.currentText() == "" and programa6.essencia2_g.text() != ""\
            or programa6.combo_essencia_vela2.currentText() != "" and programa6.essencia2_g.text() == ""):
            QMessageBox.about(programa6,"Mensagem" ,"Essencia e peso devem estar ambos preenchidos ou vazios.")
        elif (programa6.combo_essencia_vela3.currentText() == "" and programa6.essencia3_g.text() != ""\
            or programa6.combo_essencia_vela3.currentText() != "" and programa6.essencia3_g.text() == ""):
            QMessageBox.about(programa6,"Mensagem" ,"Essencia e peso devem estar ambos preenchidos ou vazios.")
        elif (programa6.combo_essencia_vela1.currentText() == "" and programa6.combo_essencia_vela2.currentText() == "" and \
            programa6.combo_essencia_vela3.currentText() == ""):
            QMessageBox.about(programa6,"Mensagem" ,"Nenhuma essencia inserida na nova vela.")
        else:
            try:
                float(programa6.cera_g.text())  
                float(programa6.cera_p.text())  
                if(programa6.combo_essencia_vela1.currentText() != ""):
                    float(programa6.essencia1_g.text()) 
                if(programa6.combo_essencia_vela2.currentText() != ""):
                    float(programa6.essencia2_g.text())
                if(programa6.combo_essencia_vela3.currentText() != ""):
                    float(programa6.essencia3_g.text())        
            except ValueError:
                QMessageBox.about(programa6,"Mensagem" ,"Existem palavras digitadas nos campos de valores.")
            else:
                essencia1 = programa6.combo_essencia_vela1.currentText()
                essencia2 = programa6.combo_essencia_vela2.currentText()
                essencia3 = programa6.combo_essencia_vela3.currentText()

                #Captacao da essencia no banco de dados para buscar o valor por grama              
                if programa6.combo_essencia_vela1.currentText() != "": 
                    resposta1 = ConexoesBD.getValorEssencia(essencia1) 
                    lista1 = []
                    for i in resposta1:
                        lista1.append(i)
                else:
                    lista1 = [(0,)] #O programa esta conferindo se ha essencia selecionada, caso contrario atribui 0 ao preco da essencia
                
                if programa6.combo_essencia_vela2.currentText() != "":
                    resposta2 = ConexoesBD.getValorEssencia(essencia2) 
                    lista2 = []
                    for i in resposta2:
                        lista2.append(i)
                else:
                    lista2 = [(0,)]

                if programa6.combo_essencia_vela3.currentText() != "":
                    resposta3 = ConexoesBD.getValorEssencia(essencia3) 
                    lista3 = []
                    for i in resposta3:
                        lista3.append(i)
                else:
                    lista3 = [(0,)]

                #Atribui peso zero caso nao seja selsecionada nenhuma essencia.
                if programa6.combo_essencia_vela1.currentText() != "":
                    peso_essencia1 = float(programa6.essencia1_g.text())
                else:
                    peso_essencia1 = 0
                preco_essencia1_total = peso_essencia1 * lista1[0][0]
                
                if programa6.combo_essencia_vela2.currentText() != "":
                    peso_essencia2 = float(programa6.essencia2_g.text())
                else:
                    peso_essencia2 = 0
                preco_essencia2_total = peso_essencia2 * lista2[0][0]
                
                if programa6.combo_essencia_vela3.currentText() != "":
                    peso_essencia3 = float(programa6.essencia3_g.text())
                else:
                    peso_essencia3 = 0
                preco_essencia3_total = peso_essencia3 * lista3[0][0]

                produto = programa6.produto.text()
                peso_cera = float(programa6.cera_g.text())
                preco_cera = float(programa6.cera_p.text())
                preco_cera_total = peso_cera * preco_cera

                #Criacao da vela no banco de dados
                ConexoesBD.setVela(produto, peso_cera, preco_cera, preco_cera_total, essencia1, peso_essencia1, preco_essencia1_total, essencia2, 
                peso_essencia2, preco_essencia2_total, essencia3, peso_essencia3, preco_essencia3_total)

                #Limpando campos apos clique do botao
                ResetFields.resetVelas(programa6, lista_combobox())

                QMessageBox.about(programa6,"Mensagem" ,"Vela cadastrada com sucesso.")

def botao_lista_velas():
    programa6.frame_cadastrar_nova_vela.close()
    programa6.frame_lista_velas.show()

    resposta = ConexoesBD.listaVelas() #Retornar uma lista igual a de essencias

    qtd_linhas = len(resposta)
    programa6.tabela_velas.setRowCount(qtd_linhas)
    programa6.tabela_velas.setColumnCount(5)
    programa6.tabela_velas.setColumnWidth(0, 160)
    programa6.tabela_velas.setColumnWidth(1, 80)
    programa6.tabela_velas.setColumnWidth(2, 170)
    programa6.tabela_velas.setColumnWidth(3, 170)
    programa6.tabela_velas.setColumnWidth(4, 170)
    programa6.tabela_velas.setEditTriggers(QAbstractItemView.NoEditTriggers) #Comando para impedir que as celulas sejam editaveis
    programa6.tabela_velas.setHorizontalHeaderLabels(["Nome", "Gramas", "Essencia 1", "Essencia 2", "Essencia 3"]) #Para impedir renomeio apos reiniciar a tabela

    linha = 0
    while linha < len(resposta):
        programa6.tabela_velas.setItem(linha, 0, QTableWidgetItem(resposta[linha][1]))
        programa6.tabela_velas.setItem(linha, 1, QTableWidgetItem("{:.2f}".format(float(str(resposta[linha][2])))))
        programa6.tabela_velas.setItem(linha, 2, QTableWidgetItem(resposta[linha][5]))
        programa6.tabela_velas.setItem(linha, 3, QTableWidgetItem(resposta[linha][8]))
        programa6.tabela_velas.setItem(linha, 4, QTableWidgetItem(resposta[linha][11]))
        programa6.tabela_velas.item(linha, 1).setTextAlignment(QtCore.Qt.AlignCenter) #Centarliza a informacao na celula mencionada
        programa6.tabela_velas.item(linha, 2).setTextAlignment(QtCore.Qt.AlignCenter) 
        programa6.tabela_velas.item(linha, 3).setTextAlignment(QtCore.Qt.AlignCenter) 
        programa6.tabela_velas.item(linha, 4).setTextAlignment(QtCore.Qt.AlignCenter) 
        linha += 1

def deletar_vela():
    if(programa6.tabela_velas.selectedIndexes()):
        linha = programa6.tabela_velas.currentRow() + 1

        ConexoesBD.delVela(linha)

        indice = programa6.tabela_velas.selectedIndexes()[0]
        programa6.tabela_velas.removeRow(indice.row())
    else:
        QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")
        
def alterar_vela():
    if(programa6.tabela_velas.selectedIndexes()):   
        programa6_alterar_vela.show()
        ResetFields.resetCombobox(programa6_alterar_vela, lista_combobox())

        linha = programa6.tabela_velas.currentRow() 

        resposta = ConexoesBD.listaVelas()

        programa6_alterar_vela.produto.setText(str(resposta[linha][1]))
        programa6_alterar_vela.cera_g.setText(str(resposta[linha][2]))
        programa6_alterar_vela.cera_p.setText(str(resposta[linha][3]))       
        programa6_alterar_vela.essencia1_g.setText(str(resposta[linha][6]))       
        programa6_alterar_vela.essencia2_g.setText(str(resposta[linha][9]))
        programa6_alterar_vela.essencia3_g.setText(str(resposta[linha][12]))

        #PRE-DEFINIR ITEM COMBOBOX
        item_atual_bd = resposta[linha][5]
        if item_atual_bd in lista_combobox():
            indice1 = lista_combobox().index(item_atual_bd)
            programa6_alterar_vela.combo_essencia_vela1.setCurrentIndex(indice1)
        else:
            programa6_alterar_vela.combo_essencia_vela1.setCurrentIndex(0)

        item_atual_bd = resposta[linha][8]
        if item_atual_bd in lista_combobox():
            indice2 = lista_combobox().index(item_atual_bd)
            programa6_alterar_vela.combo_essencia_vela2.setCurrentIndex(indice2)
        else:
            programa6_alterar_vela.combo_essencia_vela2.setCurrentIndex(0)

        item_atual_bd = resposta[linha][11]
        if item_atual_bd in lista_combobox():
            indice3 = lista_combobox().index(item_atual_bd)
            programa6_alterar_vela.combo_essencia_vela3.setCurrentIndex(indice3)
        else:
            programa6_alterar_vela.combo_essencia_vela3.setCurrentIndex(0)

    else:
        QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")

def botao_salvar_alterar_vela():   
        if (programa6_alterar_vela.produto.text() == "" or programa6_alterar_vela.cera_g.text() == "" or programa6_alterar_vela.cera_p.text() == ""):
            QMessageBox.about(programa6_alterar_vela,"Mensagem" ,"Preencha todos os campos.")
        elif (programa6_alterar_vela.combo_essencia_vela1.currentText() == "" and programa6_alterar_vela.essencia1_g.text() != ""\
            or programa6_alterar_vela.combo_essencia_vela1.currentText() != "" and programa6_alterar_vela.essencia1_g.text() == ""):
            QMessageBox.about(programa6_alterar_vela,"Mensagem" ,"Essencia e peso devem estar ambos preenchidos ou vazios.")
        elif (programa6_alterar_vela.combo_essencia_vela2.currentText() == "" and programa6_alterar_vela.essencia2_g.text() != ""\
            or programa6_alterar_vela.combo_essencia_vela2.currentText() != "" and programa6_alterar_vela.essencia2_g.text() == ""):
            QMessageBox.about(programa6_alterar_vela,"Mensagem" ,"Essencia e peso devem estar ambos preenchidos ou vazios.")
        elif (programa6_alterar_vela.combo_essencia_vela3.currentText() == "" and programa6_alterar_vela.essencia3_g.text() != ""\
            or programa6_alterar_vela.combo_essencia_vela3.currentText() != "" and programa6_alterar_vela.essencia3_g.text() == ""):
            QMessageBox.about(programa6_alterar_vela,"Mensagem" ,"Essencia e peso devem estar ambos preenchidos ou vazios.")
        elif (programa6_alterar_vela.combo_essencia_vela1.currentText() == "" and programa6_alterar_vela.combo_essencia_vela2.currentText() == "" and \
            programa6_alterar_vela.combo_essencia_vela3.currentText() == ""):
            QMessageBox.about(programa6_alterar_vela,"Mensagem" ,"Nenhuma essencia inserida na nova vela.")
        else:
            try:
                float(programa6_alterar_vela.cera_g.text())  
                float(programa6_alterar_vela.cera_p.text())  
                if(programa6_alterar_vela.combo_essencia_vela1.currentText() != ""):
                    float(programa6_alterar_vela.essencia1_g.text()) 
                if(programa6_alterar_vela.combo_essencia_vela2.currentText() != ""):
                    float(programa6_alterar_vela.essencia2_g.text())
                if(programa6_alterar_vela.combo_essencia_vela3.currentText() != ""):
                    float(programa6_alterar_vela.essencia3_g.text())       
            except ValueError:
                QMessageBox.about(programa6_alterar_vela,"Mensagem" ,"Existem palavras digitadas nos campos de valores.")
            else:
                essencia1 = programa6_alterar_vela.combo_essencia_vela1.currentText()
                essencia2 = programa6_alterar_vela.combo_essencia_vela2.currentText()
                essencia3 = programa6_alterar_vela.combo_essencia_vela3.currentText()

                #Captacao da essencia no banco de dados para buscar o valor por grama
                if programa6_alterar_vela.combo_essencia_vela1.currentText() != "": 
                    resposta1 = ConexoesBD.getValorEssencia(essencia1) 
                    lista1 = []
                    for i in resposta1:
                        lista1.append(i)
                else:
                    lista1 = [(0,)] #O programa esta conferindo se ha essencia selecionada, caso contrario atribui 0 ao preco da essencia

                if programa6_alterar_vela.combo_essencia_vela2.currentText() != "":
                    resposta2 = ConexoesBD.getValorEssencia(essencia2) 
                    lista2 = []
                    for i in resposta2:
                        lista2.append(i)
                else:
                    lista2 = [(0,)]

                if programa6_alterar_vela.combo_essencia_vela3.currentText() != "":
                    resposta3 = ConexoesBD.getValorEssencia(essencia3) 
                    lista3 = []
                    for i in resposta3:
                        lista3.append(i)
                else:
                    lista3 = [(0,)]

                #Atribui peso zero caso nao seja selsecionada nenhuma essencia.
                if programa6_alterar_vela.combo_essencia_vela1.currentText() != "":
                    peso_essencia1 = float(programa6_alterar_vela.essencia1_g.text())
                else:
                    peso_essencia1 = 0
                preco_essencia1_total = peso_essencia1 * lista1[0][0]
                
                if programa6_alterar_vela.combo_essencia_vela2.currentText() != "":
                    peso_essencia2 = float(programa6_alterar_vela.essencia2_g.text())
                else:
                    peso_essencia2 = 0
                preco_essencia2_total = peso_essencia2 * lista2[0][0]
                
                if programa6_alterar_vela.combo_essencia_vela3.currentText() != "":
                    peso_essencia3 = float(programa6_alterar_vela.essencia3_g.text())
                else:
                    peso_essencia3 = 0
                preco_essencia3_total = peso_essencia3 * lista3[0][0]

                produto = programa6_alterar_vela.produto.text()
                peso_cera = float(programa6_alterar_vela.cera_g.text())
                preco_cera = float(programa6_alterar_vela.cera_p.text())
                preco_cera_total = peso_cera * preco_cera

                #Atualizacao da vela no banco de dados
                linha = programa6.tabela_velas.currentRow() + 1
                ConexoesBD.setUpdateVela(produto, peso_cera, preco_cera, preco_cera_total, essencia1, peso_essencia1, preco_essencia1_total, essencia2, 
                peso_essencia2, preco_essencia2_total, essencia3, peso_essencia3, preco_essencia3_total, linha)

                #Limpando campos apos clique do botao
                ResetFields.resetVelas(programa6_alterar_vela, lista_combobox())

                #Reinicializacao da tabela
                programa6.tabela_velas.clear()
                botao_lista_velas()

                programa6_alterar_vela.close()
                QMessageBox.about(programa6,"Mensagem" ,"Vela atualizada com sucesso.")

def botao_montar_essencias():
    programa6.frame_montar_itens.close()
    programa6.frame_montar_produtos.close()
    programa6.frame_montar_velas.close()
    programa6.frame_montar_essencias.show()
    programa6.frame_cadastrar_nova_essencia.show()

def botao_voltar_montarprod_essencias():
    programa6.frame_montar_itens.close()
    programa6.frame_montar_velas.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.close()
    programa6.frame_montar_produtos.show()
    programa6.frame_lista_essencias.close()
    programa6.frame_cadastrar_nova_essencia.show()

    #Limpando campos
    programa6.essencia.clear()
    programa6.essencia_p.clear()

def botao_cadastrar_nova_essencia():
    programa6.frame_lista_essencias.close()
    programa6.frame_cadastrar_nova_essencia.show()

def botao_salvar_nova_essencia():
    nome = programa6.essencia.text()
    preco = programa6.essencia_p.text()
    if(nome == "" or preco == ""):
        QMessageBox.about(programa6,"Mensagem" ,"Por favor, preencha todos os campos.")
    else:
        try:    
            float(preco)
        except ValueError:
            QMessageBox.about(programa6,"Mensagem" ,"Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setEssencia(nome, preco)
            QMessageBox.about(programa6, "Mensagem", "Essencia cadastrada com sucesso")
            
            #Limpando campos
            ResetFields.resetEssencias(programa6)
    
def botao_lista_essencias():
    programa6.frame_cadastrar_nova_essencia.close()
    programa6.frame_lista_essencias.show()

    #LISTAGEM DAS ESSENCIAS
    #Retorna uma lista [(nome, preco), (nome,preco)...]
    resposta = ConexoesBD.listaEssencias()

    qtd_linhas = len(resposta)
    programa6.tabela_essencias.setRowCount(qtd_linhas)
    programa6.tabela_essencias.setColumnCount(2)
    programa6.tabela_essencias.setColumnWidth(0, 350)
    programa6.tabela_essencias.setColumnWidth(1, 100)
    programa6.tabela_essencias.setEditTriggers(QAbstractItemView.NoEditTriggers) #Comando para impedir que as celulas sejam editaveis
    programa6.tabela_essencias.setHorizontalHeaderLabels(["Nome", "Valor(R$/g)"]) #Para impedir renomeio apos reiniciar a tabela
   
    linha = 0

    while linha < len(resposta):
        programa6.tabela_essencias.setItem(linha, 0, QTableWidgetItem(resposta[linha][1]))
        programa6.tabela_essencias.setItem(linha, 1, QTableWidgetItem("R$" + "{:.2f}".format(float(str(resposta[linha][2])))))
        programa6.tabela_essencias.item(linha, 1).setTextAlignment(QtCore.Qt.AlignCenter) #Este comando centraliza a informacao na linha em que passa
        linha += 1

def deletar_essencia():
    if(programa6.tabela_essencias.selectedIndexes()):
        linha = programa6.tabela_essencias.currentRow() + 1

        ConexoesBD.delEssencia(linha) 

        #As duas linha abaixo removem uma linha da tabela, apenas visualmente, porem a remocao ocorre simultaneamente ao banco de dados
        indice = programa6.tabela_essencias.selectedIndexes()[0]
        programa6.tabela_essencias.removeRow(indice.row())
    else:
         QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")
   
def alterar_essencia():
    if(programa6.tabela_essencias.selectedIndexes()):
        programa6_alterar_essencia.show()
        linha = programa6.tabela_essencias.currentRow()
        nome = programa6.tabela_essencias.item(linha, 0).text()
        valor = programa6.tabela_essencias.item(linha, 1).text()
        valor_limpo = valor.replace("R$", "")

        programa6_alterar_essencia.essencia.setText(nome)
        programa6_alterar_essencia.essencia_p.setText(valor_limpo)
    else:
        QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")

def botao_salvar_alterar_essencia():
    linha = programa6.tabela_essencias.currentRow() + 1
    preco = programa6_alterar_essencia.essencia_p.text()
    nome = programa6_alterar_essencia.essencia.text()
    if(nome == "" or preco == ""):
        QMessageBox.about(programa6_alterar_essencia,"Mensagem" ,"Por favor, preencha todos os campos.")
    else:
        try:    
            float(preco)
        except ValueError:
            QMessageBox.about(programa6_alterar_essencia,"Mensagem" ,"Existem palavras digitadas nos campos de valores.")
        else:    
            ConexoesBD.setUpdateEssencia(nome, preco, linha)

            ResetFields.resetEssencias(programa6_alterar_essencia)
            programa6_alterar_essencia.close()

            #Reinicializacao da tabela
            programa6.tabela_essencias.clear()
            botao_lista_essencias()

            QMessageBox.about(programa6,"Mensagem" ,"Essencia atualizada com sucesso.")

def botao_montar_itens():
    programa6.frame_montar_itens.show()
    programa6.frame_montar_produtos.close()
    programa6.frame_montar_velas.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.close()
    programa6.frame_cadastrar_pote.show()

def botao_voltar_montarprod_itens():
    programa6.frame_montar_itens.close()
    programa6.frame_montar_velas.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.close()
    programa6.frame_lista_itens.close()
    programa6.frame_montar_produtos.show()
    programa6.frame_cadastrar_pote.show()

def botao_item_pote():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.show()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.close()

def botao_salvar_item_pote():
    nome = programa6.item_pote.text()
    preco = programa6.item_preco_pote.text()
    if (nome == "" and preco == ""):
        QMessageBox.about(programa6, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Pote")
            QMessageBox.about(programa6, "Mensagem", "Pote cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetPote(programa6)
            
def botao_item_pavio():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.show()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.close()

def botao_salvar_item_pavio():
    nome = programa6.item_pavio.text()
    preco = programa6.item_preco_pavio.text()
    if (nome == "" and preco == ""):
        QMessageBox.about(programa6, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Pavio")
            QMessageBox.about(programa6, "Mensagem", "Pavio cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetPavio(programa6)

def botao_item_adesivo():
    programa6.frame_cadastrar_adesivo.show()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.close()

def botao_salvar_item_adesivo():
    nome = programa6.item_adesivo.text()
    preco = programa6.item_preco_adesivo.text()
    if (nome == "" and preco == ""):
        QMessageBox.about(programa6, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Adesivo")
            QMessageBox.about(programa6, "Mensagem", "Adesivo cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetAdesivo(programa6)

def botao_item_etiquetas():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.show()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.close()

def botao_salvar_item_etiqueta():
    nome = programa6.item_etiqueta.text()
    preco = programa6.item_preco_etiqueta.text()
    if (nome == "" and preco == ""):
        QMessageBox.about(programa6, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Etiqueta")
            QMessageBox.about(programa6, "Mensagem", "Etiqueta cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetEtiqueta(programa6)

def botao_item_ilhos():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.show()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.close()

def botao_salvar_item_ilhos():
    nome = programa6.item_ilhos.text()
    preco = programa6.item_preco_ilhos.text()
    if (nome == "" and preco == ""):
        QMessageBox.about(programa6, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Ilhos")
            QMessageBox.about(programa6, "Mensagem", "Ilhos cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetIlhos(programa6)

def botao_item_outros():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.show()

def botao_salvar_item_outros():
    nome = programa6.item_outros.text()
    preco = programa6.item_preco_outros.text()
    if (nome == "" and preco == ""):
        QMessageBox.about(programa6, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Outros")
            QMessageBox.about(programa6, "Mensagem", "Item diversificado cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetOutros(programa6)

def botao_item_ectg():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.show()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.close()
    programa6.frame_cadastrar_outros.close()

def botao_salvar_item_ectg():
    preco_eco = programa6.item_preco_ecobag.text()
    preco_cartao = programa6.item_preco_cartao.text()
    preco_tag = programa6.item_preco_tag.text()
    preco_caixa = programa6.item_preco_caixa.text()
    pesquisa_ecobag = ConexoesBD.itensPesquisa("Ecobag")
    pesquisa_cartao = ConexoesBD.itensPesquisa("Cartao")
    pesquisa_tag = ConexoesBD.itensPesquisa("Tag")
    pesquisa_caixa = ConexoesBD.itensPesquisa("Caixa")

    if (preco_eco == "" or preco_cartao == "" or preco_tag == "" or preco_caixa == ""):
        QMessageBox.about(programa6, "Mensagem", "Preencha todos os campos.")
    elif (len(pesquisa_ecobag) != 0 or len(pesquisa_cartao) != 0 or len(pesquisa_tag) != 0 or len(pesquisa_caixa) != 0):
        QMessageBox.about(programa6, "Mensagem", "Existem cadastros destes itens no sistema.")
        ResetFields.resetEctg(programa6)
    else:
        try:
            float(preco_eco)
            float(preco_cartao)
            float(preco_tag)
            float(preco_caixa)
        except ValueError:
            QMessageBox.about(programa6, "Mensagem", "Existem palavras digitadas em campos de valores.")
        else:
            ConexoesBD.setItens("Ecobag", preco_eco, "Ecobag")
            ConexoesBD.setItens("Cartoes Agradecimento", preco_cartao, "Cartao")
            ConexoesBD.setItens("Tag", preco_tag, "Tag")  
            ConexoesBD.setItens("Caixa", preco_caixa, "Caixa")
            #Limpando campos
            ResetFields.resetEctg(programa6)  
            QMessageBox.about(programa6, "Mensagem", "Itens cadastrados com sucesso.")

def botao_lista_itens():
    programa6.frame_cadastrar_adesivo.close()
    programa6.frame_cadastrar_ectg.close()
    programa6.frame_cadastrar_etiqueta.close()
    programa6.frame_cadastrar_ilhos.close()
    programa6.frame_cadastrar_pavio.close()
    programa6.frame_cadastrar_pote.close()
    programa6.frame_lista_itens.show()
    programa6.frame_cadastrar_outros.close()

    resposta = ConexoesBD.listaItens()

    qtd_linhas = len(resposta)
    programa6.tabela_itens.setRowCount(qtd_linhas)
    programa6.tabela_itens.setColumnCount(3)
    programa6.tabela_itens.setColumnWidth(0, 350)
    programa6.tabela_itens.setColumnWidth(1, 100)
    programa6.tabela_itens.setColumnWidth (2, 100)
    programa6.tabela_itens.setEditTriggers(QAbstractItemView.NoEditTriggers)
    programa6.tabela_itens.setHorizontalHeaderLabels(["Nome", "Valor", "Tipo"])

    linha = 0

    while linha<len(resposta):
        programa6.tabela_itens.setItem(linha, 0, QTableWidgetItem(resposta[linha][1]))
        programa6.tabela_itens.setItem(linha, 1, QTableWidgetItem("R$" + "{:.2f}".format(float(str(resposta[linha][2])))))
        programa6.tabela_itens.setItem(linha, 2, QTableWidgetItem(resposta[linha][3]))
        programa6.tabela_itens.item(linha, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        programa6.tabela_itens.item(linha, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        linha += 1

def deletar_item():
    if(programa6.tabela_itens.selectedIndexes()):
        linha = programa6.tabela_itens.currentRow() 
        nome = programa6.tabela_itens.item(linha, 0).text()

        ConexoesBD.delItem(nome) 

        indice = programa6.tabela_itens.selectedIndexes()[0]
        programa6.tabela_itens.removeRow(indice.row())
    else:
         QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")

def alterar_item():
    programa6_alterar_item.show()
    linha = programa6.tabela_itens.currentRow() 
    nome = programa6.tabela_itens.item(linha, 0).text()
    valor = programa6.tabela_itens.item(linha, 1).text()
    valor_limpo = valor.replace("R$", "")

    programa6_alterar_item.item.setText(nome)
    programa6_alterar_item.item_p.setText(valor_limpo)

def botao_salvar_alterar_item():
    #Variaveis para buscar valores no BD afim de definir a linha a alterar
    linha = programa6.tabela_itens.currentRow()
    nome_bd = programa6.tabela_itens.item(linha, 0).text()
    
    id = ConexoesBD.buscarId(nome_bd)

    #Variaveis para inserir valores no BD afim de alterar determinada linha
    nome = programa6_alterar_item.item.text()
    preco = programa6_alterar_item.item_p.text()

    if(nome == "" or preco == ""):
        QMessageBox.about(programa6_alterar_item, "Mensagem", "Por favor, preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa6_alterar_essencia, "Mensagem", "Existem palavras digitadas nos campos de valores.")
        else:
            ConexoesBD.setUpdateItens(nome, preco, id[0][0])

            ResetFields.resetAlterarItens(programa6_alterar_item)
            programa6_alterar_item.close()
        
            #Reinicializacao da tabela
            programa6.tabela_itens.clear()
            botao_lista_itens()

            QMessageBox.about(programa6, "Mensagem", "Item atualizado com sucesso.")
    
def botao_escolher_diversos():
    programa6.frame_montar_itens.close()
    programa6.frame_montar_produtos.close()
    programa6.frame_montar_velas.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.show()

def botao_voltar_montarprod_diversos():
    programa6.frame_montar_velas.close()
    programa6.frame_montar_itens.close()
    programa6.frame_montar_essencias.close()
    programa6.frame_escolher_diversos.close()
    programa6.frame_montar_produtos.show()

def botao_diversos_concreto():
    programa7.show()

def botao_salvar_diversos_concreto():
    nome = programa7.diversos_concreto_nome.text()
    preco = programa7.diversos_concreto_preco.text()

    if (nome == "" and preco == ""):
        QMessageBox.about(programa7, "Mensagem", "Por favor, Preencha todos os campos.")
    else:
        try:
            float(preco)
        except ValueError:
            QMessageBox.about(programa7, "Mesagem", "Existem palavras digitadas no campo de valor.")
        else:
            ConexoesBD.setItens(nome, preco, "Diversos")
            QMessageBox.about(programa7, "Mensagem", "Item de concreto cadastrado com sucesso.")

            #Limpando campos
            ResetFields.resetDiversosConcreto(programa7)

    programa7.close()

def cadastrar_pacote():
    programa3.frame_cadastrar_pacote.show()
    programa3.frame_lista_pacotes.close()
    ResetFields.resetPacote(programa3)
    programa3.pacote_vela.clear() 
    programa3.pacote_vela.addItems(combobox_pacote_vela()) 
    programa3.pacote_pote.clear() 
    programa3.pacote_pote.addItems(combobox_pacote_pote()) 
    programa3.pacote_pavio.clear() 
    programa3.pacote_pavio.addItems(combobox_pacote_pavio()) 
    programa3.pacote_ilhos.clear() 
    programa3.pacote_ilhos.addItems(combobox_pacote_ilhos()) 
    programa3.pacote_etiqueta.clear() 
    programa3.pacote_etiqueta.addItems(combobox_pacote_etiqueta()) 
    programa3.pacote_adesivo.clear() 
    programa3.pacote_adesivo.addItems(combobox_pacote_adesivo()) 
    programa3.pacote_outros.clear() 
    programa3.pacote_outros.addItems(combobox_pacote_outros())
    programa3.pacote_diversos.clear() 
    programa3.pacote_diversos.addItems(combobox_pacote_diversos())

#CALCULO VALOR VELA
def calculo_valor_vela(linha):
    info_vela = ConexoesBD.listaVelas()
    preco_cera_total = info_vela[linha][4]
    preco_essencia1_total = info_vela[linha][7]
    preco_essencia2_total = info_vela[linha][10]
    preco_essencia3_total = info_vela[linha][13]
    valor_vela = preco_cera_total + preco_essencia1_total + preco_essencia2_total + preco_essencia3_total 
    return valor_vela

def botao_calcular_pacote():
    combo_indice_vela_selecionado = combobox_pacote_vela().index(programa3.pacote_vela.currentText())       
    combo_pote_selecionado = programa3.pacote_pote.currentText()
    combo_pavio_selecionado = programa3.pacote_pavio.currentText()
    combo_ilhos_selecionado = programa3.pacote_ilhos.currentText()
    combo_etiqueta_selecionado = programa3.pacote_etiqueta.currentText()
    combo_adesivo_selecionado = programa3.pacote_adesivo.currentText()
    combo_outros_selecionado = programa3.pacote_outros.currentText()
    combo_diversos_selecionado = programa3.pacote_diversos.currentText()
    margem = programa3.pacote_margem.text()

    try:
        float(margem)
    except ValueError:
        QMessageBox.about(programa4, "Mensagem", "Existem palavaras escritas nos campos de valores")
    if(programa3.pacote_vela.currentText() != ""):
        valor_vela = calculo_valor_vela(combo_indice_vela_selecionado-1)
    else:
        valor_vela = 0
    if(programa3.pacote_pote.currentText() != ""):
        valor_poteL = ConexoesBD.calculo_valor_itens(combo_pote_selecionado)
        valor_pote = valor_poteL[0][0]
    else:
        valor_pote = 0
    if(programa3.pacote_pavio.currentText() != ""):
        valor_pavioL = ConexoesBD.calculo_valor_itens(combo_pavio_selecionado)
        valor_pavio = valor_pavioL[0][0]
    else:
        valor_pavio = 0
    if(programa3.pacote_ilhos.currentText() != ""):
        valor_ilhosL = ConexoesBD.calculo_valor_itens(combo_ilhos_selecionado)
        valor_ilhos = valor_ilhosL[0][0]
    else:
        valor_ilhos = 0
    if(programa3.pacote_etiqueta.currentText() != ""):
        valor_etiquetaL = ConexoesBD.calculo_valor_itens(combo_etiqueta_selecionado)
        valor_etiqueta = valor_etiquetaL[0][0]
    else:
        valor_etiqueta = 0
    if(programa3.pacote_adesivo.currentText() != ""):
        valor_adesivoL = ConexoesBD.calculo_valor_itens(combo_adesivo_selecionado)
        valor_adesivo = valor_adesivoL[0][0]
    else:
        valor_adesivo = 0
    if(programa3.pacote_outros.currentText() != ""):
        valor_outrosL = ConexoesBD.calculo_valor_itens(combo_outros_selecionado)
        valor_outros = valor_outrosL[0][0]
    else:
        valor_outros = 0
    if(programa3.pacote_diversos.currentText() != ""):
        valor_diversosL = ConexoesBD.calculo_valor_itens(combo_diversos_selecionado)
        valor_diversos = valor_diversosL[0][0]
    else:
        valor_diversos = 0

    valor_pacote = valor_vela + valor_pote + valor_pavio + valor_ilhos + valor_etiqueta + valor_adesivo + valor_outros + valor_diversos
    venda = valor_pacote + (valor_pacote * float(margem)/100)

    programa3.pacote_custo.setText(str("{:.2f}".format(valor_pacote)))
    programa3.pacote_venda.setText(str("{:.2f}".format(venda)))

def pacote_salvar():
    if (programa3.pacote_nome.text() == ""):
        QMessageBox.about(programa3, "Mensagem", "Nenhum nome foi definido para o produto.")
    elif (programa3.pacote_vela.currentText() == "" and programa3.pacote_pote.currentText() == "" and programa3.pacote_pavio.currentText() == ""\
        and programa3.pacote_ilhos.currentText() == "" and programa3.pacote_etiqueta.currentText() == "" and programa3.pacote_adesivo.currentText() == ""\
        and programa3.pacote_outros.currentText() == "" and programa3.pacote_diversos.currentText() == ""):
        QMessageBox.about(programa3, "Mensagem", "Preencha algum campo alem do nome.")
    elif(programa3.pacote_custo.text() == "0.00"):
        QMessageBox.about(programa3, "Mensagem", "Calcule o valor antes de salvar.")
    else:
        nome = programa3.pacote_nome.text()
        vela = programa3.pacote_vela.currentText()
        pote = programa3.pacote_pote.currentText()
        pavio = programa3.pacote_pavio.currentText()
        ilhos = programa3.pacote_ilhos.currentText()
        etiqueta = programa3.pacote_etiqueta.currentText()
        adesivo = programa3.pacote_adesivo.currentText()
        outros = programa3.pacote_outros.currentText()
        diversos = programa3.pacote_diversos.currentText()
        preco_custo = programa3.pacote_custo.text()
        preco_venda = programa3.pacote_venda.text()

        ConexoesBD.cadastro_pacote(nome, vela, pote, pavio, ilhos, etiqueta, adesivo, outros, diversos, preco_custo, preco_venda)
        QMessageBox.about(programa3, "Mensagem", "Cadastro realizado com sucesso.")
        ResetFields.resetPacote(programa3)
        programa3.pacote_vela.clear() 
        programa3.pacote_vela.addItems(combobox_pacote_vela()) 
        programa3.pacote_pote.clear() 
        programa3.pacote_pote.addItems(combobox_pacote_pote()) 
        programa3.pacote_pavio.clear() 
        programa3.pacote_pavio.addItems(combobox_pacote_pavio()) 
        programa3.pacote_ilhos.clear() 
        programa3.pacote_ilhos.addItems(combobox_pacote_ilhos()) 
        programa3.pacote_etiqueta.clear() 
        programa3.pacote_etiqueta.addItems(combobox_pacote_etiqueta()) 
        programa3.pacote_adesivo.clear() 
        programa3.pacote_adesivo.addItems(combobox_pacote_adesivo()) 
        programa3.pacote_outros.clear() 
        programa3.pacote_outros.addItems(combobox_pacote_outros())
        programa3.pacote_diversos.clear() 
        programa3.pacote_diversos.addItems(combobox_pacote_diversos())

def botao_lista_pacotes():
    programa3.frame_cadastrar_pacote.close()
    programa3.frame_lista_pacotes.show()        

    resposta = ConexoesBD.listaPacotes()

    qtd_linhas = len(resposta)
    programa3.tabela_pacotes.setRowCount(qtd_linhas)
    programa3.tabela_pacotes.setColumnCount(3)
    programa3.tabela_pacotes.setColumnWidth(0, 350)
    programa3.tabela_pacotes.setColumnWidth (1, 100)
    programa3.tabela_pacotes.setColumnWidth (2, 100)
    programa3.tabela_pacotes.setEditTriggers(QAbstractItemView.NoEditTriggers)
    programa3.tabela_pacotes.setHorizontalHeaderLabels(["Nome", "Custo", "Venda"])

    linha = 0

    while linha<len(resposta):
        programa3.tabela_pacotes.setItem(linha, 0, QTableWidgetItem(resposta[linha][1]))
        programa3.tabela_pacotes.setItem(linha, 1, QTableWidgetItem("R$" + "{:.2f}".format(float(str(resposta[linha][13])))))
        programa3.tabela_pacotes.setItem(linha, 2, QTableWidgetItem("R$" + "{:.2f}".format(float(str(resposta[linha][14])))))
        programa3.tabela_pacotes.item(linha, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        programa3.tabela_pacotes.item(linha, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        linha += 1

def deletar_pacote():
    if(programa3.tabela_pacotes.selectedIndexes()):
        linha = programa3.tabela_pacotes.currentRow() 
        nome = programa3.tabela_pacotes.item(linha, 0).text()

        ConexoesBD.delPacote(nome) 

        indice = programa3.tabela_pacotes.selectedIndexes()[0]
        programa3.tabela_pacotes.removeRow(indice.row())
    else:
         QMessageBox.about(programa3,"Mensagem" ,"Nenhuma linha selecionada.")

def botao_calcular_alterar_pacote():
    combo_indice_vela_selecionado = combobox_pacote_vela().index(programa3_alterar_pacote.pacote_vela_2.currentText())       
    combo_pote_selecionado = programa3_alterar_pacote.pacote_pote_2.currentText()
    combo_pavio_selecionado = programa3_alterar_pacote.pacote_pavio_2.currentText()
    combo_ilhos_selecionado = programa3_alterar_pacote.pacote_ilhos_2.currentText()
    combo_etiqueta_selecionado = programa3_alterar_pacote.pacote_etiqueta_2.currentText()
    combo_adesivo_selecionado = programa3_alterar_pacote.pacote_adesivo_2.currentText()
    combo_outros_selecionado = programa3_alterar_pacote.pacote_outros_2.currentText()
    combo_diversos_selecionado = programa3_alterar_pacote.pacote_diversos_2.currentText()
    margem = programa3_alterar_pacote.pacote_margem_2.text()

    if(programa3_alterar_pacote.pacote_vela_2.currentText() != ""):
        valor_vela = calculo_valor_vela(combo_indice_vela_selecionado-1)
    else:
        valor_vela = 0
    if(programa3_alterar_pacote.pacote_pote_2.currentText() != ""):
        valor_poteL = ConexoesBD.calculo_valor_itens(combo_pote_selecionado)
        valor_pote = valor_poteL[0][0]
    else:
        valor_pote = 0
    if(programa3_alterar_pacote.pacote_pavio_2.currentText() != ""):
        valor_pavioL = ConexoesBD.calculo_valor_itens(combo_pavio_selecionado)
        valor_pavio = valor_pavioL[0][0]
    else:
        valor_pavio = 0
    if(programa3_alterar_pacote.pacote_ilhos_2.currentText() != ""):
        valor_ilhosL = ConexoesBD.calculo_valor_itens(combo_ilhos_selecionado)
        valor_ilhos = valor_ilhosL[0][0]
    else:
        valor_ilhos = 0
    if(programa3_alterar_pacote.pacote_etiqueta_2.currentText() != ""):
        valor_etiquetaL = ConexoesBD.calculo_valor_itens(combo_etiqueta_selecionado)
        valor_etiqueta = valor_etiquetaL[0][0]
    else:
        valor_etiqueta = 0
    if(programa3_alterar_pacote.pacote_adesivo_2.currentText() != ""):
        valor_adesivoL = ConexoesBD.calculo_valor_itens(combo_adesivo_selecionado)
        valor_adesivo = valor_adesivoL[0][0]
    else:
        valor_adesivo = 0
    if(programa3_alterar_pacote.pacote_outros_2.currentText() != ""):
        valor_outrosL = ConexoesBD.calculo_valor_itens(combo_outros_selecionado)
        valor_outros = valor_outrosL[0][0]
    else:
        valor_outros = 0
    if(programa3_alterar_pacote.pacote_diversos_2.currentText() != ""):
        valor_diversosL = ConexoesBD.calculo_valor_itens(combo_diversos_selecionado)
        valor_diversos = valor_diversosL[0][0]
    else:
        valor_diversos = 0

    valor_pacote = valor_vela + valor_pote + valor_pavio + valor_ilhos + valor_etiqueta + valor_adesivo + valor_outros + valor_diversos
    venda = valor_pacote + (valor_pacote * float(margem)/100)

    programa3_alterar_pacote.pacote_custo_2.setText(str("{:.2f}".format(valor_pacote)))
    programa3_alterar_pacote.pacote_venda_2.setText(str("{:.2f}".format(venda)))

def alterar_pacote():
    if(programa3.tabela_pacotes.selectedIndexes()):
        programa3_alterar_pacote.show()

        programa3_alterar_pacote.pacote_vela_2.clear() 
        programa3_alterar_pacote.pacote_vela_2.addItems(combobox_pacote_vela()) 
        programa3_alterar_pacote.pacote_pote_2.clear() 
        programa3_alterar_pacote.pacote_pote_2.addItems(combobox_pacote_pote()) 
        programa3_alterar_pacote.pacote_pavio_2.clear() 
        programa3_alterar_pacote.pacote_pavio_2.addItems(combobox_pacote_pavio()) 
        programa3_alterar_pacote.pacote_ilhos_2.clear() 
        programa3_alterar_pacote.pacote_ilhos_2.addItems(combobox_pacote_ilhos()) 
        programa3_alterar_pacote.pacote_etiqueta_2.clear() 
        programa3_alterar_pacote.pacote_etiqueta_2.addItems(combobox_pacote_etiqueta()) 
        programa3_alterar_pacote.pacote_adesivo_2.clear() 
        programa3_alterar_pacote.pacote_adesivo_2.addItems(combobox_pacote_adesivo()) 
        programa3_alterar_pacote.pacote_outros_2.clear() 
        programa3_alterar_pacote.pacote_outros_2.addItems(combobox_pacote_outros())
        programa3_alterar_pacote.pacote_diversos_2.clear() 
        programa3_alterar_pacote.pacote_diversos_2.addItems(combobox_pacote_diversos())

        linha = programa3.tabela_pacotes.currentRow() 

        resposta = ConexoesBD.listaPacotes()

        programa3_alterar_pacote.pacote_nome_2.setText(str(resposta[linha][1]))
        programa3_alterar_pacote.pacote_custo_2.setText(str(resposta[linha][12]))
        programa3_alterar_pacote.pacote_venda_2.setText(str(resposta[linha][13]))
        programa3_alterar_pacote.pacote_margem_2.setText("0.00")

        #PRE-DEFINIR ITEM COMBOBOX
        item_atual_bd = resposta[linha][2]
        if item_atual_bd in combobox_pacote_vela():
            indice1 = combobox_pacote_vela().index(item_atual_bd)
            programa3_alterar_pacote.pacote_vela_2.setCurrentIndex(indice1)
        else:
            programa3_alterar_pacote.pacote_vela_2.setCurrentIndex(0)

        item_atual_bd = resposta[linha][3]
        if item_atual_bd in combobox_pacote_pote():
            indice2 = combobox_pacote_pote().index(item_atual_bd)
            programa3_alterar_pacote.pacote_pote_2.setCurrentIndex(indice2)
        else:
            programa3_alterar_pacote.pacote_pote_2.setCurrentIndex(0)

        item_atual_bd = resposta[linha][4]
        if item_atual_bd in combobox_pacote_pavio():
            indice3 = combobox_pacote_pavio().index(item_atual_bd)
            programa3_alterar_pacote.pacote_pavio_2.setCurrentIndex(indice3)
        else:
            programa3_alterar_pacote.pacote_pavio_2.setCurrentIndex(0)
        
        item_atual_bd = resposta[linha][5]
        if item_atual_bd in combobox_pacote_ilhos():
            indice4 = combobox_pacote_ilhos().index(item_atual_bd)
            programa3_alterar_pacote.pacote_ilhos_2.setCurrentIndex(indice4)
        else:
            programa3_alterar_pacote.pacote_ilhos_2.setCurrentIndex(0)

        item_atual_bd = resposta[linha][6]
        if item_atual_bd in combobox_pacote_etiqueta():
            indice5 = combobox_pacote_etiqueta().index(item_atual_bd)
            programa3_alterar_pacote.pacote_etiqueta_2.setCurrentIndex(indice5)
        else:
            programa3_alterar_pacote.pacote_etiqueta_2.setCurrentIndex(0)

        item_atual_bd = resposta[linha][7]
        if item_atual_bd in combobox_pacote_adesivo():
            indice6 = combobox_pacote_adesivo().index(item_atual_bd)
            programa3_alterar_pacote.pacote_adesivo_2.setCurrentIndex(indice6)
        else:
            programa3_alterar_pacote.pacote_adesivo_2.setCurrentIndex(0)
        
        item_atual_bd = resposta[linha][8]
        if item_atual_bd in combobox_pacote_outros():
            indice7 = combobox_pacote_outros().index(item_atual_bd)
            programa3_alterar_pacote.pacote_outros_2.setCurrentIndex(indice7)
        else:
            programa3_alterar_pacote.pacote_outros_2.setCurrentIndex(0)
        if item_atual_bd in combobox_pacote_diversos():
            indice7 = combobox_pacote_diversos().index(item_atual_bd)
            programa3_alterar_pacote.pacote_diversos_2.setCurrentIndex(indice7)
        else:
            programa3_alterar_pacote.pacote_diversos_2.setCurrentIndex(0)

    else:
         QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")

def botao_salvar_alterar_pacote():
    if (programa3_alterar_pacote.pacote_nome_2.text() == ""):
        QMessageBox.about(programa3_alterar_pacote, "Mensagem", "Nenhum nome foi definido para o produto.")
    elif (programa3_alterar_pacote.pacote_vela_2.currentText() == "" and programa3_alterar_pacote.pacote_pote_2.currentText() == "" and programa3_alterar_pacote.pacote_pavio_2.currentText() == ""\
        and programa3_alterar_pacote.pacote_ilhos_2.currentText() == "" and programa3_alterar_pacote.pacote_etiqueta_2.currentText() == "" and programa3_alterar_pacote.pacote_adesivo_2.currentText() == ""\
        and programa3_alterar_pacote.pacote_outros_2.currentText() == "" and programa3_alterar_pacote.pacote_diversos_2.currentText() == ""):
        QMessageBox.about(programa3_alterar_pacote, "Mensagem", "Preencha algum campo alem do nome.")
    elif(programa3_alterar_pacote.pacote_custo_2.text() == "0.00"):
        QMessageBox.about(programa3_alterar_pacote, "Mensagem", "Calcule o valor antes de salvar.")
    else:
        nome = programa3_alterar_pacote.pacote_nome_2.text()
        vela = programa3_alterar_pacote.pacote_vela_2.currentText()
        pote = programa3_alterar_pacote.pacote_pote_2.currentText()
        pavio = programa3_alterar_pacote.pacote_pavio_2.currentText()
        ilhos = programa3_alterar_pacote.pacote_ilhos_2.currentText()
        etiqueta = programa3_alterar_pacote.pacote_etiqueta_2.currentText()
        adesivo = programa3_alterar_pacote.pacote_adesivo_2.currentText()
        outros = programa3_alterar_pacote.pacote_outros_2.currentText()
        diversos = programa3_alterar_pacote.pacote_diversos_2.currentText()
        preco_custo = programa3_alterar_pacote.pacote_custo_2.text()
        preco_venda = programa3_alterar_pacote.pacote_venda_2.text()

        linha = programa3.tabela_pacotes.currentRow() + 1
        ConexoesBD.setUpdatepacote(nome, vela, pote, pavio, ilhos, etiqueta, adesivo, outros, diversos, preco_custo, preco_venda, linha)
        ResetFields.resetPacote_2(programa3_alterar_pacote)
        programa3_alterar_pacote.pacote_vela_2.clear() 
        programa3_alterar_pacote.pacote_vela_2.addItems(combobox_pacote_vela()) 
        programa3_alterar_pacote.pacote_pote_2.clear() 
        programa3_alterar_pacote.pacote_pote_2.addItems(combobox_pacote_pote()) 
        programa3_alterar_pacote.pacote_pavio_2.clear() 
        programa3_alterar_pacote.pacote_pavio_2.addItems(combobox_pacote_pavio()) 
        programa3_alterar_pacote.pacote_ilhos_2.clear() 
        programa3_alterar_pacote.pacote_ilhos_2.addItems(combobox_pacote_ilhos()) 
        programa3_alterar_pacote.pacote_etiqueta_2.clear() 
        programa3_alterar_pacote.pacote_etiqueta_2.addItems(combobox_pacote_etiqueta()) 
        programa3_alterar_pacote.pacote_adesivo_2.clear() 
        programa3_alterar_pacote.pacote_adesivo_2.addItems(combobox_pacote_adesivo()) 
        programa3_alterar_pacote.pacote_outros_2.clear() 
        programa3_alterar_pacote.pacote_outros_2.addItems(combobox_pacote_outros()) 
        programa3_alterar_pacote.pacote_diversos_2.clear() 
        programa3_alterar_pacote.pacote_diversos_2.addItems(combobox_pacote_diversos()) 

        #Reinicializacao da tabela
        programa3.tabela_pacotes.clear()
        botao_lista_pacotes()

        QMessageBox.about(programa3_alterar_pacote, "Mensagem", "Produto atualizado com sucesso.")
        programa3_alterar_pacote.close()

def botao_novo_pedido():
    programa4.frame_montar_pedido.show()
    programa4.frame_pedidos_inicio.close()
    programa4.frame_lista_pedidos.close()

    programa4.tabela_produtos_pedido.setColumnCount(3)
    programa4.tabela_produtos_pedido.setColumnWidth(0, 315)
    programa4.tabela_produtos_pedido.setColumnWidth(1, 110)
    programa4.tabela_produtos_pedido.setColumnWidth(2, 110)
    programa4.tabela_produtos_pedido.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    programa4.tabela_produtos_pedido.setHorizontalHeaderLabels(["Produto", "Custo", "Venda"]) 

    programa4.pedido_custo.setText("0.00")
    programa4.pedido_venda.setText("0.00")

def botao_historico_pedido():
    programa4.frame_lista_pedidos.show()
    programa4.frame_montar_pedido.close()
    programa4.frame_pedidos_inicio.close()

    programa4.frame_lista_pedidos.show()

    resposta = ConexoesBD.listaPedidos()

    qtd_linhas = len(resposta)
    programa4.tabela_pedidos.setRowCount(qtd_linhas)
    programa4.tabela_pedidos.setColumnCount(6)
    programa4.tabela_pedidos.setColumnWidth(0, 200)
    programa4.tabela_pedidos.setColumnWidth(1, 50)
    programa4.tabela_pedidos.setColumnWidth(2, 50)
    programa4.tabela_pedidos.setColumnWidth(3, 50)
    programa4.tabela_pedidos.setColumnWidth (4, 500)
    programa4.tabela_pedidos.setColumnWidth (5, 100)
    programa4.tabela_pedidos.setEditTriggers(QAbstractItemView.NoEditTriggers)
    programa4.tabela_pedidos.setHorizontalHeaderLabels(["Nome", "Dia", "Mes", "Ano", "Produtos", "Preco de Venda"])

    linha = 0

    while linha<len(resposta):
        programa4.tabela_pedidos.setItem(linha, 0, QTableWidgetItem(resposta[linha][1]))
        programa4.tabela_pedidos.setItem(linha, 1, QTableWidgetItem(resposta[linha][2]))
        programa4.tabela_pedidos.setItem(linha, 2, QTableWidgetItem(resposta[linha][3]))
        programa4.tabela_pedidos.setItem(linha, 3, QTableWidgetItem(resposta[linha][4]))
        lista_velas = resposta[linha][5]
        lista_velas = lista_velas.replace("'", "")
        lista_velas = lista_velas.replace("[", "")
        lista_velas = lista_velas.replace("]", "")
        lista_velas = lista_velas.replace(", ", "\n")
        programa4.tabela_pedidos.setItem(linha, 4, QTableWidgetItem(lista_velas))
        programa4.tabela_pedidos.setItem(linha, 5, QTableWidgetItem("R$" + "{:.2f}".format(float(str(resposta[linha][7])))))
        programa4.tabela_pedidos.item(linha, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        programa4.tabela_pedidos.item(linha, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        programa4.tabela_pedidos.item(linha, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        programa4.tabela_pedidos.item(linha, 5).setTextAlignment(QtCore.Qt.AlignCenter)
        linha += 1

def botao_voltar_inicio_montar_pedido():
    programa4.frame_pedidos_inicio.show()
    programa4.frame_lista_pedidos.close()
    programa4.frame_montar_pedido.close()

def botao_voltar_inicio_lista_pedidos():
    programa4.frame_pedidos_inicio.show()
    programa4.frame_lista_pedidos.close()
    programa4.frame_montar_pedido.close()

def inserir_produto_pedido():
    programa4_inserir_produto_pedido.show()

    programa4_inserir_produto_pedido.lista_pacotes.clear()
    programa4_inserir_produto_pedido.lista_pacotes.addItems(combobox_lista_pacotes())

lista_produtos_pedido = []

def botao_salvar_inserir_produto():
    produto = programa4_inserir_produto_pedido.lista_pacotes.currentText()
    lista = ConexoesBD.listaPacotes()
    if (produto != ""):
        linha_combobox = combobox_lista_pacotes().index(produto)
        custo = lista[linha_combobox-1][13]
        venda = lista[linha_combobox-1][14]
    else:
        custo = 0
        venda = 0

    qtd_linhas = len(lista_produtos_pedido) + 1
    programa4.tabela_produtos_pedido.setRowCount(qtd_linhas)
    programa4.tabela_produtos_pedido.setColumnCount(3)
    programa4.tabela_produtos_pedido.setColumnWidth(0, 315)
    programa4.tabela_produtos_pedido.setColumnWidth(1, 110)
    programa4.tabela_produtos_pedido.setColumnWidth(2, 110)
    programa4.tabela_produtos_pedido.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    programa4.tabela_produtos_pedido.setHorizontalHeaderLabels(["Produto", "Custo", "Venda"])    
    programa4.tabela_produtos_pedido.setItem(len(lista_produtos_pedido), 0, QTableWidgetItem(produto))
    programa4.tabela_produtos_pedido.setItem(len(lista_produtos_pedido), 1, QTableWidgetItem("R$" + "{:.2f}".format(float(str(custo)))))
    programa4.tabela_produtos_pedido.setItem(len(lista_produtos_pedido), 2, QTableWidgetItem("R$" + "{:.2f}".format(float(str(venda)))))
    programa4.tabela_produtos_pedido.item(len(lista_produtos_pedido), 1).setTextAlignment(QtCore.Qt.AlignCenter) 
    programa4.tabela_produtos_pedido.item(len(lista_produtos_pedido), 2).setTextAlignment(QtCore.Qt.AlignCenter)
    
    lista_produtos_pedido.append([produto, custo, venda])

def deletar_produto_pedido():
    if(programa4.tabela_produtos_pedido.selectedIndexes()):
        linha = programa4.tabela_produtos_pedido.currentRow()

        del lista_produtos_pedido[linha]
        indice = programa4.tabela_produtos_pedido.selectedIndexes()[0]
        programa4.tabela_produtos_pedido.removeRow(indice.row())
    else:
        QMessageBox.about(programa4, "Mensagem", "Nenhuma linha selecionada.")

def alterar_produto_pedido():
    if(programa4.tabela_produtos_pedido.selectedIndexes()):
        programa4_alterar_produto_pedido.show()

        programa4_alterar_produto_pedido.lista_pacotes.clear()
        programa4_alterar_produto_pedido.lista_pacotes.addItems(combobox_lista_pacotes())

        ##PRE-DEFINIR ITENS
        linha = programa4.tabela_produtos_pedido.currentRow() 
        item_atual_bd = lista_produtos_pedido[linha][0]

        if item_atual_bd in combobox_lista_pacotes():
            indice1 = combobox_lista_pacotes().index(item_atual_bd)
            programa4_alterar_produto_pedido.lista_pacotes.setCurrentIndex(indice1)
        else:
            programa4_alterar_produto_pedido.lista_pacotes.setCurrentIndex(0)
    else:
        QMessageBox.about(programa4, "Mensagem", "Nenhuma linha selecionada.")

def botao_salvar_alterar_produto():
    linha = programa4.tabela_produtos_pedido.currentRow() 
    produto1 = lista_produtos_pedido[linha][0]
    custo1 = lista_produtos_pedido[linha][1]
    venda1 = lista_produtos_pedido[linha][2]
    produto2 = programa4_alterar_produto_pedido.lista_pacotes.currentText()

    if(produto2 != ""):
        preco_pacote = ConexoesBD.listaPacotesValorProduto(produto2)
        custo2 = preco_pacote[0][0]
        venda2 = preco_pacote[0][1]
    else:
        custo2 = 0
        venda2 = 0

    indice_anterior = lista_produtos_pedido.index([produto1, custo1, venda1])

    lista_produtos_pedido[indice_anterior] = [produto2, custo2, venda2] 

    #REINICIANDO TABELA
    programa4.tabela_produtos_pedido.setItem(linha, 0, QTableWidgetItem(produto2))
    programa4.tabela_produtos_pedido.setItem(linha, 1, QTableWidgetItem("R$" + "{:.2f}".format(float(str(custo2)))))
    programa4.tabela_produtos_pedido.setItem(linha, 2, QTableWidgetItem("R$" + "{:.2f}".format(float(str(venda2)))))
    programa4.tabela_produtos_pedido.item(linha, 1).setTextAlignment(QtCore.Qt.AlignCenter)
    programa4.tabela_produtos_pedido.item(linha, 2).setTextAlignment(QtCore.Qt.AlignCenter) 
   
    programa4_alterar_produto_pedido.close()

def pedido_calculo():
    if(programa4.ecobag_pedido.text() == ""):
        qtd_ecobag = 0
    else:
        qtd_ecobag = programa4.ecobag_pedido.text()
    if(programa4.cartoes_pedido.text() == ""):
        qtd_cartoes = 0
    else:
        qtd_cartoes = programa4.cartoes_pedido.text()
    if(programa4.tag_pedido.text() == ""):
        qtd_tag = 0
    else:
        qtd_tag = programa4.tag_pedido.text()
    if(programa4.caixa_pedido.text() == ""):
        qtd_caixa = 0
    else:
        qtd_caixa = programa4.caixa_pedido.text()
    try:
        float(qtd_ecobag)
        float(qtd_cartoes)
        float(qtd_tag)
        float(qtd_caixa)
    except ValueError:
        QMessageBox.about(programa4, "Mensagem", "Existem palavaras escritas nos campos de valores")
    else:
        soma_pacotes_custo = 0
        soma_pacotes_venda = 0
        i = 0
        while i < len(lista_produtos_pedido):
            soma_pacotes_custo += lista_produtos_pedido[i][1]
            soma_pacotes_venda += lista_produtos_pedido[i][2]
            i += 1
        
        lista_ecobag = ConexoesBD.calculo_valor_itens("Ecobag")
        ecobag = lista_ecobag[0][0]
        lista_cartoes = ConexoesBD.calculo_valor_itens("Cartoes Agradecimento")
        cartoes = lista_cartoes[0][0]
        lista_tag = ConexoesBD.calculo_valor_itens("Tag")
        tag = lista_tag[0][0]
        lista_caixa = ConexoesBD.calculo_valor_itens("Caixa")
        caixa = lista_caixa[0][0]

        custo_total = soma_pacotes_custo + (ecobag * int(qtd_ecobag)) + (cartoes * int(qtd_cartoes)) + (tag * int(qtd_tag)) + (caixa * int(qtd_caixa))

        venda_total = soma_pacotes_venda + (ecobag * int(qtd_ecobag)) + (cartoes * int(qtd_cartoes)) + (tag * int(qtd_tag)) + (caixa * int(qtd_caixa))

        programa4.pedido_custo.setText(str("{:.2f}".format(custo_total)))
        programa4.pedido_venda.setText(str("{:.2f}".format(venda_total)))

def salvar_pedido():
    if(programa4.pedido_venda.text() == "0.00"):
        QMessageBox.about(programa4, "Mensagem", "Calcule o pedido antes de salvar.")
    else:
        programa4_salvar_pedido.show()

def salvar_pedidoBD():
    nome = programa4_salvar_pedido.nome.text()
    dia = programa4_salvar_pedido.dia_pedido.text()
    mes = programa4_salvar_pedido.mes_pedido.text()
    ano = programa4_salvar_pedido.ano_pedido.text()
    custo = programa4.pedido_custo.text()
    venda = programa4.pedido_venda.text()

    if (nome == "" or dia == "" or mes == "" or ano == ""):
        QMessageBox.about(programa4_salvar_pedido, "Mensagem", "Preencha todos os campos.")
    else:
        try:
            int(dia)
            int(mes)
            int(ano)
        except ValueError:
            QMessageBox.about(programa4_salvar_pedido, "Mensagem", "Insira valores validos para a data.")
        else:
            if (int(mes) > 12 or int(mes) <= 0):
                QMessageBox.about(programa4_salvar_pedido, "Mensagem", "Insira um valor de 01 a 12 para o mes.")
            elif (int(ano) <= 0):
                QMessageBox.about(programa4_salvar_pedido, "Mensagem", "Insira um valor maior que 0 para o ano.")
            elif (len(ano) != 4):
                QMessageBox.about(programa4_salvar_pedido, "Mensagem", "O ano deve conter quatro digitos.")
            elif (len(mes) != 2):
                QMessageBox.about(programa4_salvar_pedido, "Mensagem", "O mes deve conter dois digitos.")
            else:
                produtos = []
                i = 0
                while i < len(lista_produtos_pedido):
                    produtos.append(lista_produtos_pedido[i][0])
                    i += 1

                ConexoesBD.salvar_pedido(nome, dia, mes, ano, produtos, custo, venda)
                QMessageBox.about(programa4_salvar_pedido, "Mensagem", "Pedido salvo com sucesso.")

                programa4_salvar_pedido.close()
                programa4_salvar_pedido.nome.clear()
                programa4_salvar_pedido.dia_pedido.clear()
                programa4_salvar_pedido.mes_pedido.clear()
                programa4_salvar_pedido.ano_pedido.clear()
                programa4.tabela_produtos_pedido.clear()
                ResetFields.resetSalvarPedido(programa4)
                lista_produtos_pedido.clear()
                programa4.tabela_produtos_pedido.setRowCount(0)
                programa4.tabela_produtos_pedido.setColumnWidth(0, 315)
                programa4.tabela_produtos_pedido.setColumnWidth(1, 110)
                programa4.tabela_produtos_pedido.setColumnWidth(2, 110)
                programa4.tabela_produtos_pedido.setHorizontalHeaderLabels(["Produto", "Custo", "Venda"])  

def botao_deletar_pedido():
    if(programa4.tabela_pedidos.selectedIndexes()):
        linha = programa4.tabela_pedidos.currentRow()
        id_pedido = linha + 1
    
        ConexoesBD.delPedido(id_pedido)

        indice = programa4.tabela_pedidos.selectedIndexes()[0]
        programa4.tabela_pedidos.removeRow(indice.row())
    else:
        QMessageBox.about(programa6,"Mensagem" ,"Nenhuma linha selecionada.")

def gerar_relatorio():
    nome_arquivo = programa5.nome_relatorio.text()
    mes = programa5.mes_relatorio.text()
    ano = programa5.ano_relatorio.text()

    try:
        int(mes)
        int(ano)
    except ValueError:
        QMessageBox.about(programa5, "Mensagem", "Insira valores validos para a data.")
    else:
        if (int(mes) > 12 or int(mes) <= 0):
                QMessageBox.about(programa5, "Mensagem", "Insira um valor de 01 a 12 para o mes.")
        #elif ("'\'" or "/" or ":" or "?" or '"' or "<" or ">" or "|" or "*" in nome_arquivo):
            #QMessageBox.about(programa5, "Mensagem", "O nome do documento nao pode conter caracteres especiais.")
        elif (int(ano) <= 0):
            QMessageBox.about(programa5, "Mensagem", "Insira um valor maior que 0 para o ano.")
        elif (len(ano) != 4):
            QMessageBox.about(programa5, "Mensagem", "O ano deve conter quatro digitos.")
        elif (len(mes) != 2):
            QMessageBox.about(programa5, "Mensagem", "O mes deve conter dois digitos.")
        else:
            meses = {
            "01": "JANEIRO",
            "02": "FEVEREIRO",
            "03": "MARCO",
            "04": "ABRIL",
            "05": "MAIO",
            "06": "JUNHO",
            "07": "JULHO",
            "08": "AGOSTO",
            "09": "SETEMBRO",
            "10": "OUTRUBRO",
            "11": "NOVEMBRO",
            "12": "DEZEMBRO"
            }

            if mes in meses:
                nome_mes = meses[mes]

            cnv = canvas.Canvas(f"C:/Users/rafae/Documents/RAFAEL DOC/ESTUDOS TI/PROJETO CALMARE/Projeto Calmare/RELATORIOS/{nome_arquivo}.pdf", pagesize = A4)
            cnv.rect(10, 10, 575, 821)
            cnv.drawImage("titulo_janela.png", 17, 739, width= 561, height= 80)
            cnv.drawString(220, 700, f"Relatorio de {nome_mes} de {ano}")
            cnv.drawString(40, 650, "NOME DO PEDIDO")
            cnv.drawString(220, 650, "DIA")
            cnv.drawString(280, 650, "MES")
            cnv.drawString(340, 650, "ANO")
            cnv.drawString(400, 650, "CUSTO")
            cnv.drawString(460, 650, "VENDA")
            
            lista = ConexoesBD.relatorio(mes, ano)
            i = 0
            k = 0
            while k < len(lista):
                nome_pedido = lista[k][1]
                dia_pedido = lista[k][2]
                mes_pedido = lista[k][3]
                ano_pedido = lista[k][4]
                custo_pedido = lista[k][6]
                venda_pedido = lista[k][7]

                cnv.drawString(40, 600 - 20*i, f"{nome_pedido}")
                cnv.drawString(220, 600 - 20*i, f"{dia_pedido}")
                cnv.drawString(280, 600 - 20*i, f"{mes_pedido}")
                cnv.drawString(340, 600 - 20*i, f"{ano_pedido}")
                cnv.drawString(400, 600 - 20*i, f"{custo_pedido}")
                cnv.drawString(460, 600 - 20*i, f"{venda_pedido}")
                i += 1
                k += 1

                if (600 - 20*i) <= 0:
                    cnv.showPage()
                    cnv.rect(10, 10, 575, 821)
                    cnv.drawImage("titulo_janela.png", 17, 739, width= 561, height= 80)
                    cnv.drawString(220, 700, f"Relatorio de {nome_mes}")
                    cnv.drawString(40, 650, "NOME DO PEDIDO")
                    cnv.drawString(220, 650, "DIA")
                    cnv.drawString(280, 650, "MES")
                    cnv.drawString(340, 650, "ANO")
                    cnv.drawString(400, 650, "CUSTO")
                    cnv.drawString(460, 650, "VENDA")
                    i = 0
            
            j = 0
            custo_total = 0
            venda_total = 0
            while j < len(lista):
                custo_total += lista[j][6]
                venda_total += lista[j][7]
                j += 1

            cnv.drawString(40, 600 - 20*(i+1), "Custo Total: " + "{:.2f}".format(float(f"{custo_total}")))
            cnv.drawString(40, 600 - 20*(i+2), "Receita Total: " + "{:.2f}".format(float(f"{venda_total}")))
            cnv.drawString(40, 600 - 20*(i+3), "Lucro: " + "{:.2f}".format(float(f"{(venda_total - custo_total)}")))

            cnv.save()
            
            QMessageBox.about(programa5,"Mensagem" ,"Documento criado com sucesso.")
            programa5.nome_relatorio.clear()
            programa5.mes_relatorio.clear()
            programa5.ano_relatorio.clear()
       
#FUNCIONALIDADES BOTOES LOGIN
programa.botao_login_cadastrar.clicked.connect(abrir_frame_cadastro)
programa.botao_login_salvar.clicked.connect(salvar_cadastro)
programa.botao_login_voltar.clicked.connect(botao_login_voltar)
programa.botao_login.clicked.connect(botao_login)

#FUNCIONALIDADES BOTOES INICIO
programa2.botao_cadastrar_pacote.clicked.connect(botao_cadastrar_pacote)
programa2.botao_cadastrar_pedido.clicked.connect(botao_cadastrar_pedido)
programa2.botao_relatorio.clicked.connect(botao_relatorio)
programa2.botao_montar_produtos.clicked.connect(botao_montar_produtos)

#FUNCIONALIDADES BOTOES MONTAR PRODUTOS
programa6.botao_montar_velas.clicked.connect(botao_montar_velas)
programa6.botao_voltar_montarprod_velas.clicked.connect(botao_voltar_montarprod_velas)
programa6.botao_lista_velas.clicked.connect(botao_lista_velas)
programa6.botao_cadastrar_nova_vela.clicked.connect(botao_cadastrar_nova_vela)
programa6.botao_salvar_nova_vela.clicked.connect(botao_salvar_nova_vela)
programa6.botao_montar_essencias.clicked.connect(botao_montar_essencias)
programa6.botao_voltar_montarprod_essencias.clicked.connect(botao_voltar_montarprod_essencias)
programa6.botao_cadastrar_nova_essencia.clicked.connect(botao_cadastrar_nova_essencia)
programa6.botao_lista_essencias.clicked.connect(botao_lista_essencias)
programa6.botao_salvar_nova_essencia.clicked.connect(botao_salvar_nova_essencia)
programa6.botao_deletar_essencia.clicked.connect(deletar_essencia)
programa6.botao_alterar_essencia.clicked.connect(alterar_essencia)
programa6.botao_deletar_vela.clicked.connect(deletar_vela)
programa6.botao_alterar_vela.clicked.connect(alterar_vela)
programa6_alterar_essencia.botao_salvar_alterar_essencia.clicked.connect(botao_salvar_alterar_essencia)
programa6_alterar_vela.botao_salvar_alterar_vela.clicked.connect(botao_salvar_alterar_vela)
programa6.botao_montar_itens.clicked.connect(botao_montar_itens)
programa6.botao_voltar_montarprod_itens.clicked.connect(botao_voltar_montarprod_itens)
programa6.botao_item_pote.clicked.connect(botao_item_pote)
programa6.botao_item_pavio.clicked.connect(botao_item_pavio)
programa6.botao_item_adesivo.clicked.connect(botao_item_adesivo)
programa6.botao_item_etiquetas.clicked.connect(botao_item_etiquetas)
programa6.botao_item_ilhos.clicked.connect(botao_item_ilhos)
programa6.botao_item_outros.clicked.connect(botao_item_outros)
programa6.botao_item_ectg.clicked.connect(botao_item_ectg)
programa6.botao_lista_itens.clicked.connect(botao_lista_itens)
programa6.botao_salvar_item_pote.clicked.connect(botao_salvar_item_pote)
programa6.botao_salvar_item_pavio.clicked.connect(botao_salvar_item_pavio)
programa6.botao_salvar_item_ilhos.clicked.connect(botao_salvar_item_ilhos)
programa6.botao_salvar_item_outros.clicked.connect(botao_salvar_item_outros)
programa6.botao_salvar_item_etiqueta.clicked.connect(botao_salvar_item_etiqueta)
programa6.botao_salvar_item_adesivo.clicked.connect(botao_salvar_item_adesivo)
programa6.botao_salvar_item_ectg.clicked.connect(botao_salvar_item_ectg)
programa6.botao_deletar_item.clicked.connect(deletar_item)
programa6.botao_alterar_item.clicked.connect(alterar_item)
programa6_alterar_item.botao_salvar_alterar_item.clicked.connect(botao_salvar_alterar_item)
programa6.botao_escolher_diversos.clicked.connect(botao_escolher_diversos)
programa6.botao_voltar_montarprod_diversos.clicked.connect(botao_voltar_montarprod_diversos)
programa6.botao_diversos_concreto.clicked.connect(botao_diversos_concreto)
programa7.botao_salvar_diversos_concreto.clicked.connect(botao_salvar_diversos_concreto)
programa3.botao_cadastrar_pacote.clicked.connect(cadastrar_pacote)
programa3.botao_lista_pacotes.clicked.connect(botao_lista_pacotes)
programa3.pacote_calculo.clicked.connect(botao_calcular_pacote)
programa3.pacote_salvar.clicked.connect(pacote_salvar)
programa3.botao_deletar_pacote.clicked.connect(deletar_pacote)
programa3_alterar_pacote.pacote_calculo_2.clicked.connect(botao_calcular_alterar_pacote)
programa3.botao_alterar_pacote.clicked.connect(alterar_pacote)
programa3_alterar_pacote.pacote_salvar_2.clicked.connect(botao_salvar_alterar_pacote)
programa4.botao_novo_pedido.clicked.connect(botao_novo_pedido)
programa4.botao_historico_pedido.clicked.connect(botao_historico_pedido)
programa4.botao_voltar_inicio_montar_pedido.clicked.connect(botao_voltar_inicio_montar_pedido)
programa4.botao_voltar_inicio_lista_pedido.clicked.connect(botao_voltar_inicio_lista_pedidos)
programa4.inserir_produto_pedido.clicked.connect(inserir_produto_pedido)
programa4_inserir_produto_pedido.botao_salvar_inserir_produto.clicked.connect(botao_salvar_inserir_produto)
programa4.deletar_produto_pedido.clicked.connect(deletar_produto_pedido)
programa4.alterar_produto_pedido.clicked.connect(alterar_produto_pedido)
programa4_alterar_produto_pedido.botao_salvar_alterar_produto.clicked.connect(botao_salvar_alterar_produto)
programa4.pedido_calculo.clicked.connect(pedido_calculo)
programa4.salvar_pedido.clicked.connect(salvar_pedido)
programa4_salvar_pedido.botao_salvar_pedido.clicked.connect(salvar_pedidoBD)
programa4.botao_deletar_pedido.clicked.connect(botao_deletar_pedido)
programa5.gerar_relatorio.clicked.connect(gerar_relatorio)

programa.show()
app.exec()