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
        "Lightning Bolt": move("Lightning Bolt", 10, 0, 80, "Electric"),
        "Tackle": move("Tackle", 7, 2, 95, "Normal"),
        "Water Gun": move("Water Gun", 10, 0, 85, "Water"),
        "Ember": move("Ember", 15, 5, 60, "Fire"),
        "Vine Whip": move("Vine Whip", 9, 0, 85, "Grass"),
        "Rock Slide": move("Rock Slide", 12, 0, 75, "Rock")
    }

    pikachu_moveset = [global_moveset["Tail Whip"], global_moveset["Lightning Bolt"]]
    pikachu_object_1 = pokemon("Pikachu", 30, 30, 6, 2, pikachu_moveset, "Electric", "Rock")
    pikachu_object_2 = pokemon("Pikachu", 30, 30, 6, 2, pikachu_moveset, "Electric", "Rock")
    squirtle_moveset = [global_moveset["Tackle"], global_moveset["Water Gun"]]
    squirtle_object_1 = pokemon("Squirtle", 40, 40, 4, 4, squirtle_moveset, "Water", "Electric")
    squirtle_object_2 = pokemon("Squirtle", 40, 40, 4, 4, squirtle_moveset, "Water", "Electric")

    print(pikachu_object_1)
    print(global_moveset["Ember"])

    team_for_p1 = [pikachu_object_1, squirtle_object_1]
    team_for_p2 = [squirtle_object_2, pikachu_object_2]
    p1 = player("Onais", team_for_p1)
    p2 = player("Zohaib", team_for_p2)

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
                    p2_current_pokemon.hitpoints -= (p1_current_pokemon.move_set[choice-1].damage + p1_current_pokemon.attack_stat - p2_current_pokemon.defence_stat)
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
                            p1.victory_flag = True
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
            # break
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
                    p1_current_pokemon.hitpoints -= (p2_current_pokemon.move_set[choice-1].damage+ p2_current_pokemon.attack_stat-p1_current_pokemon.defence_stat)
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
                            p1.victory_flag = True

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