# Urna Eletrônica

''' Cadastro de candidatos: Nome e Número (Aba ep/ digitar) / Contador de votos '''

from tkinter import *

class ConfiguraTela:
    __urna = []
    __entrada = 0 
    __cont1 = 0 
    __cont2 = 0

    def __init__(self):
        self.root = root
        self.tela()
        self.insere_voto()
        self.widgets()
        root.mainloop()

    def tela(self):
        self.root.title('VOTE')
        self.root.geometry('675x675+700+200')
        self.root.configure(bg='white')

    def tela_contagem_votos(self): #Método de contagem e 'get' dos votos e do vencedor 
        self.janela2 = Frame(self.root, bg = 'white') # Frame que cobra toda à tela 
        self.janela2.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.computa_votos()

    def insere_voto(self):
        self.titulo_txt = Label(self.root,      #Título Principal
                                text='Número o Candidato:',
                                font=('Arial', 35),
                                bg='white',
                                fg='black')
        self.titulo_txt.place(relx=0.02, rely=0.05)

        self.__entrada = Entry(self.root,       #ENtrada de votos 
                                 bg='white',
                                 fg='black',
                                 font=('Arial', 30))
        self.__entrada.bind("<Return>", self.verifica_candidato) #Bind 
        self.__entrada.place(relx=0.02, rely=0.15, relwidth=0.50, relheight=0.12)

    def widgets(self):
        self.janela_principal = Frame(self.root, bg = 'black') 
        self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        self.btn_confirma = Button(self.root, text='Confirmar',
            font=('Arial', 20),
            bg='green',
            activebackground='green',
            fg='white',
            activeforeground='white',
            command=self.confirma_voto)
        self.btn_confirma.place(relx=0.55, rely=0.8, relwidth=0.40, relheight=0.1)

        self.btn_cancela = Button(self.root, text='Cancelar',
            font=('Arial', 20),
            bg='red',
            activebackground='red',
            fg='white',
            activeforeground='white')
        self.btn_cancela.place(relx=0.55, rely=0.65, relwidth=0.40, relheight=0.1)

    def confirma_voto(self):
        self.__urna.append(self.__entrada.get())
        print(self.__urna)

        self.song = self.song_box.get(ACTIVE)
        self.song = f'C:/Users/Gabriel/Downloads/MP3/{self.song}.mp3'

        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)
         
        if self.__entrada.get() == '1': # Condição que mostram 
            self.__cont1 += 1 #Contador de votos para o candidato 1
            self.__entrada.delete(0, END)

            self.janela_principal = Frame(self.root, bg = 'black') 
            self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        if self.__entrada.get() == '2':
            self.__cont2 += 1 #Contador de votos para o candidato 2
            self.__entrada.delete(0, END)

            self.janela_principal = Frame(self.root, bg = 'black') 
            self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        
    def verifica_candidato(self, *args):
        if self.__entrada.get() == '1': # Condição que mostram 
            self.img1 = PhotoImage(file='Candidato_Machado.png')
            self.img_cand1 = Label(self.root, image=self.img1)
            self.img_cand1.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

            self.titulo2_txt = Label(self.root,      
                                text='Machado de Assis',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo2_txt.place(relx=0.52, rely=0.32)

        if self.__entrada.get() == '2':
            self.img2 = PhotoImage(file='Candidata_Clarice.png')
            self.img_cand2 = Label(self.root, image=self.img2)
            self.img_cand2.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

            self.titulo2_txt = Label(self.root,      
                                text=' Clarice Lispector  ',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo2_txt.place(relx=0.52, rely=0.32)

        if self.__entrada.get() == '99': # Condição pra ativar a aba de contagem de votos 
            self.tela_contagem_votos()

    def computa_votos(self):
        if self.__cont1 > self.__cont2:
            self.titulo2_txt = Label(self.janela2,      
                                text='O campeão(a) foi:',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo2_txt.place(relx=0.02, rely=0.05)

            self.titulo4_txt = Label(self.janela2,      
                                text='Machado de Assis',
                                font=('Arial', 45, 'bold'),
                                bg='white',
                                fg='black')
            self.titulo4_txt.place(relx=0.02, rely=0.15)

            self.img1 = PhotoImage(file='Candidato_Machado.png')
            self.img_cand1 = Label(self.root, image=self.img1)
            self.img_cand1.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        if self.__cont2 > self.__cont1:
            self.titulo2_txt = Label(self.janela2,      
                                text='O campeão(a) foi:',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo2_txt.place(relx=0.02, rely=0.05)

            self.titulo5_txt = Label(self.janela2,      
                                text='Clarice Lispector',
                                font=('Arial', 45, 'bold'),
                                bg='white',
                                fg='black')
            self.titulo5_txt.place(relx=0.08, rely=0.15)

            self.img2 = PhotoImage(file='Candidata_Clarice.png')
            self.img_cand2 = Label(self.root, image=self.img2)
            self.img_cand2.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

##### Programa Principal #####
root = Tk()
ConfiguraTela()
