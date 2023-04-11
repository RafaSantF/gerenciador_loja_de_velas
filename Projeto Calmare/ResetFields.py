def resetCombobox(janela, combobox):
    janela.combo_essencia_vela1.clear() #Campos para limpar a lista.
    janela.combo_essencia_vela2.clear()
    janela.combo_essencia_vela3.clear()  
    janela.combo_essencia_vela1.addItems(combobox) #Campos para inserir as essencias.
    janela.combo_essencia_vela2.addItems(combobox)
    janela.combo_essencia_vela3.addItems(combobox)

def resetVelas(janela, combobox):
    janela.produto.clear()
    janela.cera_g.clear()
    janela.cera_p.clear()
    janela.essencia1_g.clear()
    janela.essencia2_g.clear()
    janela.essencia3_g.clear()
    janela.combo_essencia_vela1.clear() #Campos para limpar a lista.
    janela.combo_essencia_vela2.clear()
    janela.combo_essencia_vela3.clear()  
    janela.combo_essencia_vela1.addItems(combobox) #Campos para inserir as essencias.
    janela.combo_essencia_vela2.addItems(combobox)
    janela.combo_essencia_vela3.addItems(combobox)

def resetEssencias(janela):
    janela.essencia.clear()
    janela.essencia_p.clear()

def resetLogin(janela):
    janela.usuario_login.clear()
    janela.senha_login.clear()

def resetCadastro(janela):
    janela.usuario_cadastrar.clear()
    janela.senha_cadastrar.clear()
    janela.senha_adm_cadastrar.clear()

def resetPote(janela):
    janela.item_pote.clear()
    janela.item_preco_pote.clear()

def resetPavio(janela):
    janela.item_pavio.clear()
    janela.item_preco_pavio.clear()

def resetIlhos(janela):
    janela.item_ilhos.clear()
    janela.item_preco_ilhos.clear()

def resetOutros(janela):
    janela.item_outros.clear()
    janela.item_preco_outros.clear()

def resetEtiqueta(janela):
    janela.item_etiqueta.clear()
    janela.item_preco_etiqueta.clear()

def resetAdesivo(janela):
    janela.item_adesivo.clear()
    janela.item_preco_adesivo.clear()

def resetEctg(janela):
    janela.item_preco_ecobag.clear()
    janela.item_preco_cartao.clear()
    janela.item_preco_tag.clear()
    janela.item_preco_caixa.clear()

def resetAlterarItens(janela):
    janela.item.clear()
    janela.item_p.clear()

def resetDiversosConcreto(janela):
    janela.diversos_concreto_nome.clear()
    janela.diversos_concreto_preco.clear()

def resetPacote(janela):
    janela.pacote_nome.clear()
    janela.pacote_custo.setText("0.00")
    janela.pacote_venda.setText("0.00")
    janela.pacote_margem.setText("0.00")

def resetPacote_2(janela):
    janela.pacote_nome_2.clear()
    janela.pacote_custo_2.setText("0.00")

def resetSalvarPedido(janela):
    janela.ecobag_pedido.clear()
    janela.cartoes_pedido.clear()
    janela.tag_pedido.clear()
    janela.caixa_pedido.clear()
    janela.pedido_custo.setText("0.00")
    janela.pedido_venda.setText("0.00")
    janela.tabela_produtos_pedido.clear()
    janela.tabela_produtos_pedido.setRowCount(0)
    janela.tabela_produtos_pedido.setColumnWidth(0, 315)
    janela.tabela_produtos_pedido.setColumnWidth(1, 110)
    janela.tabela_produtos_pedido.setColumnWidth(2, 110)
    janela.tabela_produtos_pedido.setHorizontalHeaderLabels(["Produto", "Custo", "Venda"])