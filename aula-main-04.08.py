# Urna Eletrônica

''' Cadastro de candidatos: Nome e Número (Aba ep/ digitar) / Contador de votos '''

from tkinter import *
from tkinter import messagebox
from playsound import playsound 

class ConfiguraTela:
    #Atributos do programa
    __urna = []
    __votosBrancos = 0
    __votos1 = 0
    __votos2 = 0
    __entrada = 0 
    __cont1 = 0 
    __cont2 = 0

    def __init__(self): #Método Construtor
        self.root = root
        self.tela()
        self.insere_voto()
        self.widgets()
        root.mainloop()

    def tela(self): #Configurações da tela: Título/Tamanho/Configurações        
        self.root.title('VOTE')
        self.root.geometry('675x675+700+200')
        self.root.configure(bg='white')
        
    def tela_contagem_votos(self): #Método de contagem e 'get' dos votos e do vencedor 
        self.janela2 = Frame(self.root, bg = 'white') # Frame que cobre toda à tela 
        self.janela2.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.titulo2_txt = Label(self.janela2,      #Título de Campeão    
                                text='O campeão(a) foi:',
                                font=('Arial', 30),
                                bg='white',
                                fg='black',)
        self.titulo2_txt.place(relx=0.02, rely=0.05)

        self.nulos_txt = Label(self.janela2,      #Título de Vtos Nulos    
                                text='Votos Nulos:',
                                font=('Arial', 20),
                                bg='white',
                                fg='black',)
        self.nulos_txt.place(relx=0.55, rely=0.8, relwidth=0.40, relheight=0.1)

        self.nulos_txt1 = Label(self.janela2,      #Quantidade de votos nulos     
                                text=self.__votosBrancos,
                                font=('Arial', 20),
                                bg='white',
                                fg='black',)
        self.nulos_txt1.place(relx=0.6, rely=0.88, relwidth=0.40, relheight=0.1)

        self.computa_votos()    #Direciona para o computa votos

    def insere_voto(self):
        self.titulo_txt = Label(self.root,      #Título Principal
                                text='Número o Candidato:',
                                font=('Arial', 35),
                                bg='white',
                                fg='black')
        self.titulo_txt.place(relx=0.02, rely=0.05)

        self.__entrada = Entry(self.root,       #Entrada de votos 
                                 bg='white',
                                 fg='black',
                                 font=('Arial', 30))
        self.__entrada.bind("<Return>", self.verifica_candidato) #Bind é um comando que ativa uma função quando se clica em uma tecla no teclado
        self.__entrada.place(relx=0.02, rely=0.15, relwidth=0.50, relheight=0.12)

    def widgets(self):  #Widgets da tela
        self.janela_principal = Frame(self.root, bg = 'black') #FRame principal (Base para a foto)
        self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        self.btn_confirma = Button(self.root, text='Confirmar',     #Botão de 'Confirma' 
            font=('Arial', 20),
            bg='green',
            activebackground='green',
            fg='white',
            activeforeground='white',
            command=self.confirma_voto)
        self.btn_confirma.place(relx=0.55, rely=0.8, relwidth=0.40, relheight=0.1)

        self.btn_cancela = Button(self.root, text='Cancelar',       #Botão 'Cancela'
            font=('Arial', 20),
            bg='red',
            activebackground='red',
            fg='white',
            activeforeground='white',
            command=self.cancela)
        self.btn_cancela.place(relx=0.55, rely=0.65, relwidth=0.40, relheight=0.1)

        self.btn_nulo = Button(self.root, text='Branco',        #Botão de voto em 'Branco'
            font=('Arial', 20),
            bg='#f2f3f4',
            activebackground='#f2f3f4',
            fg='black',
            activeforeground='black',
            command=self.vota_nulo)
        self.btn_nulo.place(relx=0.55, rely=0.5, relwidth=0.40, relheight=0.1)

    def confirma_voto(self):        #Método de confirmar o voto
        if self.__entrada.get() == '1': # Condição que mostram
            self.__urna.append(self.__entrada.get())        #Atribui a entrada do voto 'self.entrada' para 'self.__urna'
            print(self.__urna)

            self.__cont1 += 1 #Contador de votos para o candidato 1
            self.__entrada.delete(0, END)

            self.janela_principal = Frame(self.root, bg = 'black') 
            self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

            self.titulo5_txt = Label(self.root,      
                                text='                              ',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo5_txt.place(relx=0.52, rely=0.32)

            playsound('C:/Users/RES0130138/OneDrive - Firjan/Documentos/Curso/Python/Barulho_Urna.mp3')

            messagebox.showinfo('Confirma', 'Voto Confirmado com Sucesso')

        if self.__entrada.get() == '2':
            self.__urna.append(self.__entrada.get())        #Atribui a entrada do voto 'self.entrada' para 'self.__urna'
            print(self.__urna)

            self.__cont2 += 1 #Contador de votos para o candidato 2
            self.__entrada.delete(0, END)

            self.janela_principal = Frame(self.root, bg = 'black') 
            self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

            self.titulo5_txt = Label(self.root,      
                                text='                              ',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo5_txt.place(relx=0.52, rely=0.32)

            playsound('C:/Users/RES0130138/OneDrive - Firjan/Documentos/Curso/Python/Barulho_Urna.mp3')

            messagebox.showinfo('Confirma', 'Voto Confirmado com Sucesso')

        else:
            self.__entrada.delete(0, END)
            messagebox.askokcancel('Erro', 'O número digitado não corresponde à algum candidato')

    def cancela(self):
        messagebox.showerror('Cancela', 'Voto Cancelado')

        self.janela_principal = Frame(self.root, bg = 'black') 
        self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        self.titulo5_txt = Label(self.root,      
                                text='                              ',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
        self.titulo5_txt.place(relx=0.52, rely=0.32)

        self.__entrada.delete(0, END)

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

    def vota_nulo(self):
        status = messagebox.askokcancel('Voto Branco', 'Confima seu voto em branco?')

        if status == True:
            self.__votosBrancos += 1
            print(self.__votosBrancos)
            self.janela_principal = Frame(self.root, bg = 'black') 
            self.janela_principal.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

            self.titulo5_txt = Label(self.root,      
                                text='                              ',
                                font=('Arial', 30),
                                bg='white',
                                fg='black')
            self.titulo5_txt.place(relx=0.52, rely=0.32)

            self.__entrada.delete(0, END)

        if status == False:
            print('Voto Cancelado')

    def computa_votos(self):
        if self.__cont1 > self.__cont2:
            self.__votos1 += 1
            self.titulo4_txt = Label(self.janela2,      
                                text='Machado de Assis',
                                font=('Arial', 45, 'bold'),
                                bg='white',
                                fg='black')
            self.titulo4_txt.place(relx=0.02, rely=0.15)

            self.camp1_txt = Label(self.janela2,      
                                text=f'Primeiro mais votado:',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp1_txt.place(relx=0.55, rely=0.3, relwidth=0.40, relheight=0.1)

            self.camp11_txt = Label(self.janela2,      
                                text=f'{self.__cont1}',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp11_txt.place(relx=0.55, rely=0.38, relwidth=0.40, relheight=0.1)

            self.camp22_txt = Label(self.janela2,      
                                text=f'Segundo mais votado:',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp22_txt.place(relx=0.55, rely=0.5, relwidth=0.40, relheight=0.1)

            self.camp22_txt = Label(self.janela2,      
                                text=f'{self.__cont2}',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp22_txt.place(relx=0.55, rely=0.58, relwidth=0.40, relheight=0.1)

            self.img1 = PhotoImage(file='Candidato_Machado.png')
            self.img_cand1 = Label(self.janela2, image=self.img1)
            self.img_cand1.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

        if self.__cont2 > self.__cont1:
            self.__votos2 += 1
            self.titulo5_txt = Label(self.janela2,      
                                text='Clarice Lispector',
                                font=('Arial', 45, 'bold'),
                                bg='white',
                                fg='black')
            self.titulo5_txt.place(relx=0.08, rely=0.15)

            self.camp3_txt = Label(self.janela2,      
                                text=f'Primeiro mais votado:',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp3_txt.place(relx=0.55, rely=0.3, relwidth=0.40, relheight=0.1)

            self.camp33_txt = Label(self.janela2,      
                                text=f'{self.__cont1}',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp33_txt.place(relx=0.55, rely=0.38, relwidth=0.40, relheight=0.1)

            self.camp4_txt = Label(self.janela2,      
                                text=f'Segundo mais votado:',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp4_txt.place(relx=0.55, rely=0.5, relwidth=0.40, relheight=0.1)

            self.camp44_txt = Label(self.janela2,      
                                text=f'{self.__cont2}',
                                font=('Arial', 20),
                                bg='white',
                                fg='black')
            self.camp44_txt.place(relx=0.55, rely=0.58, relwidth=0.40, relheight=0.1)

            self.img2 = PhotoImage(file='Candidata_Clarice.png')
            self.img_cand2 = Label(self.janela2, image=self.img2)
            self.img_cand2.place(relx = 0.02, rely = 0.3, relwidth = 0.5, relheight = 0.68)

##### Programa Principal #####
root = Tk()
ConfiguraTela()
