# treat hallway states as nodes on graph and use dijkstra to find lowest cost way to get to end state
# My creating of the states could use some serious optimization
import dijkstar

nothing_char = "."

leftestcubby = 0
leftcubby = 1
betweenab = 2
betweenbc = 3
betweencd = 4
rightcubby = 5
rightestcubby = 6

gas = {"A": 1, "B": 10, "C": 100, "D": 1000}

room_distance = {"A": [2, 1, 1, 3, 5, 7, 8], "B": [4, 3, 1, 1, 3, 5, 6], "C": [6, 5, 3, 1, 1, 3, 4],
                 "D": [8, 7, 5, 3, 1, 1, 2]}


class AmphipodHallway:
    # represents the state of the amphipod hallway, consisting of the hallway itself and the rooms

    class room:
        def __init__(self, state, intended):
            assert len(state) == 2
            self.intended = intended
            self.state = state
            self.top_slot = state[0]
            self.bottom_slot = state[1]

        def __repr__(self):
            return f"{self.top_slot}, {self.bottom_slot}"

        def is_open(self):
            counter = 0
            for i in range(len(self.state)):
                current = self.state[i]
                if current == nothing_char:
                    counter += 1
                if current not in [nothing_char, self.intended]:
                    return 0
            return counter

        # def wants_to_move(self):
        #     if self.top_slot == self.intended and self.bottom_slot == self.intended:
        #         return False, None
        #     elif self.bottom_slot == self.intended and self.top_slot == nothing_char:
        #         return False, None
        #     elif self.bottom_slot == nothing_char and self.top_slot == nothing_char:
        #         return False, None
        #     elif self.bottom_slot == self.intended and self.top_slot != self.intended:
        #         return True, 0
        #     elif self.bottom_slot != self.intended and self.top_slot == nothing_char:
        #         return True, 1
        #     elif self.bottom_slot != self.intended and self.top_slot != nothing_char:
        #         return True, 0

        def wants_to_move(self):
            state_list = list(self.state)
            # check if any crustaceans in this room want to move (any non room owners or empty spaces)
            for char in state_list:
                if char not in [self.intended, nothing_char]:
                    first_char = [char for char in state_list if char != nothing_char][0]
                    first_char_index = state_list.index(first_char)
                    return True, first_char_index
            return False, None

    class hallway:
        def __init__(self, sevenspots):
            assert len(sevenspots) == 7
            self.sevenspots = sevenspots

        def hallway_clear_helper(self, list_to_check):
            for spot in list_to_check:
                if self.sevenspots[spot] != nothing_char:
                    return False
            return True

        # disgusting function. Assumes front of rooms aren't blocked
        # checks if you can get from a room to a spot
        def hallway_clear(self, spot, room, exiting=False):
            if exiting:
                if self.sevenspots[spot] != nothing_char:
                    return False
            if spot == leftestcubby:
                if room == "A":
                    return self.hallway_clear_helper([leftcubby])
                elif room == "B":
                    return self.hallway_clear_helper([leftcubby, betweenab])
                elif room == "C":
                    return self.hallway_clear_helper([leftcubby, betweenab, betweenbc])
                elif room == "D":
                    return self.hallway_clear_helper([leftcubby, betweenab, betweenbc, betweencd])
            elif spot == leftcubby:
                if room == "A":
                    return True
                elif room == "B":
                    return self.hallway_clear_helper([betweenab])
                elif room == "C":
                    return self.hallway_clear_helper([betweenab, betweenbc])
                elif room == "D":
                    return self.hallway_clear_helper([betweenab, betweenbc, betweencd])
            elif spot == betweenab:
                if room == "A":
                    return True
                elif room == "B":
                    return True
                elif room == "C":
                    return self.hallway_clear_helper([betweenbc])
                elif room == "D":
                    return self.hallway_clear_helper([betweenbc, betweencd])
            elif spot == betweenbc:
                if room == "A":
                    return self.hallway_clear_helper([betweenab])
                elif room == "B":
                    return True
                elif room == "C":
                    return True
                elif room == "D":
                    return self.hallway_clear_helper([betweencd])
            elif spot == betweencd:
                if room == "A":
                    return self.hallway_clear_helper([betweenab, betweenbc])
                elif room == "B":
                    return self.hallway_clear_helper([betweenbc])
                elif room == "C":
                    return True
                elif room == "D":
                    return True
            elif spot == rightestcubby:
                if room == "A":
                    return self.hallway_clear_helper([rightcubby, betweenab, betweenbc, betweencd])
                elif room == "B":
                    return self.hallway_clear_helper([rightcubby, betweencd, betweenbc])
                elif room == "C":
                    return self.hallway_clear_helper([rightcubby, betweencd])
                elif room == "D":
                    return self.hallway_clear_helper([rightcubby])
            elif spot == rightcubby:
                if room == "A":
                    return self.hallway_clear_helper([betweenab, betweenbc, betweencd])
                elif room == "B":
                    return self.hallway_clear_helper([betweencd, betweenbc])
                elif room == "C":
                    return self.hallway_clear_helper([betweencd])
                elif room == "D":
                    return True

        def __repr__(self):
            return self.sevenspots

    def __init__(self, state_string):
        assert len(state_string) == 15
        self.state_string = state_string
        self.hallway = self.hallway(state_string[0:7])
        self.rooms = {"A": self.room(state_string[7:9], "A"), "B": self.room(state_string[9:11], "B"),
                      "C": self.room(state_string[11:13], "C"), "D": self.room(state_string[13:15], "D")}

    def __repr__(self):
        return f"state: {self.state_string}, hallway: {self.hallway}, rooms: {self.rooms}"

    def get_valid_moves(self):
        valid_moves = {}
        # Check for valid moves from the things in the hallway
        for i in range(0, 7):
            letter = self.hallway.sevenspots[i]
            if letter == nothing_char:
                continue
            else:
                if self.hallway.hallway_clear(i, letter):
                    available = self.rooms[letter].is_open()
                    if available == 0:
                        continue
                    else:
                        room_string = ""
                        for room in ["A", "B", "C", "D"]:
                            if room == letter:
                                index = available - 1
                                room_string += self.rooms[room].state[:index] + letter + self.rooms[room].state[index+1:]
                            else:
                                room_string += self.rooms[room].state
                        new_state = self.hallway.sevenspots[:i] + "." + self.hallway.sevenspots[i + 1:] + room_string
                        cost = (room_distance[letter][i] + available) * gas[letter]
                        valid_moves[new_state] = cost

        # Check for valid moves from the things in the rooms
        for letter in self.rooms:  # this letter is the room letter, not the crustacean letter !
            room = self.rooms[letter]
            wants_to_move, index = room.wants_to_move()
            if wants_to_move:
                crusty_letter = self.rooms[letter].state[index]
                for i in range(0, 7):
                    if self.hallway.hallway_clear(i, letter, exiting=True):
                        room_string = ""
                        for room in ["A", "B", "C", "D"]:
                            if room == letter:
                                if index == 0:
                                    room_string += "." + self.rooms[room].bottom_slot
                                else:
                                    room_string += self.rooms[room].top_slot + "."
                            else:
                                room_string += self.rooms[room].state
                        new_state = self.hallway.sevenspots[:i] + crusty_letter + self.hallway.sevenspots[
                                                                                  i + 1:] + room_string

                        cost = (room_distance[letter][i] + 1 + index) * gas[crusty_letter]
                        valid_moves[new_state] = cost
        return valid_moves


