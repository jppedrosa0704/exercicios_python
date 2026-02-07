import os
import json


# ==== Utilities =====
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# ==== File Handling ====
def salvar_dados(players, arquivo="players.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(players, f, ensure_ascii=False, indent=4)


def carregar_dados(arquivo="players.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# ==== Add New Player ====
def add_player(players):
    limpar_tela()

    name = input("What’s the name of the player? ").strip()

    if not name or name.isdigit():
        print("⚠️ Invalid name.")
        input('Type "Enter" to continue...')
        return

    for n in players:
        if name.title() == n['name']:
            print('⚠️ Player name already exists.')
            input('Type "Enter" to continue...')
            return

    while True:
        try:
            score = int(input("What’s the score of the player? "))
            if score < 0:
                print('⚠️ Score cannot be negative.')
            else:
                break
        except ValueError:
            print('⚠️ Invalid score.')

    data = {'name': name.title(), 'score': score}
    players.append(data)

    players.sort(key=lambda p: p['score'], reverse=True)
    salvar_dados(players)

    print(f"💾 '{name}' saved successfully!")
    input('Type "Enter" to continue...')


# ==== Record Points ====
def record_point(players):
    while True:
        limpar_tela()
        print("==== Add points to players ====")

        for i, jogador in enumerate(players, start=1):
            print(f"{i}. {jogador['name']:<12} score: {jogador['score']}")

        name = input("\nPlayer name (Press ENTER to cancel): ").title().strip()

        if not name:
            print("Operation canceled.")
            input('Type "Enter" to continue...')
            return

        player = next((p for p in players if p["name"] == name), None)

        if not player:
            print("⚠️ Player not found.")
            input('Type "Enter" to continue...')
            continue

        break

    while True:
        try:
            add_score = int(input("How many points do you want to add? "))
            if add_score <= 0:
                print("⚠️ Points must be greater than zero.")
            else:
                break
        except ValueError:
            print("⚠️ Invalid value.")

    player["score"] += add_score

    players.sort(key=lambda p: p['score'], reverse=True)
    salvar_dados(players)

    print(f"✅ {add_score} points added to {player['name']}!")
    input('Type "Enter" to continue...')


# ==== List Ranking ====
def list_ranking(players):
    limpar_tela()
    print("====== LIST RANKING ======\n")

    for i, jogador in enumerate(players, start=1):
        print(f"{i}º {jogador['name']:<12} score: {jogador['score']}")

    input('\nType "Enter" to continue...')


# ==== Menu ====
def menu():
    print("[1] Add Player")
    print("[2] Record Points")
    print("[3] List Ranking")
    print("[4] Exit")


# ==== Main Program ====
players = carregar_dados()
players.sort(key=lambda p: p['score'], reverse=True)

while True:
    limpar_tela()
    menu()

    try:
        opt = int(input("\nChoose an option: "))
    except ValueError:
        print("⚠️ Invalid option.")
        input('Type "Enter" to continue...')
        continue

    match opt:
        case 1:
            add_player(players)
        case 2:
            record_point(players)
        case 3:
            list_ranking(players)
        case 4:
            break
        case _:
            print("⚠️ Option not available.")
            input('Type "Enter" to continue...')

print("\nFinal Players List:")
print(*players, sep='\n')
