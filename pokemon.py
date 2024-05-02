import random

def intput(prompt):
    return (int(input(prompt)))


class pokemon:
    def __init__(self, name, total_hitpoints, hitpoints, attack_stat, defence_stat, move_set, resistance, weakness) -> None:
        self.name = name
        self.total_hitpoints = total_hitpoints
        self.hitpoints = hitpoints
        self.attack_stat = attack_stat
        self.defence_stat = defence_stat
        self.move_set = move_set
        self.resistance = resistance
        self.weakness = weakness
        self.alive_flag = True


    def __str__(self) -> str:
        returned_moves = []
        for moves in self.move_set:
            returned_moves.append(moves.name)
        alive_status = ""
        if(self.alive_flag):
            alive_status = "Alive"
        else:
            alive_status = "Dead"
        return (f"Name: {self.name}\n"
                f"Hitpoints: {self.hitpoints}\n"
                f"Attack Stat: {self.attack_stat}\n"
                f"Defence Stat: {self.defence_stat}\n"
                f"Move Set: {returned_moves}\n"
                f"Resistance: {self.resistance}\n"
                f"Weakness: {self.weakness}\n"
                f"Pokemon Status: {alive_status}\n")


class move:
    def __init__(self, name, damage, self_damage, accuracy, move_type) -> None:
        self.name = name
        self.damage = damage
        self.self_damage = self_damage
        self.accuracy = accuracy
        self.move_type = move_type


    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Damage: {self.damage}\n"
            f"Self Damage: {self.self_damage}\n"
            f"Accuracy: {self.accuracy}%\n"
            f"Move Type: {self.move_type}\n"
        )


class item:
    def __init__(self, name, effect, item_stat, cost) -> None:
        self.name = name
        self.effect = effect
        self.item_stat = item_stat
        self.cost = cost


    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Effect: {self.effect}\n"
            f"Item Stat: {self.item_stat}\n"
            f"Cost: {self.cost}\n"
        )


class player:
    def __init__(self, name, team) -> None:
        self.name = name
        self.team = team
        self.heal_count = 2
        self.victory_flag = False


    def __str__(self) -> str:
        returned_team = []
        for member in self.team:
            returned_team.append(member.name)
        return (f"Name: {self.name}"
                f"Team: {returned_team}\n")


