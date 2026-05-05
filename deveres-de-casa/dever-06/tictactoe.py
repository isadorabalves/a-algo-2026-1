"""
Tic Tac Toe

Implementação das funções de jogo e do algoritmo Minimax para o Jogo da
Velha. O tabuleiro é representado por uma lista de três listas, onde cada
célula contém X, O ou EMPTY (None).
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """Retorna o estado inicial do tabuleiro (todas as células vazias)."""
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """Retorna o jogador que fará o próximo movimento (X ou O).

    X sempre joga primeiro e os jogadores se alternam. Logo, se a
    quantidade de X no tabuleiro for igual à de O, é a vez de X;
    caso contrário, é a vez de O. Para um tabuleiro terminal qualquer
    valor de retorno é aceitável.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """Retorna o conjunto de todas as ações (i, j) possíveis no tabuleiro.

    Cada ação é uma tupla (linha, coluna) correspondente a uma célula
    vazia. Para um tabuleiro terminal qualquer valor de retorno é
    aceitável.
    """
    return {(i, j)
            for i in range(3)
            for j in range(3)
            if board[i][j] is EMPTY}


def result(board, action):
    """Retorna um novo tabuleiro após aplicar `action` em `board`.

    O tabuleiro original não é modificado (deepcopy). Levanta
    ValueError se a ação estiver fora dos limites ou se a célula
    indicada já estiver ocupada.
    """
    i, j = action
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError(f"Ação {action} fora dos limites do tabuleiro.")
    if board[i][j] is not EMPTY:
        raise ValueError(f"Célula {action} já está ocupada.")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """Retorna o vencedor do tabuleiro (X ou O) ou None, se não houver.

    Verifica as três linhas, três colunas e duas diagonais. Pressupõe
    que existe no máximo um vencedor.
    """
    lines = []
    # Linhas.
    lines.extend(board)
    # Colunas.
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])
    # Diagonais.
    lines.append([board[k][k] for k in range(3)])
    lines.append([board[k][2 - k] for k in range(3)])

    for line in lines:
        if line[0] is not EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None


def terminal(board):
    """Retorna True se o jogo terminou; False caso contrário.

    O jogo termina quando há um vencedor ou quando todas as células
    estão preenchidas (empate).
    """
    if winner(board) is not None:
        return True
    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """Retorna 1 se X venceu, -1 se O venceu, 0 em caso de empate.

    Pressupõe que `board` é um tabuleiro terminal.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0


def minimax(board):
    """Retorna a ação ótima (i, j) para o jogador atual no tabuleiro.

    Retorna None caso o tabuleiro seja terminal. X maximiza a
    utilidade enquanto O a minimiza. A busca é interrompida assim
    que se encontra uma ação que garante a melhor utilidade possível
    (1 para X, -1 para O), o que é correto e acelera o jogador.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = _min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
                if best_value == 1:
                    return best_action
        return best_action

    # current == O
    best_value = math.inf
    best_action = None
    for action in actions(board):
        value = _max_value(result(board, action))
        if value < best_value:
            best_value = value
            best_action = action
            if best_value == -1:
                return best_action
    return best_action


def _max_value(board):
    """Auxiliar do Minimax: utilidade máxima alcançável a partir de `board`."""
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, _min_value(result(board, action)))
        if v == 1:
            return v
    return v


def _min_value(board):
    """Auxiliar do Minimax: utilidade mínima alcançável a partir de `board`."""
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, _max_value(result(board, action)))
        if v == -1:
            return v
    return v
