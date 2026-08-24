import os
import smtplib
from email.mime.text import MIMEText

gmail_user = os.environ["GMAIL_USER"]
gmail_password = os.environ["GMAIL_PASSWORD"]

destinatario = "ana.storion@ache.com.br"

with open("resultado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

mensagem["Subject"] = "Teste CADIFA"
mensagem["From"] = gmail_user
mensagem["To"] = destinatario

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(gmail_user, gmail_password)
    servidor.send_message(mensagem)

print("E-mail enviado com sucesso.")
