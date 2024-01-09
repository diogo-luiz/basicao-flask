import tkinter as tk

def mostrar_mensagem():
    label_resultado.config(text="Olá, Tkinter!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter")
janela.geometry("1200x700")  # Definir resolução da janela

# Criar e adicionar um rótulo
label = tk.Label(janela, text="Bem-vindo ao Tkinter!", font=("Arial", 18))
label.pack(pady=20)

# Criar e adicionar um botão
botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem, font=("Arial", 14))
botao.pack(pady=20)

# Criar um rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 16))
label_resultado.pack(pady=20)

# Iniciar o loop principal da janela
janela.mainloop()
