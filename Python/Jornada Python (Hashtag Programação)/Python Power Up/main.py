import pyautogui
import pandas as pd
from time import sleep
# Passo a passo do projeto
# 1°: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrir o navegador

# press -> aperta tecla
# write -> escreve
# click -> clica em algum lugar na tela
# hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Entrar no link
pyautogui.hotkey('ctrl', 'l')
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 2°: Fazer login

sleep(3)
pyautogui.click(x=1050, y=379)
pyautogui.write('matheuslevit@gmail.com')
pyautogui.press("tab")
pyautogui.write('vel')
pyautogui.press("tab")
pyautogui.press("enter")

# 3°: Importar a base de produtos para cadastrar

produtos = pd.read_csv("produtos.csv")
print(produtos)

# 4°: Cadastrar um produto

# 5°: Repetir o processo de cadastro até o fim

sleep(3)
for linha in produtos.index:
    código = produtos.loc[linha, "codigo"] 
    marca = produtos.loc[linha, "marca"]
    tipo = produtos.loc[linha, "tipo"]
    categoria = produtos.loc[linha, "categoria"]
    preco_unitario = produtos.loc[linha, "preco_unitario"]
    custo = produtos.loc[linha, "custo"]
    obs = produtos.loc[linha, "obs"]

    pyautogui.click(x=987, y=248)
    pyautogui.write(str(código))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    if not pd.isna(obs):
        pyautogui.write(str(obs))
        pyautogui.press("tab")
        
    pyautogui.press("enter")
    pyautogui.scroll(5000)