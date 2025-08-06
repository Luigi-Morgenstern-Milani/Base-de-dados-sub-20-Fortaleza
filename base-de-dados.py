base_fortaleza = [
    {
        "nome": "Cássio Penafiel Acosta",
        "idade": 20,
        "posicao": "Goleiro",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 17,
        "total_de_minutos_jogados": 1530,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "Guilherme Moura da Fonseca",
        "idade": 20,
        "posicao": "Defensor",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 15,
        "total_de_minutos_jogados": 1329,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "Victor Kauã Guimarães Rocha",
        "idade": 18,
        "posicao": "Defensor",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 15,
        "total_de_minutos_jogados": 1188,
        "gols": 2,
        "assistencias": 0
    },
    {
        "nome": "Rafael da Silva Vaz",
        "idade": 19,
        "posicao": "Defensor",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 13,
        "total_de_minutos_jogados": 1139,
        "gols": 1,
        "assistencias": 0
    },
    {
        "nome": "Arthur Barbosa Moura de Oliveira",
        "idade": 19,
        "posicao": "Defensor",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 13,
        "total_de_minutos_jogados": 581,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "Lucas Emanoel de Abreu dos Reis",
        "idade": 19,
        "posicao": "Meio-campista",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 17,
        "total_de_minutos_jogados": 1356,
        "gols": 4,
        "assistencias": 0
    },
    {
        "nome": "Dimas Cândido de Oliveira Filho",
        "idade": 20,
        "posicao": "Meio-campista",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 18,
        "total_de_minutos_jogados": 830,
        "gols": 2,
        "assistencias": 0
    },
    {
        "nome": "João Vitor Hipólito Costa",
        "idade": 20,
        "posicao": "Meio-campista",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 15,
        "total_de_minutos_jogados": 1000,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "Landerson Costa Araujo",
        "idade": 18,
        "posicao": "Atacante",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 18,
        "total_de_minutos_jogados": 1573,
        "gols": 2,
        "assistencias": 0
    },
    {
        "nome": "Tomás Ignacio Roco Latorre",
        "idade": 19,
        "posicao": "Atacante",
        "nacionalidade": "Chileno",
        "numero_de_partidas": 17,
        "total_de_minutos_jogados": 1062,
        "gols": 4,
        "assistencias": 0
    },
    {
        "nome": "Henrique Cerri Leite",
        "idade": 19,
        "posicao": "Atacante",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 14,
        "total_de_minutos_jogados": 611,
        "gols": 1,
        "assistencias": 0
    },
    {
        "nome": "César Augusto Braga Rodrígues",
        "idade": 19,
        "posicao": "Goleiro",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 2,
        "total_de_minutos_jogados": 180,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "Kauan Richard Leal Silva",
        "idade": 20,
        "posicao": "Defensor",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 11,
        "total_de_minutos_jogados": 846,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "João Vitor da Rosa",
        "idade": 20,
        "posicao": "Defensor",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 7,
        "total_de_minutos_jogados": 437,
        "gols": 0,
        "assistencias": 0
    },
    {
        "nome": "Jairo Joel Reyes Castillo",
        "idade": 19,
        "posicao": "Meio-campista",
        "nacionalidade": "Equatoriano",
        "numero_de_partidas": 12,
        "total_de_minutos_jogados": 532,
        "gols": 0,
        "assistencias": 1
    },
    {
        "nome": "Bruno Domingos Branco",
        "idade": 19,
        "posicao": "Atacante",
        "nacionalidade": "Brasileiro",
        "numero_de_partidas": 16,
        "total_de_minutos_jogados": 524,
        "gols": 1,
        "assistencias": 0
    }
]

# Exibindo informações específicas conforme o desafio

# Atacante
print(f"Atacante: {base_fortaleza[8]['nome']}, Gols: {base_fortaleza[8]['gols']}, Partidas: {base_fortaleza[8]['numero_de_partidas']}")

# Defensor (Zagueiro)
print(f"Zagueiro: {base_fortaleza[1]['nome']}, Idade: {base_fortaleza[1]['idade']}, Partidas: {base_fortaleza[1]['numero_de_partidas']}, Minutos jogados: {base_fortaleza[1]['total_de_minutos_jogados']}")

# Meio-campista
print(f"Meio-campista: {base_fortaleza[5]['nome']}, Posição: {base_fortaleza[5]['posicao']}, Nacionalidade: {base_fortaleza[5]['nacionalidade']}, Assistências: {base_fortaleza[5]['assistencias']}")
