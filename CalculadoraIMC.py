from tkinter import *

class IMCalc:
    def __init__(self, win):

        self.lbl1 = Label(win, text='Digite sua altura (cm):', font=('Arial', 12), anchor="c")
        self.lbl2 = Label(win, text='Digite seu peso (kg):', font=('Arial', 12), anchor="c")
        self.lbl3 = Label(win, text='Seu IMC:', font=('Arial', 12), anchor="e")
        self.lbl4 = Label(win, text='Classificação:', font=('Arial', 12), anchor="w")
        self.lbl6 = Label(win, text='Peso Ideal:', font=('Arial', 12), anchor="e")
        self.lbl7 = Label(win, text='Recomendação:', font=('Arial', 12), anchor="e")

        self.lbl1.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.lbl2.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.lbl3.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.lbl4.grid(row=4, column=0, padx=20, pady=10, sticky="e")
        self.lbl6.grid(row=5, column=0, padx=20, pady=10, sticky="e")
        self.lbl7.grid(row=6, column=0, padx=20, pady=10, sticky="e")

        self.texto1 = Entry(win, bd=3, font=('Arial', 12), width=10)
        self.texto1.grid(row=1, column=1, padx=20, pady=10, sticky="n")
        self.texto2 = Entry(win, font=('Arial', 12), width=10)
        self.texto2.grid(row=2, column=1, padx=20, pady=10, sticky="n")
        self.texto3 = Label(win, font=('Arial', 12), width=10, anchor="n")
        self.texto3.grid(row=3, column=1, padx=20, pady=10, sticky="n")
        self.texto4 = Label(win, font=('Arial', 12), width=25, anchor="n")
        self.texto4.grid(row=4, column=1, padx=20, pady=10, sticky="n")
        self.texto6 = Label(win, font=('Arial', 12), width=40, anchor="n")
        self.texto6.grid(row=5, column=1, padx=20, pady=10, sticky="n")
        self.texto7 = Label(win, font=('Arial', 12), width=40, anchor="n")
        self.texto7.grid(row=6, column=1, padx=20, pady=10, sticky="n")

        self.lbl5 = Label(win, text='AVISO: O IMC é uma medida simplificada e não leva em conta outros fatores como a composição corporal.', font=('Arial', 10), fg='red', wraplength=450, justify="center")
        self.lbl5.grid(row=8, column=0, columnspan=2, padx=20, pady=10, sticky="n")

        self.botao1 = Button(win, text='Calcular IMC', command=self.pronto, font=('Arial', 12))
        self.botao1.grid(row=7, column=1, columnspan=2, pady=20, padx=20, sticky="n")
        self.centralizar_elementos(win)

    def centralizar_elementos(self, win):
        # Centralizar os elementos na janela
        for widget in win.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def pronto(self):
        altura = int(self.texto1.get())
        peso = int(self.texto2.get())

        # Precisamos converter a altura em centímetros para metros na conta
        resultado = peso / ((altura / 100) ** 2)

        self.texto3.config(text='%.2f' % resultado)

        if resultado <= 17:
            classificacao = "Muito abaixo do peso"
            cor = 'red'
        elif resultado < 18.5:
            classificacao = "Abaixo do peso"
            cor = 'orange'
        elif resultado < 25:
            classificacao = "Peso normal"
            cor = 'green'
        elif resultado < 30:
            classificacao = "Acima do peso"
            cor = 'orange'
        elif resultado < 35:
            classificacao = "Obesidade grau I"
            cor = 'red'
        elif resultado < 40:
            classificacao = "Obesidade grau II (severa)"
            cor = 'red'
        else:
            classificacao = "Obesidade III (mórbida)"
            cor = 'red'

        self.texto4.config(text=classificacao, fg=cor)
        self.texto3.config(fg=cor) 

        peso_minimo = 18.5 * ((altura / 100) ** 2)
        peso_maximo = 24.9 * ((altura / 100) ** 2)

        self.texto6.config(text='Peso Ideal: %.2f - %.2f kg' % (peso_minimo, peso_maximo))

        if resultado < 18.5:
            recomendacao = "ganhar aproximadamente %.2f kg" % (peso_minimo - peso)
            
        elif resultado > 24.9:
            recomendacao = "perder aproximadamente %.2f kg" % (peso - peso_maximo)
            
        else:
            recomendacao = "manter seu peso"
            

        self.texto7.config(text='O ideal é ' + recomendacao, fg=cor)


# Cria a janela principal
janela = Tk()
janela.title("Calculadora de IMC")

largura_janela = 550
altura_janela = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Cria a instância da classe IMCalc
IMCalc(janela)

# Inicia o loop de eventos da janela
janela.mainloop()
