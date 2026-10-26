import tkinter as tk
from tkinter import messagebox
import urllib.parse
import webbrowser
import re


def gerar_mensagem():
    nome = campo_nome.get().strip()
    tipo = tipo_abordagem.get()

    saudacao = f"Olá, {nome}!" if nome else "Olá!"

    mensagens = {
        "RH e Recrutamento": (
            f"{saudacao} Tudo bem? "
            "Trabalho com RH e recrutamento e seleção. "
            "Gostaria de me apresentar e conhecer possíveis "
            "demandas de recrutamento da sua empresa. "
            "Podemos conversar? Obrigada!"
        ),
        "Recolocação CLT": (
            f"{saudacao} Tudo bem? "
            "Estou buscando uma oportunidade de recolocação CLT "
            "e gostaria de apresentar meu perfil profissional. "
            "Tenho interesse em contribuir com a equipe e "
            "desenvolver meus talentos. Fico à disposição "
            "para conversarmos. Obrigada!"
        ),
        "Comercial": (
            f"{saudacao} Tudo bem? "
            "Entro em contato para apresentar meus serviços "
            "profissionais e entender se existe alguma demanda "
            "em que eu possa contribuir. Podemos conversar?"
        ),
        "Networking": (
            f"{saudacao} Tudo bem? "
            "Gostaria de ampliar meu networking profissional "
            "e trocar experiências sobre oportunidades e "
            "projetos. Será um prazer conversar com você!"
        )
    }

    texto = mensagens[tipo]

    campo_mensagem.delete("1.0", tk.END)
    campo_mensagem.insert(tk.END, texto)


def abrir_whatsapp():
    telefone = campo_telefone.get().strip()
    mensagem = campo_mensagem.get("1.0", tk.END).strip()

    # Remove espaços, parênteses, traços e sinal de +
    numero = re.sub(r"\D", "", telefone)

    if len(numero) < 10 or len(numero) > 15:
        messagebox.showerror(
            "Número inválido",
            "Informe o telefone com código do país e DDD.\n"
            "Exemplo: 5551999999999"
        )
        return

    if not mensagem:
        messagebox.showwarning(
            "Mensagem vazia",
            "Clique em Gerar mensagem primeiro."
        )
        return

    url = (
        "https://wa.me/"
        + numero
        + "?text="
        + urllib.parse.quote(mensagem)
    )

    webbrowser.open(url)


# Criar janela
janela = tk.Tk()
janela.title("Gerador de Abordagem WhatsApp")
janela.geometry("560x590")
janela.configure(bg="#171717")

titulo = tk.Label(
    janela,
    text="GERADOR WHATSAPP",
    font=("Arial", 20, "bold"),
    fg="#25D366",
    bg="#171717"
)
titulo.pack(pady=18)


# Nome do contato
tk.Label(
    janela,
    text="Nome do contato:",
    fg="white",
    bg="#171717"
).pack()

campo_nome = tk.Entry(janela, width=45, font=("Arial", 11))
campo_nome.pack(pady=6)


# Número
tk.Label(
    janela,
    text="Telefone com código do país e DDD:",
    fg="white",
    bg="#171717"
).pack(pady=(8, 0))

campo_telefone = tk.Entry(
    janela,
    width=45,
    font=("Arial", 11)
)
campo_telefone.pack(pady=6)
campo_telefone.insert(0, "55")


# Tipo de abordagem
tk.Label(
    janela,
    text="Escolha o tipo de abordagem:",
    fg="white",
    bg="#171717"
).pack(pady=(8, 0))

tipo_abordagem = tk.StringVar(value="RH e Recrutamento")

opcoes = [
    "RH e Recrutamento",
    "Recolocação CLT",
    "Comercial",
    "Networking"
]

menu = tk.OptionMenu(janela, tipo_abordagem, *opcoes)
menu.config(width=30)
menu.pack(pady=6)


# Gerar mensagem
botao_gerar = tk.Button(
    janela,
    text="GERAR MENSAGEM",
    command=gerar_mensagem,
    bg="#25D366",
    fg="black",
    font=("Arial", 11, "bold")
)
botao_gerar.pack(pady=12)


# Campo de mensagem editável
tk.Label(
    janela,
    text="Mensagem de abordagem:",
    fg="white",
    bg="#171717"
).pack()

campo_mensagem = tk.Text(
    janela,
    width=58,
    height=8,
    font=("Arial", 10),
    wrap="word"
)
campo_mensagem.pack(padx=12, pady=8)


# Abrir WhatsApp
botao_enviar = tk.Button(
    janela,
    text="ABRIR WHATSAPP",
    command=abrir_whatsapp,
    bg="#128C7E",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=12,
    pady=8
)
botao_enviar.pack(pady=12)

tk.Label(
    janela,
    text="Confira a mensagem e envie manualmente.",
    fg="#BBBBBB",
    bg="#171717"
).pack()

janela.mainloop()
