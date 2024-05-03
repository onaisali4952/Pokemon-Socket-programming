# Server File

import socket
import threading
import random
import queue

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

player_names_queue = queue.Queue()
player_team_queue = queue.Queue()
team_for_p1 = []
team_for_p2 = []
player_name1 = ""
player_name2 = ""
lock2 = threading.Lock()
lock1 = threading.Lock()

def handle_client(client_socket, addr, player_id):
    print(f"Accepted connection from {addr} with player ID {player_id}")
    try:
        server_message = "Enter your name: "
        client_socket.send(bytes(server_message, 'UTF-8'))
        client_message = client_socket.recv(1024).decode()
        if(player_id == 1):
            player_name1 = client_message
        elif(player_id == 2):
            player_name2 = client_message

        server_message = ""
        for idx, name in enumerate(pokemon_names):
            server_message += f"{idx+1}.{name} \n"
        
        if(player_id == 1):
            for i in range(3,0,-1):
                server_message += f"Pick a pokemon from the above list ({i} left): "
                client_socket.send(bytes(server_message, 'UTF-8'))
                server_message = ""
                client_message = client_socket.recv(1024).decode()
                if(not (0 < int(client_message) < 6)):
                    continue
                team_for_p1.append(global_roster[int(client_message)])
        elif(player_id == 2):
            for i in range(3,0,-1):
                server_message += f"Pick a pokemon from the above list ({i} left): "
                client_socket.send(bytes(server_message, 'UTF-8'))
                server_message = ""
                client_message = client_socket.recv(1024).decode()
                if(not (0 < int(client_message) < 6)):
                    continue
                team_for_p2.append(global_roster[int(client_message)])

        with lock1:
            if(player_id == 1):
                player_names_queue.put(player_name1)
                player_team_queue.put(team_for_p1)
            if(player_id == 2):
                player_names_queue.put(player_name2)
                player_team_queue.put(team_for_p2)

    finally:
        pass