# start_state = ".......BACDBCDA" # example
start_state = ".......BDCDCABA"  # actual
end_state = ".......AABBCCDD"
start = AmphipodHallway(start_state)
from collections import defaultdict

adjacency = {start.state_string: []}
last_adjacency = dict()
visited = set(start.state_string)
elements = [start.state_string]
edges_added = -1
graph = dijkstar.Graph()
while edges_added != 0:
    edges_added = 0
    new_elements = []
    for state in elements:
        if state not in adjacency:
            adjacency[state] = []
        new_hallway = AmphipodHallway(state)
        valid_states = new_hallway.get_valid_moves()
        for move in valid_states:
            if move not in adjacency[state]:
                graph.add_edge(new_hallway.state_string, move, valid_states[move])
                edges_added += 1
                adjacency[state].append(move)
                if move not in visited:
                    new_elements.append(move)
                    visited.add(move)
    elements = new_elements
# print(graph)
path = dijkstar.find_path(graph, start_state, end_state)
print(path)


def print_hallway(path):
    print("#############")
    print("#" + path[0:2] + "." + path[2] + "." + path[3] + "." + path[4] + "." + path[5:7] + "#")
    print("###" + path[7] + "#" + path[9] + "#" + path[11] + "#" + path[13] + "###")
    print("  #" + path[8] + "#" + path[10] + "#" + path[12] + "#" + path[14] + "#  ")
    print("  #########  ")


for node in path.nodes:
    print("---------------------")
    print_hallway(node)
print(path.total_cost)
# 18501
