import os
import smtplib
from email.mime.text import MIMEText

gmail_user = os.environ["GMAIL_USER"]
gmail_password = os.environ["GMAIL_PASSWORD"]

destinatarios = [
    "ana.storion@ache.com.br",
    "lais.horta@ache.com.br"
]

with open("resultado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

mensagem = MIMEText(conteudo)

mensagem["Subject"] = "MONITOR CADIFA"
mensagem["From"] = gmail_user
mensagem["To"] = ", ".join(destinatarios)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(gmail_user, gmail_password)
    servidor.sendmail(
        gmail_user,
        destinatarios,
        mensagem.as_string()
    )
    

print("E-mail enviado com sucesso.")
