import mysql.connector
import random
prenome = ["José","Miguel","Rafael","Cristiano","Davi","Guilherme","Paulo","Ederson","Carlos","Mario"]
nome = ["Arthur","Noah","Michalagenlo","Kekule","Eren","Lahm","Zidane","Kamiina","Ronaldinho","Kroos","Tony"]
sobrenomes = ["Costa","Barolo","Dacosta","Silva","Yeager","Joestar","Salvatore","Maldini","Mussolini","Coldreanu","Mosley"]
contador = 1
ageidade = ["1","5","10","20","40","80","100","120"]
vezes = int(input("digite o numero de commits: "))

banco = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="",
    database="testesql"
)
print(banco)

cursor = banco.cursor()
while (contador<=vezes):
    escolhido = random.choice(prenome) + " " + random.choice(nome) + " " + random.choice(sobrenomes)
    print(escolhido)
    age = random.choice(ageidade)
    print(age)
    telefone = random.randint(1000000, 9000000)
    print(telefone)
    comandosql = "INSERT INTO pessoas(nome,idade,sexo) VALUES(%s,%s,%s)"
    dados = (escolhido,age, "m")
    contador = contador + 1
    cursor.execute(comandosql,dados)
    banco.commit()
