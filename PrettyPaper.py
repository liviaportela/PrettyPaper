from tkinter import *
import mysql.connector

conexaodb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "PrettyPaper"
)

cursordb = conexaodb.cursor()

class App:
    def __init__(self):
        self.root = Tk() 
        self.root.title("PrettyPaper")
        self.root.geometry("360x640+490+90")
        self.root.resizable(0,0)
        self.tela_splash()
        self.root.mainloop()

    #Tela de splash
    def tela_splash(self):
        self.splash = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.splash.place(x='0', y='0') # Cria uma tela secundária dentro da tela principal

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaSplash.png")
        self.Imagem = Label(self.splash, image=self.backgroundImg)
        self.Imagem.pack()

        self.splash.after(3000, self.tela_inicial)    

    #Tela inicial - Funcionário ou cliente
    def tela_inicial(self):
        self.splash.destroy()

        self.bemVindo = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.bemVindo.place(x='0', y='0') # Cria outra tela secundária dentro da tela principal

        self.backgroundImg = PhotoImage(file="Imagens\Background\Entrar.png")
        self.imgBotFunc = PhotoImage(file="Imagens\Botoes\Button_Funcionario.png")
        self.imgBotClie = PhotoImage(file="Imagens\Botoes\Button_Cliente.png")
        self.Imagem = Label(self.bemVindo, image=self.backgroundImg)
        self.Imagem.pack()

        self.botaoFunc = Button(self.bemVindo, bd=0, image=self.imgBotFunc, bg="#fff2f2", command=lambda: self.tela_login_func())
        self.botaoFunc.place(x=67, y=360)
        self.botaoUsuario = Button(self.bemVindo, bd=0, image=self.imgBotClie, bg="#fff2f2", command=lambda: self.tela_cliente())
        self.botaoUsuario.place(x=67, y=450)

    #Tela de Login ou cadastro do cliente
    def tela_cliente(self):
        self.bemVindo.destroy() # Destroy a tela secundária 
        self.entrar = Frame(self.root, width='360', height="640", bg='#fffff2') # Cria outra tela secundária dentro da tela principal
        self.entrar.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaEntrar.png")
        self.imgBotLogin = PhotoImage(file="Imagens\Botoes\Button_login.png")
        self.imgBotCad = PhotoImage(file="Imagens\Botoes\Button_cadastro.png")
        self.Imagem = Label(self.entrar, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.entrar, bd=0, image=self.imgBotVol, bg="#fff2f2", command=lambda: self.tela_inicial())
        self.BotVoltar.place(x=15, y=30)  
        self.botaoCad = Button(self.entrar, bd=0, image=self.imgBotCad, bg="#fff2f2", command=lambda: self.tela_cadastro())
        self.botaoCad.place(x=67, y=360)
        self.botaoLogin = Button(self.entrar, bd=0, image=self.imgBotLogin, bg="#fff2f2", command=lambda: self.tela_login())
        self.botaoLogin.place(x=67, y=450)

    #Tela de cadastro do cliente
    def tela_cadastro(self):
        self.entrar.destroy()
        self.cadastro = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.cadastro.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaCadastro.png")
        self.Imagem = Label(self.cadastro, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.cadastro, bd=0, image=self.imgBotVol, bg="#fff2f2", command=lambda: self.tela_cliente())
        self.BotVoltar.place(x=15,y=30)       
        self.LbNome = Label(self.cadastro, text="NOME", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbNome.place(x=35,y=180)  
        self.campoNome = Entry(self.cadastro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoNome.place(x=40,y=210)
        self.LbEmail = Label(self.cadastro, text="EMAIL", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbEmail.place(x=35,y=240)
        self.campoEmail = Entry(self.cadastro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoEmail.place(x=40,y=270)
        self.LbTel = Label(self.cadastro, text="TELEFONE", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbTel.place(x=35,y=300)
        self.campoTel = Entry(self.cadastro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoTel.place(x=40,y=330)
        self.LbSenha = Label(self.cadastro, text="SENHA", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbSenha.place(x=35,y=360)
        self.campoSenha = Entry(self.cadastro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove", show="*")
        self.campoSenha.place(x=40,y=390)
        self.imgBotEnt = PhotoImage(file="Imagens\Botoes\Button_entrar.png")
        self.botaoEnt = Button(self.cadastro, bd=0, image=self.imgBotEnt, bg="#fff2f2", command=lambda: self.cadastrar())
        self.botaoEnt.place(x=85,y=465)
        self.mensagem = Label(self.cadastro, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.mensagem.place(x=55,y=425)  

    #Tela de login do cliente
    def tela_login(self):
        self.bemVindo.destroy()

        self.login = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.login.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaLogin.png")
        self.Imagem = Label(self.login, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.login, bd=0, image=self.imgBotVol, bg="#fff2f2", command=lambda: self.tela_cliente())
        self.BotVoltar.place(x=15, y=30)
        self.LbEmailTel = Label(self.login, text="EMAIL OU TELEFONE", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbEmailTel.place(x=35,y=190)
        self.campoEmailTel = Entry(self.login, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoEmailTel.place(x=40,y=220)
        self.LbSenha = Label(self.login, text="SENHA", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbSenha.place(x=35,y=260)
        self.campoSenha = Entry(self.login, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove", show="*")
        self.campoSenha.place(x=40,y=290)
        self.mensagem = Label(self.login, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.mensagem.place(x=87, y=335)
        self.imgBotEnt = PhotoImage(file="Imagens\Botoes\Button_entrar.png")
        self.botaoEnt = Button(self.login, bd=0, image=self.imgBotEnt, bg="#fff2f2", command= self.loginCliente)
        self.botaoEnt.place(x=85, y=390)

    #Tela de login do Funcionário
    def tela_login_func(self):
        self.bemVindo.destroy()
        self.loginfunc = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.loginfunc.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaLogin.png")
        self.Imagem = Label(self.loginfunc, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.loginfunc, bd=0, image=self.imgBotVol, bg="#fff2f2", command=lambda: self.tela_inicial())
        self.BotVoltar.place(x=15, y=30)
        self.LbEmailTel = Label(self.loginfunc, text="EMAIL OU TELEFONE", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbEmailTel.place(x=35,y=190)
        self.campoEmailTel = Entry(self.loginfunc, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoEmailTel.place(x=40,y=220)
        self.LbSenha = Label(self.loginfunc, text="SENHA", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbSenha.place(x=35,y=260)
        self.campoSenha = Entry(self.loginfunc, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove", show="*")
        self.campoSenha.place(x=40,y=290)
        self.mensagem = Label(self.loginfunc, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.mensagem.place(x=87, y=335)
        self.imgBotEnt = PhotoImage(file="Imagens\Botoes\Button_entrar.png")
        self.botaoEnt = Button(self.loginfunc, bd=0, image=self.imgBotEnt, bg="#fff2f2", command= self.loginFuncio)
        self.botaoEnt.place(x=85, y=390)

    #Tela de home do cliente
    def tela_home(self):
        self.login.destroy()
        self.home = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.home.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaHome.png")
        self.Imagem = Label(self.home, image=self.backgroundImg)
        self.Imagem.pack()
            
        self.imgBotMenu = PhotoImage(file="Imagens\Botoes\Button_Menu.png")
        self.BotMenu = Button(self.home, bd=0, image=self.imgBotMenu, bg="#fff2f2", command=lambda: self.tela_menu())
        self.BotMenu.place(x=10, y=25)
        self.imgBotPerfil = PhotoImage(file="Imagens\Botoes\Button_Perfil.png")
        self.BotPerfil = Button(self.home, bd=0, image=self.imgBotPerfil, bg="#ffd0d0", command=lambda: self.tela_conta())
        self.BotPerfil.place(x=50, y=70)

        self.campoPesquisa= Entry(self.home, font="Bahnschrift 9", width=19, fg="#A6A6A6", bg="#fff", relief="flat")
        self.campoPesquisa.place(x=180,y=76)
        
        self.imgBotSkt = PhotoImage(file="Imagens\Botoes\Button_Sketchbooks.png")
        self.BotSkt = Button(self.home, bd=0, image=self.imgBotSkt, bg="#E19B95")
        self.BotSkt.place(x=10, y=103) 

        self.imgBotPr1 = PhotoImage(file="Imagens\Botoes\Button_Produto9.png")
        self.BotPr1 = Button(self.home, bd=0, image=self.imgBotPr1, bg="#fff2f2")
        self.BotPr1.place(x=10, y=280)    
        self.imgBotPr2 = PhotoImage(file="Imagens\Botoes\Button_Produto2.png")
        self.BotPr2 = Button(self.home, bd=0, image=self.imgBotPr2, bg="#fff2f2")
        self.BotPr2.place(x=120, y=280)
        self.imgBotPr3 = PhotoImage(file="Imagens\Botoes\Button_Produto3.png")
        self.BotPr3 = Button(self.home, bd=0, image=self.imgBotPr3, bg="#fff2f2")
        self.BotPr3.place(x=230, y=280)

    def tela_menu(self):
        self.home.destroy()
        self.menu = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.menu.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaMenu.png")
        self.Imagem = Label(self.menu, image=self.backgroundImg)
        self.Imagem.pack()  
        self.imgBotMenu = PhotoImage(file="Imagens\Botoes\Button_Menu.png")

        self.BotMenu = Button(self.menu, bd=0, image=self.imgBotMenu, bg="#fff2f2", command=lambda: self.tela_home())
        self.BotMenu.place(x=10, y=25)
        self.BotCont = Button(self.menu, bd=0, font="Arialle 9 bold", text="Contato", fg="#737373", bg="#fff2f2", command=lambda: self.tela_info_cont())
        self.BotCont.place(x=5, y=65)
        self.BotInfo = Button(self.menu, bd=0, font="Arialle 9 bold", text="Informações", fg="#737373", bg="#fff2f2", command=lambda: self.tela_info())
        self.BotInfo.place(x=5, y=95)
        self.BotPag = Button(self.menu, bd=0, font="Arialle 9 bold", text="Pagamento", fg="#737373", bg="#fff2f2", command=lambda: self.tela_info_pag())
        self.BotPag.place(x=5, y=125)
        self.BotEnt = Button(self.menu, bd=0, font="Arialle 9 bold", text="Entrega", fg="#737373", bg="#fff2f2", command=lambda: self.tela_info_ent())
        self.BotEnt.place(x=5, y=155)
        self.imgRedes = PhotoImage(file="Imagens\Botoes\ImgRedes.png")
        self.Redes = Label(self.menu, bd=0, image=self.imgRedes, bg="#fff2f2")
        self.Redes.place(x=14, y=173)

        self.BotEnt.place(x=5, y=155)
        self.campoPesquisa= Entry(self.menu, font="Bahnschrift 9", text="", width=19, fg="#A6A6A6", bg="#fff", relief="flat")
        self.campoPesquisa.place(x=180,y=75)
        self.imgBotPr1 = PhotoImage(file="Imagens\Botoes\Button_Produto9.png")
        self.BotPr1 = Button(self.menu, bd=0, image=self.imgBotPr1, bg="#fff2f2")
        self.BotPr1.place(x=10, y=280)        
        self.imgBotPr2 = PhotoImage(file="Imagens\Botoes\Button_Produto2.png")
        self.BotPr2 = Button(self.menu, bd=0, image=self.imgBotPr2, bg="#fff2f2")
        self.BotPr2.place(x=120, y=280) 
        self.imgBotPr3 = PhotoImage(file="Imagens\Botoes\Button_Produto3.png")
        self.BotPr3 = Button(self.menu, bd=0, image=self.imgBotPr3, bg="#fff2f2")
        self.BotPr3.place(x=230, y=280)

    #Tela de informações sobre o pagamento
    def tela_info_pag(self):
        self.menu.destroy()
        self.infoPag = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.infoPag.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaPagamento.png")
        self.Imagem = Label(self.infoPag, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.infoPag, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home())
        self.BotVoltar.place(x=15, y=30)

    #Tela de informações gerais 
    def tela_info(self):
        self.menu.destroy()
        self.pagInfo = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.pagInfo.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaInformacoes.png")
        self.Imagem = Label(self.pagInfo, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.pagInfo, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home())
        self.BotVoltar.place(x=15, y=30)

    #Tela de informações sobre entrega
    def tela_info_ent(self):
        self.menu.destroy()
        self.infoEntrega = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.infoEntrega.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaEntrega.png")
        self.Imagem = Label(self.infoEntrega, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.infoEntrega, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home())
        self.BotVoltar.place(x=15, y=30)

    #Tela de informações sobre contato
    def tela_info_cont(self):
        self.menu.destroy()
        self.infoCont = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.infoCont.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaContato.png")
        self.Imagem = Label(self.infoCont, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.infoCont, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home())
        self.BotVoltar.place(x=15, y=30)

    #Tela de home do funcionário
    def tela_home_func(self):
        self.loginfunc.destroy()
        self.homefunc = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.homefunc.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\HomeFunc.png")
        self.Imagem = Label(self.homefunc, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotPerfil = PhotoImage(file="Imagens\Botoes\Button_PerfilFunc.png")
        self.BotPerfil = Button(self.homefunc, bd=0, image=self.imgBotPerfil, bg="#F8D8E4", command=lambda: self.tela_conta_func())
        self.BotPerfil.place(x=295, y=30)

        self.imgBotCad = PhotoImage(file="Imagens\Botoes\Button_CadPro.png")
        self.BotCad = Button(self.homefunc, bd=0, image=self.imgBotCad, bg="#fff2f2", command=lambda: self.tela_cadastro_produtos())
        self.BotCad.place(x=70, y=250)
        self.imgBotAlt = PhotoImage(file="Imagens\Botoes\Button_AltPro.png")
        self.BotAlt = Button(self.homefunc, bd=0, image=self.imgBotAlt, bg="#fff2f2", command=lambda: self.tela_alterar_produtos())
        self.BotAlt.place(x=70, y=315)
        self.imgBotVer = PhotoImage(file="Imagens\Botoes\Button_Verificar.png")
        self.BotVer = Button(self.homefunc, bd=0, image=self.imgBotVer, bg="#fff2f2", command=lambda: self.tela_pedidos())
        self.BotVer.place(x=70, y=380)

    #Tela Conta
    def tela_conta(self):
        self.home.destroy()
        
        self.perfil = Frame(self.root, width='360', height="640", bg='#bbb')
        self.perfil.place(x='0', y='0') # Cria uma tela secundária dentro da tela principal

        self.backgroundImg = PhotoImage(file="Imagens\Background\Bg_conta.png")
        self.imgBotExc = PhotoImage(file="Imagens\Botoes\Bt_exclr.png")
        
        self.Imagem = Label(self.perfil, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.perfil, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home())
        self.BotVoltar.place(x=15, y=30)

        self.Nome = Label(self.perfil, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.Nome.place(x=35, y=285)

        self.Nome["text"] = {self.NomeCliente}
        self.Email["text"] = {self.EmailCliente}
        self.Nome["text"] = {self.TelefoneCliente}
        self.Nome["text"] = {self.SenhaCliente}

        self.botaoExc = Button(self.perfil, bd=0, image=self.imgBotExc, bg="#fff2f2", command=lambda: self.tela_excluir())
        self.botaoExc.place(x=120, y=520)

    def Dados(self):
        cmd= f'SELECT * FROM Clientes WHERE (EmailCliente = ("{self.email}")'
        cursordb.execute(cmd)
        resultado = cursordb.fetchall()
        i = 0

        if i < len(resultado):
            self.tela_home()
            return self.EmailCliente, self.SenhaCliente, self.NomeCliente, self.TelefoneCliente

    #Tela Conta
    def tela_conta_func(self):
        self.homefunc.destroy()
        self.perfil = Frame(self.root, width='360', height="640", bg='#bbb')
        self.perfil.place(x='0', y='0') # Cria uma tela secundária dentro da tela principal

        self.backgroundImg = PhotoImage(file="Imagens\Background\Bg_conta.png")
        self.imgBotExc = PhotoImage(file="Imagens\Botoes\Bt_exclr.png")
        self.Imagem = Label(self.perfil, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.perfil, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home_func())
        self.BotVoltar.place(x=15, y=30)
        self.Nome = Label(self.perfil, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.Nome.place(x=85, y=455)
        self.Email = Label(self.perfil, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.Email.place(x=85, y=455)
        self.Telefone = Label(self.perfil, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.Telefone.place(x=85, y=455)
        self.Senha = Label(self.perfil, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2",)
        self.Senha.place(x=85, y=455)

    #Tela de cadastro dos produtos
    def tela_cadastro_produtos(self):
        self.homefunc.destroy()
        self.cadastropro = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.cadastropro.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaCadastroProdutos.png")
        self.Imagem = Label(self.cadastropro, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.cadastropro, bd=0, image=self.imgBotVol, bg="#fff2f2", command=lambda: self.tela_home_func())
        self.BotVoltar.place(x=15,y=30)   
        self.LbDesc = Label(self.cadastropro, text="DESCRIÇÃO", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbDesc.place(x=35,y=180)  
        self.campoDescricao= Entry(self.cadastropro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoDescricao.place(x=40,y=210)
        self.LbCat = Label(self.cadastropro, text="CATEGORIA", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbCat.place(x=35,y=240)
        self.campoCategoria = Entry(self.cadastropro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoCategoria.place(x=40,y=270)
        self.LbVal = Label(self.cadastropro, text="VALOR", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbVal.place(x=35,y=300)
        self.campoValor = Entry(self.cadastropro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoValor.place(x=40,y=330)
        self.LbQtde = Label(self.cadastropro, text="QUANTIDADE", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbQtde.place(x=35,y=360)
        self.campoQuantidade = Entry(self.cadastropro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoQuantidade.place(x=40,y=390)
        self.imgBotCad = PhotoImage(file="Imagens\Botoes\BotCadPro.png")
        self.botaoCad = Button(self.cadastropro, bd=0, image=self.imgBotCad, bg="#fff2f2", command=lambda: self.cadastrar_produto())
        self.botaoCad.place(x=105,y=465)
        self.mensagem = Label(self.cadastropro, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.mensagem.place(x=55,y=425)  

    #Tela de alteração dos produtos
    def tela_alterar_produtos(self):
        self.homefunc.destroy()
        self.alterarpro = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.alterarpro.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaAlterar.png")
        self.Imagem = Label(self.alterarpro, image=self.backgroundImg)
        self.Imagem.pack()

        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.alterarpro, bd=0, image=self.imgBotVol, bg="#fff2f2", command=lambda: self.tela_home_func())
        self.BotVoltar.place(x=15,y=30)   
        self.LbId = Label(self.alterarpro, text="ID_PRODUTO", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbId.place(x=35,y=120)  
        self.campoId= Entry(self.alterarpro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoId.place(x=40,y=150)
        self.LbDesc = Label(self.alterarpro, text="DESCRIÇÃO", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbDesc.place(x=35,y=180)  
        self.campoDescricao= Entry(self.alterarpro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoDescricao.place(x=40,y=210)
        self.LbCat = Label(self.alterarpro, text="CATEGORIA", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbCat.place(x=35,y=240)
        self.campoCategoria = Entry(self.alterarpro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoCategoria.place(x=40,y=270)
        self.LbVal = Label(self.alterarpro, text="VALOR", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbVal.place(x=35,y=300)
        self.campoValor = Entry(self.alterarpro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoValor.place(x=40,y=330)
        self.LbQtde = Label(self.alterarpro, text="QUANTIDADE", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.LbQtde.place(x=35,y=360)
        self.campoQuantidade = Entry(self.alterarpro, font="Bahnschrift 15", width=25, fg="#A6A6A6", bg="#fff2f2", relief="groove")
        self.campoQuantidade.place(x=40,y=390)
        self.imgBotAlt = PhotoImage(file="Imagens\Botoes\Button_Alterar.png")
        self.botaoAlt = Button(self.alterarpro, bd=0, image=self.imgBotAlt, bg="#fff2f2", command=lambda: self.alterar_produto())
        self.botaoAlt.place(x=105,y=465)
        self.mensagem = Label(self.alterarpro, text="", font="Bahnschrift 15", fg="#A6A6A6", bg="#fff2f2")
        self.mensagem.place(x=55,y=425)  

    #Tela de pedidos
    def tela_pedidos(self):
        self.homefunc.destroy()
        self.pedidos = Frame(self.root, width='360', height="640", bg='#fffff2')
        self.pedidos.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\TelaPedidos.png")
        self.Imagem = Label(self.pedidos, image=self.backgroundImg)
        self.Imagem.pack()
        
        self.imgBotVoltar = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.pedidos, bd=0, image=self.imgBotVoltar, bg="#fff2f2", command=lambda: self.tela_home_func())
        self.BotVoltar.place(x=15, y=30) 
        
    #Tela Excluir    
    def tela_excluir(self):
        self.perfil.destroy() # Destroy a tela secundária 

        self.deletar = Frame(self.root, width='360', height="640", bg='#fffff2') # Cria outra tela secundária dentro da tela principal
        self.deletar.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\Bg_excluir_conta.png")
        self.imgBotSim = PhotoImage(file="Imagens\Botoes\Bt_exclr_sim.png")
        self.imgBotNao = PhotoImage(file="Imagens\Botoes\Bt_exclr_nao.png")

        self.Imagem = Label(self.deletar, image=self.backgroundImg)
        self.Imagem.pack()

        self.botaoSim = Button(self.deletar, bd=0, image=self.imgBotSim, bg="#fff2f2", command=lambda: self.excluir)
        self.botaoSim.place(x=70, y=340)
        self.botaoNao = Button(self.deletar, bd=0, image=self.imgBotNao, bg="#fff2f2", command=lambda: self.usuario)
        self.botaoNao.place(x=185, y=340)
    
    def Carrinho(self):
        self.conta.destroy()

        self.carrinho = Frame(self.root, width='360', height="640", bg='#bbb')
        self.carrinho.place(x='0', y='0')

        self.backgroundImg = PhotoImage(file="Imagens\Background\Bg_carrinho.png")
        self.Imagem = Label(image=self.backgroundImg).pack()
    
    #Cadastrar cliente
    def cadastrar(self):
        self.nome = self.campoNome.get()
        self.email = self.campoEmail.get()
        self.telefone = self.campoTel.get()
        self.senha = self.campoSenha.get()

        if self.nome or self.email or self.telefone or self.senha is None:
            cmd= f'INSERT INTO Clientes (NomeCliente,EmailCliente,TelefoneCliente,SenhaCliente) VALUES ("{self.nome}","{self.email}","{self.telefone}","{self.senha}")'
            cursordb.execute(cmd)
            conexaodb.commit()
            self.tela_login()
        else:
            self.mensagem["text"] = "Preencha todos os campos"

    #Verifica as informações de login do cliente
    def loginCliente(self):
        self.emailTel = self.campoEmailTel.get()
        self.senha = self.campoSenha.get()

        cmd= f'SELECT * FROM Clientes WHERE (EmailCliente = ("{self.emailTel}") OR TelefoneCliente = ("{self.emailTel}")) AND SenhaCliente = ("{self.senha}")'
        cursordb.execute(cmd)
        resultado = cursordb.fetchall()
        i = 0

        if i < len(resultado):
            self.tela_home()
        else:
            self.mensagem["text"] = "Erro na autenticação"
    
    #Excluir cliente
    def excluir(self):
        self.nome = self.Nome.get()

        cmd= f'DELETE FROM Clientes WHERE NomeCliente = {self.nome})'
        cursordb.execute(cmd)
        conexaodb.commit()

        self.tela_login()

    #Verifica as informações de login do funcionário
    def loginFuncio(self):
        self.emailTel = self.campoEmailTel.get()
        self.senha = self.campoSenha.get()

        cmd= f'SELECT * FROM Funcionários WHERE (EmailFunc = ("{self.emailTel}") OR TelefoneFunc = ("{self.emailTel}")) AND SenhaFunc = ("{self.senha}")'
        cursordb.execute(cmd)
        resultadofunc = cursordb.fetchall()
        i = 0

        if i < len(resultadofunc):
            self.tela_home_func()
        else:
            self.mensagem["text"] = "Erro na autenticação"

    #Cadastrar produto
    def cadastrar_produto(self):
        self.descricao = self.campoDescricao.get()
        self.categoria = self.campoCategoria.get()
        self.valor = self.campoValor.get()
        self.quantidade = self.campoQuantidade.get()

        if self.descricao or self.categoria or self.valor or self.quantidade is None:
            cmd= f'INSERT INTO Produtos (Descricao,Categoria,Valor,Quantidade) VALUES ("{self.descricao}","{self.categoria}","{self.valor}","{self.quantidade}")'
            cursordb.execute(cmd)
            conexaodb.commit()
            self.tela_home_func()
        else:
            self.mensagem["text"] = "Preencha todos os campos"

    #Alterar produto
    def alterar_produto(self):
        self.id = self.campoId.get()
        self.descricao = self.campoDescricao.get()
        self.categoria = self.campoCategoria.get()
        self.valor = self.campoValor.get()
        self.quantidade = self.campoQuantidade.get()

        if self.id or self.descricao or self.categoria or self.valor or self.quantidade is None:
            cmd= f'UPDATE Produtos SET Descricao = "{self.descricao}",Categoria = "{self.categoria}",Valor = "{self.valor}",Quantidade = "{self.quantidade}" WHERE ID_PRODUTO = "{self.id}"'
            cursordb.execute(cmd)
            conexaodb.commit()
            self.tela_home_func()
        else:
            self.mensagem["text"] = "Preencha todos os campos"      

App()