def handle_game(client_socket, addr, player_id, p1, p2, p1_poke_idx, p2_poke_idx):

    print(f"Continued connection with {addr} with player ID {player_id}")

    player_turn = 1
    while(not p1.victory_flag and not p2.victory_flag):
        if(player_id == 1):
            server_message =(f"{p1.name}'s {p1.team[p1_poke_idx].name} HP: {p1.team[p1_poke_idx].hitpoints}\n"+
                                f"{p2.name}'s {p2.team[p2_poke_idx].name} HP: {p2.team[p2_poke_idx].hitpoints}\n")
            server_message += "\nEnter anything to proceed: "
            client_socket.send(bytes(server_message, 'UTF-8'))
            client_socket.recv(1024).decode()    
            with lock1:
                with lock2:        
                    while(1):
                        server_message =(f"{p1.name}'s {p1.team[p1_poke_idx].name} HP: {p1.team[p1_poke_idx].hitpoints}\n"+
                                         f"{p2.name}'s {p2.team[p2_poke_idx].name} HP: {p2.team[p2_poke_idx].hitpoints}\n")
                        server_message += "\n1. Attack\n2. Heal pokemon\nEnter your choice: "
                        client_socket.send(bytes(server_message, 'UTF-8'))
                        server_message = ""
                        menu_choice = int(client_socket.recv(1024).decode())
                        if(menu_choice != 1 and menu_choice != 2):
                            continue
                        if(menu_choice == 1):
                            server_message = f"Available moves for {p1.name}'s {p1.team[p1_poke_idx].name}\n"
                            for idx, moves in enumerate(p1.team[p1_poke_idx].move_set):
                                server_message += f"{idx+1}.{moves.name}\n"
                            server_message += "Enter your choice: "
                            client_socket.send(bytes(server_message, 'UTF-8'))
                            move_choice = int(client_socket.recv(1024).decode())
                            server_message = f"\n{p1.name}'s {p1.team[p1_poke_idx].name} used {p1.team[p1_poke_idx].move_set[move_choice-1].name}"
                            server_message += "\nEnter anything to proceed: "
                            client_socket.send(bytes(server_message, 'UTF-8'))
                            client_socket.recv(1024).decode()
                            if(random.randint(1,100) > p1.team[p1_poke_idx].move_set[move_choice-1].accuracy):
                                server_message = "\nAttack Missed!"
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                break
                            total_damage = 0
                            total_damage += p1.team[p1_poke_idx].move_set[move_choice-1].damage + p1.team[p1_poke_idx].attack_stat
                            total_damage -= p2.team[p2_poke_idx].defence_stat
                            if(p1.team[p1_poke_idx].move_set[move_choice-1].move_type == p2.team[p2_poke_idx].weakness):
                                server_message = "\nWeakness attacked!"
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                total_damage *= 1.5
                            elif(p1.team[p1_poke_idx].move_set[move_choice-1].move_type == p2.team[p2_poke_idx].resistance):
                                total_damage *= 0.5
                            p2.team[p2_poke_idx].hitpoints -= total_damage
                            if p2.team[p2_poke_idx].hitpoints < 0:
                                p2.team[p2_poke_idx].hitpoints = 0

                            p1.team[p1_poke_idx].hitpoints -= p1.team[p1_poke_idx].move_set[move_choice-1].self_damage
                            if p1.team[p1_poke_idx].hitpoints < 0:
                                p1.team[p1_poke_idx].hitpoints = 0

                            if(p2.team[p2_poke_idx].hitpoints <= 0):
                                server_message = f"\n{p2.name}'s {p2.team[p2_poke_idx].name} has died"
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                p2_poke_idx += 1
                                if(p2_poke_idx < 3):
                                    server_message = f"{p2.name} sent out {p2.team[p2_poke_idx].name}"
                                    server_message += "\nEnter anything to proceed: "
                                    client_socket.send(bytes(server_message, 'UTF-8'))
                                    client_socket.recv(1024).decode()
                                    continue
                                else:
                                    p1.victory_flag = True

                        elif(menu_choice == 2):
                            if(p1.heal_count == 0):
                                server_message = "No heals left!"
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                            else:
                                p1.team[p1_poke_idx].hitpoints = min((p1.team[p1_poke_idx].hitpoints + 20), p1.team[p1_poke_idx].total_hitpoints)
                                p1.heal_count -= 1
                                server_message +=(f"Pokemon healed! "
                                                    f"HP is now {p1.team[p1_poke_idx].hitpoints}"
                                                    f"\n{p1.heal_count} heals remaining!\n"
                                                    f"Enter anything to proceed: ")
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                break
                        break

        if(player_id == 2):
            server_message =(f"{p1.name}'s {p1.team[p1_poke_idx].name} HP: {p1.team[p1_poke_idx].hitpoints}\n"+
                                f"{p2.name}'s {p2.team[p2_poke_idx].name} HP: {p2.team[p2_poke_idx].hitpoints}\n")
            server_message += "\nEnter anything to proceed: "
            client_socket.send(bytes(server_message, 'UTF-8'))
            client_socket.recv(1024).decode()
            with lock2:
                with lock1:
                    while(1):
                        server_message = "1. Attack\n2. Heal pokemon\nEnter your choice: "
                        client_socket.send(bytes(server_message, 'UTF-8'))
                        menu_choice = int(client_socket.recv(1024).decode())
                        if(menu_choice != 1 and menu_choice != 2):
                            continue
                        if(menu_choice == 1):
                            server_message = (f"Available moves for {p2.name}'s {p2.team[p2_poke_idx].name}")
                            for idx, moves in enumerate(p2.team[p2_poke_idx].move_set):
                                server_message += f"{idx+1}.{moves.name}\n"
                            server_message += "Enter your choice: "
                            client_socket.send(bytes(server_message, 'UTF-8'))
                            move_choice = int(client_socket.recv(1024).decode())
                            server_message = (f"\n{p2.name}'s {p2.team[p2_poke_idx].name} used {p2.team[p2_poke_idx].move_set[move_choice-1].name}")
                            server_message += "\nEnter anything to proceed: "
                            client_socket.send(bytes(server_message, 'UTF-8'))
                            client_socket.recv(1024).decode()
                            if(random.randint(1,100) > p2.team[p2_poke_idx].move_set[move_choice-1].accuracy):
                                server_message = ("Attack Missed!")
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                break
                            total_damage = 0
                            total_damage += p2.team[p2_poke_idx].move_set[move_choice-1].damage + p2.team[p2_poke_idx].attack_stat
                            total_damage -= p1.team[p1_poke_idx].defence_stat
                            if(p2.team[p2_poke_idx].move_set[move_choice-1].move_type == p1.team[p1_poke_idx].weakness):
                                server_message = ("Weakness attacked!")
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                total_damage *= 1.5
                            elif(p2.team[p2_poke_idx].move_set[move_choice-1].move_type == p1.team[p1_poke_idx].resistance):
                                total_damage *= 0.5
                            p1.team[p1_poke_idx].hitpoints -= total_damage
                            if p1.team[p1_poke_idx].hitpoints < 0:
                                p1.team[p1_poke_idx].hitpoints = 0

                            p2.team[p2_poke_idx].hitpoints -= p2.team[p2_poke_idx].move_set[move_choice-1].self_damage
                            if p2.team[p2_poke_idx].hitpoints < 0:
                                p2.team[p2_poke_idx].hitpoints = 0

                                    
                            if(p1.team[p1_poke_idx].hitpoints <= 0):
                                server_message = (f"{p1.name}'s {p1.team[p1_poke_idx].name} has died")
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                p1.team[p1_poke_idx].alive_flag = False
                                p1_poke_idx += 1
                                if p1_poke_idx < 3:
                                    server_message = (f"{p1.name} sent out {p1.team[p1_poke_idx].name}")
                                    server_message += "\nEnter anything to proceed: "
                                    client_socket.send(bytes(server_message, 'UTF-8'))
                                    client_socket.recv(1024).decode()
                                    continue
                                else:
                                    p2.victory_flag = True

                            if(p2.team[p2_poke_idx].hitpoints <= 0):
                                server_message = (f"{p2.name}'s {p2.team[p2_poke_idx].name} has died")
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                p2_poke_idx += 1
                                if p2_poke_idx < 3:
                                    server_message = (f"{p2.name} sent out {p2.team[p2_poke_idx].name}")
                                    server_message += "\nEnter anything to proceed: "
                                    client_socket.send(bytes(server_message, 'UTF-8'))
                                    client_socket.recv(1024).decode()
                                    continue
                                else:
                                    p1.victory_flag = True
                            break

                        elif(menu_choice == 2):
                            if(p2.heal_count == 0):
                                server_message = ("No heals left!")
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                            else:
                                p2.team[p2_poke_idx].hitpoints = min((p2.team[p2_poke_idx].hitpoints + 20), p2.team[p2_poke_idx].total_hitpoints)
                                p2.heal_count -= 1
                                server_message = (f"Pokemon healed! "
                                    f"HP is now {p2.team[p2_poke_idx].hitpoints}"
                                    f"\n{p2.heal_count} heals remaining!")
                                server_message += "\nEnter anything to proceed: "
                                client_socket.send(bytes(server_message, 'UTF-8'))
                                client_socket.recv(1024).decode()
                                break
                        break            

        server_message = (f"{p1.name}'s {p1.team[p1_poke_idx].name} HP: {p1.team[p1_poke_idx].hitpoints}\n"
                          f"{p2.name}'s {p2.team[p2_poke_idx].name} HP: {p2.team[p2_poke_idx].hitpoints}\n")
        server_message += "\nEnter anything to proceed: "
        client_socket.send(bytes(server_message, 'UTF-8'))
        client_socket.recv(1024).decode()

        if(p1.victory_flag and not p2.victory_flag):
            server_message = (f"{p1.name} wins!")
            break
        elif(p2.victory_flag and not p1.victory_flag):
            server_message = (f"{p2.name} wins!")
            break
        elif(p2.victory_flag and p1.victory_flag):
            server_message = ("Its a draw!")
            break

        if(player_turn == 1):
            player_turn = 2
        else:
            player_turn = 1

