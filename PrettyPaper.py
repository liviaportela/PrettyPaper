from tkinter import *

class App:
    def __init__(self):
        self.splash = Tk()
        self.splash.title("PrettyPaper - Splash")
        self.splash.geometry("360x640+490+90")
        self.splash.resizable(0,0)

        self.backgroundImg = PhotoImage(file="Imagens\TelaSplash.png")
        self.Imagem = Label(image=self.backgroundImg).pack()

        self.splash.after(3000, self.Entrar)
        self.splash.mainloop()

    def Entrar(self):
        self.splash.destroy()
        
        self.entrar = Tk()
        self.entrar.title("PrettyPaper - Entrar")
        self.entrar.geometry("360x640+490+90")
        self.entrar.resizable(0,0)

        self.backgroundImg = PhotoImage(file="Imagens\LogoCoracao.png")
        self.Imagem = Label(image=self.backgroundImg).pack()

        self.imgBotLogin = PhotoImage(file="Imagens\Botoes\Button_login.png")
        self.imgBotCad = PhotoImage(file="Imagens\Botoes\Button_cadastro.png")

        self.botaoCad = Button(self.entrar, bd=0, image=self.imgBotCad, bg="#fff2f2", command=self.Cadastrar).place(x=67, y=320)
        self.botaoLogin = Button(self.entrar, bd=0, image=self.imgBotLogin, bg="#fff2f2", command=self.Login).place(x=67, y=400)
        
    def Cadastrar(self):
        self.entrar.destroy()

        self.cadastro = Tk()
        self.cadastro.title("PrettyPaper - Cadastro")
        self.cadastro.geometry("360x640+490+90")
        self.cadastro.resizable(0,0)

        self.backgroundImg = PhotoImage(file="Imagens\Logo.png")
        self.Imagem = Label(image=self.backgroundImg).pack()

        self.imgBotVol = PhotoImage(file="Imagens\Botoes\Button_voltar.png")
        self.BotVoltar = Button(self.cadastro, bd=0, image=self.imgBotVol, bg="#fff2f2", command=self.Entrar).place(x=25, y=0)

        self.campoNome = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised").place(x=30,y=50)
        self.campoEmail = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised").place(x=30,y=90)
        self.campoTel = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised").place(x=30,y=130)
        self.campoSenha = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised", show="*").place(x=30,y=170)
        self.campoConfSen = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised", show="*").place(x=30,y=210)

        self.imgBotEnt = PhotoImage(file="Imagens\Botoes\Button_entrar.png")

        self.botaoEnt = Button(self.cadastro, bd=0, image=self.imgBotEnt, bg="#fff2f2", command=self.Login).place(x=25, y=260)

    def Login(self):
        self.entrar.destroy()

        self.login = Tk()
        self.login.title("PrettyPaper - Login")
        self.login.geometry("360x640+490+90")
        self.login.resizable(0,0)

        self.backgroundImg = PhotoImage(file="Imagens\Logo.png")
        self.Imagem = Label(image=self.backgroundImg).pack()
        
        self.campoNome = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised").place(x=27,y=140)
        self.campoSenha = Entry(font="Bahnschrift 15 bold", width=17, fg="#A6A6A6", bg="#fff2f2", relief="raised", show="*").place(x=27,y=210)
        self.rotRecSenha = Button(text="Esqueci minha senha", font="Bahnschrift 10 bold", width=17, bg="#fff2f2", fg="white", relief="flat", command=self.RecSenha).place(x=27,y=260)

        self.imgBotEnt = PhotoImage(file="Imagens\Botoes\Button_entrar.png")
        self.botaoEnt = Button(self.login, bd=0, image=self.imgBotEnt, bg="#fff2f2").place(x=26, y=310)
        
    def RecSenha(self):
        self.login.destroy()

        self.recsenha = Tk()
        self.recsenha.title("PrettyPaper - Recuperar Senha")
        self.recsenha.geometry("360x640+490+90")
        self.recsenha.resizable(0,0)

        self.backgroundImg = PhotoImage(file="LimaoSiciliano.png")
        self.Imagem = Label(image=self.backgroundImg).pack()

        self.campoNome = Entry(font="Bahnschrift 20 bold", width=8, fg="white", bg="#fff2f2", relief="raised").place(x=11,y=210)

        self.imgBotConf = PhotoImage(file="button_confirmar.png")
        self.botaoConf = Button(self.recsenha, bd=0, image=self.imgBotConf, command=self.Login).place(x=11, y=210)

App()