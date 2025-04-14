import pyautogui
import time

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto

pyautogui.PAUSE = 0.8

# Passo 1: Entrar no sistema da empresa
# abrir chrome
# atalho: pyautogui.hotkey("contrl", "c")
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

# digitar o site
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer Login
pyautogui.click(x=677, y=375)
pyautogui.write("emailtest@gmail.com")
# preencher a senha
pyautogui.press("tab")
pyautogui.write("senha1")

# botao logar
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas

table = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar os produtos
for line in table.index:
    pyautogui.click(x=749, y=268)

    code = table.loc[line, "codigo"]
    pyautogui.write(code)
    pyautogui.press("tab")

    mark = table.loc[line, "marca"]
    pyautogui.write(mark)
    pyautogui.press("tab")

    type = table.loc[line, "tipo"]
    pyautogui.write(type)
    pyautogui.press("tab")

    category = str(table.loc[line, "categoria"])
    pyautogui.write(category)
    pyautogui.press("tab")

    unit_price = str(table.loc[line, "preco_unitario"])
    pyautogui.write(unit_price)
    pyautogui.press("tab")

    cost =  str(table.loc[line, "custo"])
    pyautogui.write(cost)
    pyautogui.press("tab")

    obs = str(table.loc[line, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1500)

# Passo: 5 Repetir para todos os produtos

# pyautogui -> fazer automações com python

# nan -> Not A Number