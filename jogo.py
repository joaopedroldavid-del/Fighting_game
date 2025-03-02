import random

class Personagem:
    def __init__(self, nome: str, vida: int, nivel: int, habilidade: str) -> None:
        self.__nome = nome
        self.__vida = max(vida, 0)  
        self.__nivel = max(nivel, 1)
        self.__habilidade = habilidade

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @property
    def nivel(self):
        return self.__nivel

    @property
    def habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return (
            f"Nome: {self.nome}\n"
            f"Vida: {self.vida}\n"
            f"Nível: {self.nivel}\n"
            f"Habilidade Especial: {self.habilidade}"
        )

    def receber_ataque(self, dano: int):
        self.__vida = max(self.__vida - dano, 0)

    def atacar(self, alvo):
        dano = random.randint(self.nivel * 2, self.nivel * 4)
        alvo.receber_ataque(dano)
        print(f"\n{self.nome} atacou {alvo.nome} e causou {dano} de dano!")

    def ataque_especial(self, alvo):
        dano = random.randint(self.nivel * 5, self.nivel * 8)
        alvo.receber_ataque(dano)
        print(f"\n{self.nome} usou {self.habilidade} em {alvo.nome} e causou {dano} de dano!")


class Heroi(Personagem):
    pass


class Inimigo(Personagem):
    pass


class Jogo:
    def __init__(self, heroi_nome: str, heroi_habilidade: str, inimigo_nome: str, inimigo_habilidade: str) -> None:
        self.heroi = self._criar_personagem(Heroi, heroi_nome, heroi_habilidade)
        self.inimigo = self._criar_personagem(Inimigo, inimigo_nome, inimigo_habilidade)

    @staticmethod
    def _criar_personagem(cls, nome: str, habilidade: str):
        vida = random.randint(50, 100)
        nivel = random.randint(1, 10)
        return cls(nome, vida, nivel, habilidade)

    def iniciar_batalha(self):
        print("\nIniciando a batalha!\n")

        while self.heroi.vida > 0 and self.inimigo.vida > 0:
            print("\n--- Estado Atual ---")
            print(f"Herói:\n{self.heroi.exibir_detalhes()}\n")
            print(f"Inimigo:\n{self.inimigo.exibir_detalhes()}\n")

            escolha = self._obter_escolha_jogador()
            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)

            if self.inimigo.vida > 0:
                if random.choice([True, False]):
                    self.inimigo.atacar(self.heroi)
                else:
                    self.inimigo.ataque_especial(self.heroi)

        self._exibir_resultado()

    def _obter_escolha_jogador(self):
        while True:
            try:
                escolha = int(input("\n1 - Ataque Normal\n2 - Ataque Especial\nEscolha: "))
                if escolha in [1, 2]:
                    return escolha
                else:
                    print("Opção inválida! Escolha 1 ou 2.")
            except ValueError:
                print("Entrada inválida! Digite um número válido.")

    def _exibir_resultado(self):
        if self.heroi.vida == 0:
            print("\nVocê perdeu!")
        else:
            print("\nParabéns! Você venceu a batalha!")


# Inicialização do jogo
print("Fighting Game\n\nPressione ENTER para iniciar")
input()

print("\nVamos criar nossos personagens!")
heroi_nome = input("\nQuem será o herói da história? ")
heroi_habilidade = input("Qual será sua habilidade especial? ")

inimigo_nome = input("\nQuem será o inimigo da história? ")
inimigo_habilidade = input("Qual será sua habilidade especial? ")

jogo = Jogo(heroi_nome, heroi_habilidade, inimigo_nome, inimigo_habilidade)
jogo.iniciar_batalha()
