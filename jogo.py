class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = int(vida)
        self.__nivel = nivel
    
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
        dano = int(self.__nivel)*2
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi (Personagem): 
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"


class Inimmigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Superman", vida="100", nivel="20", habilidade="Super Forca")
        self.inimigo = Inimmigo(nome="Lex Luthor", vida="150", nivel="6", tipo="Playboy")

    def iniciar_batalha(self):
        print("Iniciando batalha!")
        while (self.heroi.get_vida() > 0 and self.inimigo.get_vida() >0):
            print(f"\nDetalhes dos Personagens: \n\nHeroi: {self.heroi.exibir_detalhes()}\n\nInimigo: {self.inimigo.exibir_detalhes()}")

            input("\nPressione ENTER para atacar: ")
            escolha = int(input("1 - Ataque Normal\n2 - Ataque Especial\nEscolha: "))

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            else:
                print("[ERROR]: escolha novamente!")

        if self.heroi.get_vida() == 0:
            print("\n Voce perdeu!")
        else:
            print("\n Parabens voce venceu a batalha!")

jogo = Jogo()
jogo.iniciar_batalha()