# Main function
def main():    

    server_socket = socket.socket()
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server listening on localhost:9999")
    client_socket = {}
    addr = {}
 
    try:
        player_id = 1
        client_handlers = []
        while player_id <= 2:
            client_socket[player_id], addr[player_id] = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket[player_id], addr[player_id], player_id))
            client_handlers.append(client_handler)
            client_handler.start()
            player_id += 1

        for clients in client_handlers:
            clients.join()

        player_name1 = player_names_queue.get()
        player_names_queue.put(player_name1)
        player_name2 = player_names_queue.get()
        player_names_queue.put(player_name2)
        team_for_p1 = player_team_queue.get()
        player_team_queue.put(team_for_p1)
        team_for_p2 = player_team_queue.get()
        player_team_queue.put(team_for_p2)
        p1 = player(player_name1, team_for_p1)
        p2 = player(player_name2, team_for_p2)

        player_id = 1
        client_handlers = []
        while player_id <= 2:
            # client_socket, addr = server_socket.accept()   
            game_client_handler = threading.Thread(target=handle_game, args=(client_socket[player_id], addr[player_id], player_id, p1, p2, 0, 0))
            client_handlers.append(game_client_handler)
            game_client_handler.start()
            player_id += 1

        for clients in client_handlers:
            clients.join()

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()