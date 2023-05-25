import sys

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

from skfuzzy.control import (
    Antecedent,
    Consequent,
    ControlSystem,
    ControlSystemSimulation,
    Rule,
)


def main(*inputs, exibir=True):
    # Preparando sistema fuzzy
    universos = obter_universos()
    variaveis_fuzzy = criar_variaveis(*universos)
    criar_funcoes_pertinencia(*variaveis_fuzzy, exibir=exibir)
    regras_logicas = obter_regras(*variaveis_fuzzy)
    sistema_de_controle = criar_sistema_de_controle(regras_logicas)

    # Simulando o resultado a partir das entradas
    controle_simulacao = ControlSystemSimulation(sistema_de_controle)
    simular_estado(controle_simulacao, *inputs)
    exibir_resultado(controle_simulacao, variaveis_fuzzy)


def obter_universos():
    # Universos de valores usados nos inputs e outputs
    universo_preco = np.arange(40_000, 100_000, 1)
    universo_rendimento = np.arange(11, 18, 0.001)
    universo_beneficio = np.arange(0, 10.001, 0.001)
    return universo_preco, universo_rendimento, universo_beneficio


def criar_variaveis(universo_preco, universo_rendimento, universo_beneficio):
    # Variáveis fuzzy
    preco = Antecedent(universo_preco, "preço")
    rendimento = Antecedent(universo_rendimento, "rendimento")
    beneficio = Consequent(universo_beneficio, "benefício")
    return preco, rendimento, beneficio


def criar_funcoes_pertinencia(preco, rendimento, beneficio, *, exibir=False):
    # Funções de pertinência automaticas
    preco.automf(number=3, names=["baixo", "médio", "alto"])
    rendimento.automf(number=3, names=["baixo", "médio", "alto"])
    beneficio["baixo"] = fuzz.trapmf(beneficio.universe, [0, 0, 2.5, 5])
    beneficio["médio"] = fuzz.trimf(beneficio.universe, [2.5, 5, 7.5])
    beneficio["alto"] = fuzz.trapmf(beneficio.universe, [5, 7.5, 10, 10])
    # Visualizar as funções de pertinência
    if exibir:
        preco.view()
        rendimento.view()
        beneficio.view()
        plt.show()


def obter_regras(preco, rendimento, beneficio):
    # Abreviações
    P = preco
    R = rendimento
    B = beneficio
    # Criando sistema de controle das regras fuzzy
    logicas = [
        (P["baixo"] | R["alto"], B["alto"]),
        (P["baixo"] | R["médio"], B["médio"]),
        (P["baixo"] | R["baixo"], B["médio"]),
        (P["médio"] | R["alto"], B["médio"]),
        (P["médio"] | R["médio"], B["médio"]),
        (P["médio"] | R["baixo"], B["médio"]),
        (P["alto"] | R["alto"], B["médio"]),
        (P["alto"] | R["médio"], B["médio"]),
        (P["alto"] | R["baixo"], B["baixo"]),
    ]
    return logicas


def criar_sistema_de_controle(logicas):
    regras = [Rule(*logica) for logica in logicas]
    sistema = ControlSystem(rules=regras)
    return sistema


def simular_estado(simulacao, preco, rendimento):
    simulacao.input["preço"] = preco
    # simulacao.input["preço"] = int(sys.argv[1])
    simulacao.input["rendimento"] = rendimento
    # simulacao.input["rendimento"] = int(sys.argv[2])
    simulacao.compute()


def exibir_resultado(simulacao, variaveis):
    print(simulacao.output["benefício"])
    beneficio = variaveis[2]
    beneficio.view(sim=simulacao)
    plt.show()


if __name__ == "__main__":
    _ignorado, preco, rendimento, *exibir = sys.argv
    exibir = "--exibir-graficos" in exibir
    preco, rendimento = int(preco), int(rendimento)
    main(preco, rendimento, exibir=exibir)
