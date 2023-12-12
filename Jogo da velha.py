class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print("|".join(linha))
            print("-" * 5)

    def realizar_jogada(self, jogador, linha, coluna):
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = jogador.simbolo
            return True
        else:
            print("Posição ocupada. Escolha outra.")
            return False

    def verificar_vitoria(self):
        # Verifica linhas e colunas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                return True

        # Verifica diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True

        return False

def main():
    jogador1 = Jogador("Jogador 1", "X")
    jogador2 = Jogador("Jogador 2", "O")

    tabuleiro = Tabuleiro()

    turno = 0
    jogador_atual = jogador1

    while True:
        print(f"\nTurno de {jogador_atual.nome}")
        tabuleiro.imprimir_tabuleiro()

        linha = int(input("Digite a linha (0, 1, ou 2): "))
        coluna = int(input("Digite a coluna (0, 1, ou 2): "))

        if tabuleiro.realizar_jogada(jogador_atual, linha, coluna):
            if tabuleiro.verificar_vitoria():
                print(f"\n{jogador_atual.nome} venceu!")
                break

            turno += 1
            if turno == 9:
                print("\nEmpate!")
                break

            jogador_atual = jogador1 if turno % 2 == 0 else jogador2

if __name__ == "__main__":
    main()