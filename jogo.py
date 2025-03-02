import random

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = int(vida)
        self.__nivel = int(nivel)
    
    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0 :
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel()*2, self.get_nivel()*4)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel()*5, self.get_nivel()*8)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")


class Heroi (Personagem): 
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"


class Inimmigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo, habilidade):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        self.__habilidade = habilidade
    
    def get_tipo(self):
        return self.__tipo
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    def __init__(self, inimigo_nome, inimigo_tipo, inimigo_habilidade,heroi_nome, heroi_habilidade) -> None:

        vida = random.randint(50,100)
        nivel = random.randint(1,10)
        self.heroi = Heroi(heroi_nome, vida, nivel, heroi_habilidade)

        vida = random.randint(50,100)
        nivel = random.randint(1,10)
        self.inimigo = Inimmigo(inimigo_nome, vida, nivel, inimigo_tipo, inimigo_habilidade)

    def iniciar_batalha(self):
        print("\nIniciando batalha!")
        while (self.heroi.get_vida() > 0 and self.inimigo.get_vida() >0):
            print(f"\nDetalhes dos Personagens: \n\nHeroi: {self.heroi.exibir_detalhes()}\n\nInimigo: {self.inimigo.exibir_detalhes()}")

            escolha = int(input("\n`1 - Ataque Normal\n2 - Ataque Especial\nEscolha: "))

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("[ERROR]: escolha novamente!")

            if self.inimigo.get_vida() > 0:
                if (random.randint(1,20))%2 == 0:
                    self.inimigo.atacar(self.heroi)
                else:
                    self.inimigo.ataque_especial(self.heroi)

        if self.heroi.get_vida() == 0:
            print("\n Voce perdeu!")
        else:
            print("\n Parabens voce venceu a batalha!")

input("Figthing Game\n\nPressione ENTER para iniciar")
print("\nVamos criar nossos personagens: ")
heroi_nome = input("\nQuem sera o heroi da historia?\n")
heroi_habilidade = input("\nQual sera sua habilidade especial?\n")

inimigo_nome = input("\nQuem sera o inimigo da historia?\n")
inimigo_tipo = input("\nQual o tipinho dele?\n")
inimigo_habilidade = input("\nQual sera sua habilidade especial?\n")

jogo = Jogo(inimigo_nome, inimigo_tipo, inimigo_habilidade,heroi_nome, heroi_habilidade)
jogo.iniciar_batalha()
