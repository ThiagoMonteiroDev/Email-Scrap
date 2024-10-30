import win32com.client as win32
import requests as re


response = re.get('https://foradoplastico.com.br')
html = response.text


print(html)


outlook = win32.Dispatch("outlook.application")
email = outlook.CreateItem(0)


email.to = "thiago.tenorio@edu.pe.senac.br"
email.Subject = "Dados do Scraping"
email.HTMLBody = f"""
<p>Eu quero passar</p>
<p>Eu quero estágio</p>
<p>Eu quero dinheiro</p>
<p>Aqui está o HTML do site:</p>
<div>{html}</div>
"""


email.Send()
print("Email Enviado")
