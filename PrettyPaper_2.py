from tkinter import *

class App:
    def __init__(self):
        self.root = Tk() 
        self.root.title("PrettyPaper")
        self.root.geometry("360x640+490+90")
        self.root.resizable(0,0)
        self.tela_conta()
        self.root.mainloop()   

    def tela_conta(self):
        #Tela Conta
        self.usuario = Frame(self.root, width='360', height="640", bg='#bbb')
        self.usuario.place(x='0', y='0') # Cria uma tela secundária dentro da tela principal

        self.backgroundImg = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Background\Bg_conta.png")
        self.imgBotExc = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Botoes\Bt_exclr.png")
        
        self.Imagem = Label(self.usuario, image=self.backgroundImg)
        self.Imagem.pack()

        self.botaoExc = Button(self.usuario, bd=0, image=self.imgBotExc, bg="#fff2f2", command=lambda: self.tela_excluir())
        self.botaoExc.place(x=120, y=520)
        
    def tela_excluir(self):
        #Tela Excluir
        self.usuario.place_forget() # Destroy a tela secundária 
        self.deletar = Frame(self.root, width='360', height="640", bg='#fffff2') # Cria outra tela secundária dentro da tela principal
        self.deletar.place(x=0,y=0)

        self.backgroundImg = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Background\Bg_excluir_conta.png")
        self.imgBotSim = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Botoes\Bt_exclr_sim.png")
        self.imgBotNao = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Botoes\Bt_exclr_nao.png")

        self.Imagem = Label(self.deletar, image=self.backgroundImg)
        self.Imagem.pack()

        self.botaoSim = Button(self.deletar, bd=0, image=self.imgBotSim, bg="#fff2f2")
        self.botaoSim.place(x=70, y=340)
        self.botaoNao = Button(self.deletar, bd=0, image=self.imgBotNao, bg="#fff2f2", command=lambda: self.usuario)
        self.botaoNao.place(x=185, y=340)
    

App()
#    def Carrinho(self):
#        self.conta.stroy()

#        self.carrinho = Tk()
#        self.carrinho.title("PrettyPaper - Carrinho")
 #       self.carrinho.geometry("360x640+490+90")
 #       self.carrinho.resizable(0,0)

#self.backgroundImg = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Background\Bg_carrinho.png")
 #       self.Imagem = Label(image=self.backgroundImg).pack()

 #       self.conta.after(3000, self.Favoritos)
 #       self.conta.mainloop()

#def Favoritos(self):
  #      self.carrinho.destroy()

  #      self.favoritos = Tk()
  #      self.favoritos.title("PrettyPaper - Favoritos")
  #      self.favoritos.geometry("360x640+490+90")
  #      self.favoritos.resizable(0,0)

  #      self.backgroundImg = PhotoImage(file="D:\Lauren\PrettyPaper-main\Imagens\Background\Bg_favoritos.png")
   #     self.Imagem = Label(image=self.backgroundImg).pack()

   #     self.conta.after(3000)
   #     self.conta.mainloop()

        
