import controle
import ttkbootstrap as bootstrap
import requests
import route_controler

def initiation(root):
    root.geometry("350x450")
    root.eval('tk::PlaceWindow . center')

    def validar_numeros(char):
        return char.isdigit()

    def jmount(user: int, passw: str):
        return {
            "body": {
                "user": user,
                "pass": passw
            },
            "url": 'http://10.10.0.56:5001/validauser'
        }

    def loging():
        try:
            x = int(useridentry.get())
            if type(x) is int:
                req = jmount(x, passentry.get())
                json = requests.post(f"{req['url']}", json=req['body']).json()
                if json['valida'] == 'false':
                    ret = controle.exec_log(useridentry.get(), passentry.get())
                    if ret['bool'] is False:
                        txt.config(text='Usuario/Senha incorretos')
                        useridentry.config(bootstyle='danger')
                        passentry.config(bootstyle='danger')
                    else:
                        username = ret['obj']['nome']
                        grid.destroy()
                        route_controler.admin(root, username)
                else:
                    username = json['nmUser']
                    grid.destroy()
                    route_controler.route(root, username)
            else:
                txt.config(text='Digite apenas numeros no campo usuario')
                useridentry.config(bootstyle='danger')
                passentry.config(bootstyle='danger')
        except:
            txt.config(text='Digite apenas numeros no campo usuario')
            useridentry.config(bootstyle='danger')
            passentry.config(bootstyle='danger')

    validar_numeros_cmd = root.register(validar_numeros)
    grid = bootstrap.Frame(root)
    txt = bootstrap.Label(grid, text='')
    logtxt = bootstrap.Label(grid, text='Realizar Login Linx')
    labellog = bootstrap.Label(grid)
    labellog2 = bootstrap.Label(grid)
    useridtxt = bootstrap.Label(labellog, text='Login')
    useridentry = bootstrap.Entry(labellog, validate="key", validatecommand=(validar_numeros_cmd, '%S'))
    passtxt = bootstrap.Label(labellog2, text='Senha')
    passentry = bootstrap.Entry(labellog2, show="*")
    butonlog = bootstrap.Button(grid, text='Login', command=loging)

    logtxt.pack(pady=30, side='top')
    useridtxt.pack(side='left')
    useridentry.pack()
    passtxt.pack(side='left')
    passentry.pack()
    labellog.pack(side='top')
    labellog2.pack(pady=10)
    txt.pack(pady=20)
    butonlog.pack(side='top')
    grid.pack()