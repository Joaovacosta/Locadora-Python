from classes import *

locadora_python = locadora("Locadora Python", "Jundiaí")

itens_locadora = [
    item("Ea Sports FC 25", "Livre", "Esportes", True),
    item("The Last of US Part I", 16, "Ação/Suspense", True),
    item("Hollow Knight", 12, "Aventura", True),
    item("God of War Ragnarök", 18, "Aventura/Ação", True),
    item("Grand Theft Auto V", 18, "Ação/Mundo Aberto", True),
    item("Mortal Kombat 11", 18, "Luta", True),
    item("Forza Horizon 5", "Livre", "Corrida", True),
    item("Final Fantasy VII Remake", 14, "RPG", True),
    item("Halo Infinite", 14, "Tiro", True),
    item("Resident Evil 4 Remake", 18, "Terror/Sobrevivência", True),
    item("Far Cry 6", 18, "Ação/Mundo Aberto/FPS", True)
]
filmes_locadora = [
    item("Como eu era antes de você", 12, "Romance", True),
    item("Frozen", 10, "Animação", True),
    item("O Senhor dos Anéis: A Sociedade do Anel", 12, "Fantasia", True),
    item("Vingadores: Ultimato", 12, "Ação", True),
    item("Homem-Aranha: No Aranhaverso", 12, "Animação", True),
    item("Jurassic Park", 12, "Ficção Científica", True),
    item("Titãs", 18, "Aventura", True)
]


def additem():
    for i in itens_locadora + filmes_locadora:
        locadora_python.adicionar_item(i)

def devolucao(nome_item):
    for i in locadora_python.itens:
        if i.nome == nome_item:
            i.disponivel = True
            print(f'O item "{nome_item}" foi devolvido com sucesso!')
            return
    print(f'O item "{nome_item}" não foi encontrado na locadora.')