def main():
    global global_moveset
    global_moveset = {
        "Tail Whip": move("Tail Whip", 5, 0, 90, "Normal"),
        "Tackle": move("Tackle", 7, 2, 95, "Normal"),
        "Earthquake": move("Earthquake", 20, 2, 40, "Normal"),
        "Thunder Wave": move("Thunder Wave", 12, 2, 75, "Electric"),
        "Lightning Bolt": move("Lightning Bolt", 10, 0, 80, "Electric"),
        "Surf": move("Surf", 12, 0, 70, "Water"),
        "Water Gun": move("Water Gun", 10, 0, 85, "Water"),
        "Ember": move("Ember", 15, 5, 60, "Fire"),
        "Flamethrower": move("Flamethrower", 9, 0, 85, "Fire"),
        "Vine Whip": move("Vine Whip", 9, 0, 85, "Grass"),
        "Rock Slide": move("Rock Slide", 12, 0, 75, "Rock"),
        "Moon Blast": move("Moon Blast", 10, 1, 80, "Dark"),
        "Shadow Ball": move("Shadow Ball", 10, 0, 75, "Dark"),
        "Air Slash": move("Air Slash", 9, 0, 90, "Wind"),
        "Hurricane": move("Hurricane", 13, 0, 75, "Wind")
    }

    pikachu_moveset = [global_moveset["Tail Whip"], global_moveset["Lightning Bolt"], global_moveset["Thunder Wave"]]
    squirtle_moveset = [global_moveset["Tackle"], global_moveset["Water Gun"], global_moveset["Surf"]]
    swallow_moveset = [global_moveset["Tail Whip"], global_moveset["Air Slash"], global_moveset["Hurricane"]]
    charmander_moveset = [global_moveset["Earthquake"], global_moveset["Ember"], global_moveset["Flamethrower"]]
    gardevoir_moveset = [global_moveset["Tail Whip"], global_moveset["Vine Whip"], global_moveset["Hurricane"]]
    cyclops_moveset = [global_moveset["Tackle"], global_moveset["Shadow Ball"], global_moveset["Moon Blast"]]

    pokemon_names = ["Pikachu", "Squirtle", "Swallow", "Charmander", "Gardevoir", "Cyclops"]

    global_roster = {
        1 : pokemon("Pikachu", 30, 30, 6, 2, pikachu_moveset, "Electric", "Rock"),
        2 : pokemon("Squirtle", 40, 40, 4, 4, squirtle_moveset, "Water", "Electric"),
        3 : pokemon("Swallow", 40, 40, 5, 4, swallow_moveset, "Wind", "Fire"),
        4 : pokemon("Charmander", 50, 50, 3, 5, charmander_moveset, "Fire", "Water"),
        5 : pokemon("Gardevoir", 35, 35, 4, 4, gardevoir_moveset, "Normal", "Fire"),
        6 : pokemon("Cyclops", 45, 45, 5, 5, cyclops_moveset, "None", "None")
    }

    for idx, name in enumerate(pokemon_names):
        print(f"{idx+1}.{name}")

    team_for_p1 = []
    team_for_p2 = []
    
    for i in range(3,0,-1):
        choice = int(input(f"Pick a pokemon from the above list ({i} left): "))
        team_for_p1.append(global_roster[choice])
    
    for i in range(3,0,-1):
        choice = int(input(f"Pick a pokemon from the above list ({i} left): "))
        team_for_p2.append(global_roster[choice])


    player_name1 = input("Enter your name: ")
    player_name2 = input("Enter your name: ")

    p1 = player(player_name1, team_for_p1)
    p2 = player(player_name2, team_for_p2)

    player_turn = False
    choice = 0
    p1_current_pokemon = p1.team.pop(0) ; p2_current_pokemon = p2.team.pop(0)
    while(1):
        player_turn = not player_turn
        if(player_turn == True):
            while(1):
                print(f"\n{p1.name}'s Turn")
                print("1. Attack\n2. Heal pokemon")
                choice = intput("Enter your choice: ")
                if(choice == 1):
                    print(f"Available moves for {p1.name}'s {p1_current_pokemon.name}")
                    for idx, moves in enumerate(p1_current_pokemon.move_set):
                        print(f"{idx+1}. {moves.name}")
                    choice = intput("Enter your choice: ")
                    print(f"\n{p1.name}'s {p1_current_pokemon.name} used {p1_current_pokemon.move_set[choice-1].name}")
                    if(random.randint(1,100) > p1_current_pokemon.move_set[choice-1].accuracy):
                        print("Attack Missed!")
                        break
                    total_damage = 0
                    total_damage += p1_current_pokemon.move_set[choice-1].damage + p1_current_pokemon.attack_stat
                    total_damage -= p2_current_pokemon.defence_stat
                    if(p1_current_pokemon.move_set[choice-1].move_type == p2_current_pokemon.weakness):
                        print("Weakness attacked!")
                        total_damage *= 1.5
                    elif(p1_current_pokemon.move_set[choice-1].move_type == p2_current_pokemon.resistance):
                        total_damage *= 0.5
                    p2_current_pokemon.hitpoints -= total_damage
                    if p2_current_pokemon.hitpoints < 0:
                        p2_current_pokemon.hitpoints = 0

                    p1_current_pokemon.hitpoints -= p1_current_pokemon.move_set[choice-1].self_damage
                    if p1_current_pokemon.hitpoints < 0:
                        p1_current_pokemon.hitpoints = 0

                    print(f"{p1.name}'s {p1_current_pokemon.name} HP: {p1_current_pokemon.hitpoints}\n"
                        f"{p2.name}'s {p2_current_pokemon.name} HP: {p2_current_pokemon.hitpoints}\n")

                    if(p2_current_pokemon.hitpoints <= 0):
                        print(f"{p2.name}'s {p2_current_pokemon.name} has died")
                        if len(p2.team) != 0:
                            p2_current_pokemon = p2.team.pop(0)
                            print(f"{p2.name} sent out {p2_current_pokemon.name}")
                            continue
                        else:
                            p1.victory_flag = True

                    if(p1_current_pokemon.hitpoints <= 0):
                        print(f"{p1.name}'s {p1_current_pokemon.name} has died")
                        p1_current_pokemon.alive_flag = False
                        if len(p1.team) != 0:
                            p1_current_pokemon = p1.team.pop(0)
                            print(f"{p1.name} sent out {p1_current_pokemon.name}")
                            continue
                        else:
                            p2.victory_flag = True
                    break

                elif(choice == 2):
                    if(p1.heal_count == 0):
                        print("No heals left!")
                    else:
                        p1_current_pokemon.hitpoints = min((p1_current_pokemon.hitpoints + 20), p1_current_pokemon.total_hitpoints)
                        p1.heal_count -= 1
                        print(f"Pokemon healed! "
                            f"HP is now {p1_current_pokemon.hitpoints}"
                            f"\n{p1.heal_count} heals remaining!")
                        break
        else:
            while(1):
                print(f"\n{p2.name}'s Turn")
                print("1. Attack\n2. Heal pokemon")
                choice = intput("Enter your choice: ")
                if(choice == 1):
                    print(f"Available moves for {p2.name}'s {p2_current_pokemon.name}")
                    for idx, moves in enumerate(p2_current_pokemon.move_set):
                        print(f"{idx+1}. {moves.name}")
                    choice = intput("Enter your choice: ")
                    print(f"\n{p2.name}'s {p2_current_pokemon.name} used {p2_current_pokemon.move_set[choice-1].name}")
                    if(random.randint(1,100) > p2_current_pokemon.move_set[choice-1].accuracy):
                        print("Attack Missed!")
                        break
                    total_damage = 0
                    total_damage += p2_current_pokemon.move_set[choice-1].damage + p2_current_pokemon.attack_stat
                    total_damage -= p1_current_pokemon.defence_stat
                    if(p2_current_pokemon.move_set[choice-1].move_type == p1_current_pokemon.weakness):
                        print("Weakness attacked!")
                        total_damage *= 1.5
                    elif(p2_current_pokemon.move_set[choice-1].move_type == p1_current_pokemon.resistance):
                        total_damage *= 0.5
                    p1_current_pokemon.hitpoints -= total_damage
                    if p1_current_pokemon.hitpoints < 0:
                        p1_current_pokemon.hitpoints = 0

                    p2_current_pokemon.hitpoints -= p2_current_pokemon.move_set[choice-1].self_damage
                    if p2_current_pokemon.hitpoints < 0:
                        p2_current_pokemon.hitpoints = 0

                    print(f"{p1.name}'s {p1_current_pokemon.name} HP: {p1_current_pokemon.hitpoints}\n"
                        f"{p2.name}'s {p2_current_pokemon.name} HP: {p2_current_pokemon.hitpoints}\n")

                    if(p1_current_pokemon.hitpoints <= 0):
                        print(f"{p1.name}'s {p1_current_pokemon.name} has died")
                        p1_current_pokemon.alive_flag = False
                        if len(p1.team) != 0:
                            p1_current_pokemon = p1.team.pop(0)
                            print(f"{p1.name} sent out {p1_current_pokemon.name}")
                            continue
                        else:
                            p2.victory_flag = True

                    if(p2_current_pokemon.hitpoints <= 0):
                        print(f"{p2.name}'s {p2_current_pokemon.name} has died")
                        if len(p2.team) != 0:
                            p2_current_pokemon = p2.team.pop(0)
                            print(f"{p2.name} sent out {p2_current_pokemon.name}")
                            continue
                        else:
                            p1.victory_flag = True
                    break

                elif(choice == 2):
                    if(p2.heal_count == 0):
                        print("No heals left!")
                    else:
                        p2_current_pokemon.hitpoints = min((p2_current_pokemon.hitpoints + 20), p2_current_pokemon.total_hitpoints)
                        p2.heal_count -= 1
                        print(f"Pokemon healed! "
                            f"HP is now {p2_current_pokemon.hitpoints}"
                            f"\n{p2.heal_count} heals remaining!")
                        break
        
        if(p1.victory_flag and not p2.victory_flag):
            print(f"{p1.name} wins!")
            break
        elif(p2.victory_flag and not p1.victory_flag):
            print(f"{p2.name} wins!")
            break
        elif(p2.victory_flag and p1.victory_flag):
            print("Its a draw!")
            break


if __name__ == "__main__":
    main()