import sqlite3
from random import randrange


class AtivarServicoDois:

    def __init__(self):
        self.cursor = False
        self.conn = False
        self.contador = 1000

    def conect(self):
        conn = sqlite3.connect("db.sqlite3")
        cur = conn.cursor()

        self.conn = conn
        self.cursor = cur
        print('conexão: ok')

    def run(self):
        self.conect()

        cont = 0
        while True:
            cont += 1

            # pares entre 0 e 9
            numero = randrange(0, 1000)

            if numero % 2 == 0:
                numero += 1
                print(numero)

                if numero >= 1000:
                    numero = 999

            sql = "insert into servico_servicodois (numero_impar) values (%s)" % numero
            self.cursor.execute(sql)

            self.conn.commit()

            if cont == self.contador:
                break

        self.conn.close()
        print(self.contador)

        return


if __name__ == "__main__":
    ASU = AtivarServicoDois()
    ASU.run()
