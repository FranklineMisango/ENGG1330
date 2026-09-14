import plane
import random
import os
# Please read through the code and see if you understand what it's doing
class Board:
    # All blocks are 3*1
    # Background and text colours are done by ANSI escape codes in the format of "\33[{background colour code};{foreground colour code}m" + "string to be displayed"
    v = "\33[40;94m" + "   " # Void block, serving as background for the game board
    h = "\33[40;94m" + "---" # Hyphen block
    j = "\33[40;94m" + "<--" # Hyphen block with arrow head
    # START INITIALIZE
    plane_a = plane.Plane("r","A")
    plane_b = plane.Plane("r","B")
    plane_c = plane.Plane("r","C")
    plane_d = plane.Plane("r","D")
    plane_e = plane.Plane("g","E")
    plane_f = plane.Plane("g","F")
    plane_g = plane.Plane("g","G")
    plane_h = plane.Plane("g","H")
    plane_i = plane.Plane("y","I")
    plane_j = plane.Plane("y","J")
    plane_k = plane.Plane("y","K")
    plane_l = plane.Plane("y","L")
    plane_m = plane.Plane("b","M")
    plane_n = plane.Plane("b","N")
    plane_o = plane.Plane("b","O")
    plane_p = plane.Plane("b","P")
    player_to_string = {"r":"red","g":"green","y":"yellow","b":"blue"}
    colour_to_start_pt = {"y":0,"b":39,"r":26,"g":13}
    colour_to_landing_strip_pt = {"y":49, "g":10,"r":23,"b":36}
    player_to_emoji = {"y":"🟡","r":"🔴","g":"🟢","b":"🔵"}
    expander = "                                                                                "
    # The __init__ function is run as soon as and every time an object of the class is created ("initialized")
    def __init__(self):
        # Main board
        self.x = self.construct_board(52, "a")
        # Hangar yellow, green, blue, red
        self.hy = self.construct_board(5, "y")
        self.hg = self.construct_board(5, "g")
        self.hb = self.construct_board(5, "b")
        self.hr = self.construct_board(5, "r")
        # Landing strips green, yellow, red, blue
        self.lg = self.construct_board(6, "g")
        self.ly = self.construct_board(6, "y")
        self.lr = self.construct_board(6, "r")
        self.lb = self.construct_board(6, "b")
        self.landed_planes = {"r":0,"g":0,"b":0,"y":0}
        self.winner = None
        self.current_player = "y"
        #Red color       planes should start in the hangar
        self.change_cell("hr",0,Board.plane_a)
        self.change_cell("hr",1,Board.plane_b)
        self.change_cell("hr",2,Board.plane_c)
        self.change_cell("hr",3,Board.plane_d)
        #Blue color
        self.change_cell("hb",0,Board.plane_m)
        self.change_cell("hb",1,Board.plane_n)
        self.change_cell("hb",2,Board.plane_o)
        self.change_cell("hb",3,Board.plane_p)
        #yellow color
        self.change_cell("hy",0,Board.plane_i)
        self.change_cell("hy",1,Board.plane_j)
        self.change_cell("hy",2,Board.plane_k)
        self.change_cell("hy",3,Board.plane_l)
        #green color
        self.change_cell("hg",0,Board.plane_e)
        self.change_cell("hg",1,Board.plane_f)
        self.change_cell("hg",2,Board.plane_g)
        self.change_cell("hg",3,Board.plane_h)
    # The __repr__ function returns a string to be printed when you call print(Board_instance)
    def __repr__(self):
        print(self.cell("n","n",void=True))
        os.system("clear")
        # Code to display the board
        return f"""
{Board.v}                                                                                                     





{Board.v}{Board.expander}                                 {self.hg[4]}{Board.h}----           
{Board.v}{Board.expander}               {self.x[7]}{self.x[8]}{self.x[9]}{self.x[10]}{self.x[11]}{self.x[12]}{self.x[13]}{Board.v}   |           
{Board.v}{Board.expander}   {self.hy[0]}{self.hy[1]}{Board.v}{self.x[6]}{Board.v}      {self.lg[0]}{Board.v}      {self.x[14]}{Board.v}{self.hg[3]}{self.hg[2]}{Board.v}   
{Board.v}{Board.expander}---{self.hy[2]}{self.hy[3]}{Board.v}{self.x[5]}{Board.v}      {self.lg[1]}{Board.v}      {self.x[15]}{Board.v}{self.hg[1]}{self.hg[0]}{Board.v}   
{Board.v}{Board.expander}|           {self.x[4]}{Board.h}------{self.lg[2]}{Board.h}----->{self.x[16]}{Board.v}
{Board.v}{Board.expander}{self.hy[4]}{self.x[0]}{self.x[1]}{self.x[2]}{self.x[3]}{Board.v}      {self.lg[3]}{Board.v}      {self.x[17]}{self.x[18]}{self.x[19]}{self.x[20]}{Board.v}   
{Board.v}{Board.expander}   {self.x[51]}{Board.v}    ˄          {self.lg[4]}{Board.v}       |       {self.x[21]}{Board.v}   
{Board.v}{Board.expander}   {self.x[50]}{Board.v}    |          {self.lg[5]}{Board.v}       |       {self.x[22]}{Board.v}   
{Board.v}{Board.expander}   {self.x[49]}{self.ly[0]}{self.ly[1]}{self.ly[2]}{self.ly[3]}{self.ly[4]}{self.ly[5]}{Board.v}{self.lr[5]}{self.lr[4]}{self.lr[3]}{self.lr[2]}{self.lr[1]}{self.lr[0]}{self.x[23]}{Board.v}   
{Board.v}{Board.expander}   {self.x[48]}{Board.v}    |          {self.lb[5]}{Board.v}       |       {self.x[24]}{Board.v}   
{Board.v}{Board.expander}   {self.x[47]}{Board.v}    |          {self.lb[4]}{Board.v}       ˅       {self.x[25]}{Board.v}   
{Board.v}{Board.expander}   {self.x[46]}{self.x[45]}{self.x[44]}{self.x[43]}{Board.v}      {self.lb[3]}{Board.v}      {self.x[29]}{self.x[28]}{self.x[27]}{self.x[26]}{self.hr[4]}{Board.v}
{Board.v}{Board.expander}            {self.x[42]}{Board.j}------{self.lb[2]}{Board.h}------{self.x[30]}{Board.v}        |   
{Board.v}{Board.expander}   {self.hb[0]}{self.hb[1]}{Board.v}{self.x[41]}{Board.v}      {self.lb[1]}{Board.v}      {self.x[31]}{Board.v}{self.hr[2]}{self.hr[3]}{Board.h}   
{Board.v}{Board.expander}   {self.hb[2]}{self.hb[3]}{Board.v}{self.x[40]}{Board.v}      {self.lb[0]}{Board.v}      {self.x[32]}{Board.v}{self.hr[0]}{self.hr[1]}{Board.v}   
{Board.v}{Board.expander}        |      {self.x[39]}{self.x[38]}{self.x[37]}{self.x[36]}{self.x[35]}{self.x[34]}{self.x[33]}{Board.v}               
{Board.v}{Board.expander}        -------{self.hb[4]}{Board.v}                                 
{Board.v}                                                                      
{Board.v}                                                       
{Board.v}                                                       
{Board.v}                                                       
{Board.v}                                                       
"""
    # Returns a string that evaluates to a block on the board
    def cell(self, content, bg, void=False):
        return_string = ""
        if void:
            return "\33[40;94m" + "   "
        if content == "-":
            return "\33[40;94m" + "---"
        if content == "<":
            return "\33[40;94m" + "<--"
        # Background to colour code
        bg_map = {"r":"\33[48;5;1m","g":"\33[48;5;2m","y":"\33[48;5;3m","b":"\33[48;5;4m","n":"\33[48;5;5m"}
        return_string += bg_map[bg]
        if content == None:
            return_string += "\33[38;5;201m" + "   "
            return return_string
        if isinstance(content,plane.Plane):
            return_string += f"{content}"
        return return_string
    def construct_board(self, num_of_cells, colour="a"):
        board = []
        if colour == "a":
            # Constructing the main board with cells of alternating colours
            for i in range(num_of_cells):
                if i%4 == 0:
                    board.append(self.cell(None,"b"))
                elif i%4 == 1:
                    board.append(self.cell(None,"y"))
                elif i%4 == 2:
                    board.append(self.cell(None,"g"))
                elif i%4 == 3:
                    board.append(self.cell(None,"r"))
        else:
            # Constructing hangars and landing strips with a single colour
            for i in range(num_of_cells):
                board.append(self.cell(None,colour))
        return board
    # Checks background of any given cell
    def bg(self, part, index):
        raw = eval(f"self.{part}")[index].split("\x1b[")[1].split(";")[2]
        bg_map = {"1m":"r", "2m":"g", "3m":"y", "4m":"b", "5m":"n"}
        return bg_map[raw]
    #         Part of board↓ (hangars, main board or landing strips)
    def change_cell(self, part, index, new_content):
        eval(f"self.{part}")[index] = self.cell(new_content, self.bg(part,index))
    # Return a plane instance from the given string (these strings are elements of the lists storing what's displayed on the board)
    def get_plane(self,string):
        if string[-3].isalpha and string[-3].isupper:
            return eval(f"Board.plane_{string[-3].lower()}")
    # Check if any given cell has a plane on it
    def is_plane(self,string):
        try:
            return string[-3].isalpha and string[-3].isupper and 80 >= ord(string[-3]) >= 65
        except:
            return False
    # Locate the plane in terms of the part of the board it's in and the index
    def locate(self, plane):
        for index, obj in enumerate(self.x):
            if plane.uid in obj:
                return "x", index
        for index, obj in enumerate(self.hg):
            if plane.uid in obj:
                return "hg", index
        for index, obj in enumerate(self.hr):
            if plane.uid in obj:
                return "hr", index
        for index, obj in enumerate(self.hb):
            if plane.uid in obj:
                return "hb", index
        for index, obj in enumerate(self.hy):
            if plane.uid in obj:
                return "hy", index
        for index, obj in enumerate(self.lg):
            if plane.uid in obj:
                return "lg", index
        for index, obj in enumerate(self.lr):
            if plane.uid in obj:
                return "lr", index
        for index, obj in enumerate(self.lb):
            if plane.uid in obj:
                return "lb", index
        for index, obj in enumerate(self.ly):
            if plane.uid in obj:
                return "ly", index
        # ↓ in case the plane has already landed and was removed from the board
        return "n", -1
    # Removes the plane from the main board and puts it back into the hangar lists
    def kick_to_hangar(self, p):
        part, index = self.locate(p)
        if part != "x": return # Only planes in the main board can be kicked back to hangar
        # Remove the old plane from the main board
        self.change_cell(part, index, None)
        for i, obj in enumerate(eval(f"self.h{p.colour}")):
            if obj == self.cell(None,p.colour) and i != 4:
                new_index = i
        # Insert the plane back into its hangar
        self.change_cell(f"h{p.colour}",new_index,p)
        # Reset total distance travelled by plane
        p.total_distance = 0
    # Automate logic and calls to change_cell() for movement of planes
    def move(self, plane, steps, prepareTakeOff=False, takeOff=False):
        part, index = self.locate(plane)
        if prepareTakeOff:
            self.change_cell(part,index,None)
            self.change_cell(part, 4, plane)
        elif takeOff:
            new_index_on_main_board = Board.colour_to_start_pt[plane.colour]
            if self.is_plane(self.x[new_index_on_main_board]):
                other_plane = self.get_plane(self.x[new_index_on_main_board])
                if other_plane.colour != plane.colour:
                    self.kick_to_hangar(other_plane)
                elif other_plane.colour == plane.colour:
                    return
            self.change_cell(part,index,None)
            self.change_cell("x", new_index_on_main_board, plane)
        else:
            # For when the plane is in the main board and needs to enter the landing strip
            if part == "x" and plane.total_distance+steps > 49:
                addition_to_plane_total_distance = Board.colour_to_landing_strip_pt[plane.colour] - index
                new_index_on_landing_strip = index + steps - Board.colour_to_landing_strip_pt[plane.colour] - 1
                while self.is_plane(eval(f"self.l{plane.colour}")[new_index_on_landing_strip]):
                    new_index_on_landing_strip += 1
                    addition_to_plane_total_distance += 1
                self.change_cell(part,index,None)
                plane.total_distance += addition_to_plane_total_distance
                self.change_cell(f"l{plane.colour}", new_index_on_landing_strip, plane)
            # For when the plane is moving within a landing strip
            elif "l" in part:
                addition_to_plane_total_distance = steps
                new_index_on_landing_strip = index + steps
                if new_index_on_landing_strip > 5:
                    self.change_cell(part,index,None)
                    plane.total_distance += addition_to_plane_total_distance
                    self.landed_planes[plane.colour] += 1
                    self.check_win()
                    return
                while self.is_plane(eval(f"self.l{plane.colour}")[new_index_on_landing_strip]):
                    addition_to_plane_total_distance += 1
                    new_index_on_landing_strip += 1
                else:
                    self.change_cell(part,index,None)
                    plane.total_distance += addition_to_plane_total_distance
                    self.change_cell(f"l{plane.colour}", new_index_on_landing_strip, plane)
            # For when a plane is moving within the main board
            else:
                new_index_on_main_board = index+steps
                addition_to_plane_total_distance = steps
                if new_index_on_main_board > 51:
                    new_index_on_main_board -= 52
                def handle_plane_at_destination(plane, new_index_on_main_board, addition_to_plane_total_distance):
                    while self.is_plane(self.x[new_index_on_main_board]):
                        other_plane = self.get_plane(self.x[new_index_on_main_board])
                        if other_plane.colour != plane.colour:
                            self.kick_to_hangar(other_plane)
                            break
                        elif other_plane.colour == plane.colour:
                            new_index_on_main_board += 1
                            addition_to_plane_total_distance += 1
                            if new_index_on_main_board > 51:
                                new_index_on_main_board -= 52
                    return new_index_on_main_board, addition_to_plane_total_distance
                new_index_on_main_board, addition_to_plane_total_distance = handle_plane_at_destination(plane, new_index_on_main_board, addition_to_plane_total_distance)
                if plane.colour == self.bg("x", new_index_on_main_board) and not new_index_on_main_board in {4,17,30,43}:
                    new_index_on_main_board += 4
                    addition_to_plane_total_distance += 4
                    if new_index_on_main_board > 51:
                        new_index_on_main_board -= 52
                    new_index_on_main_baord, addition_to_plane_total_distance = handle_plane_at_destination(plane, new_index_on_main_board, addition_to_plane_total_distance)
                elif plane.colour == self.bg("x", new_index_on_main_board) and new_index_on_main_board in {4,17,30,43}:
                    self.help_attack(plane, new_index_on_main_board)
                    new_index_on_main_board += 12
                    addition_to_plane_total_distance += 12
                    if new_index_on_main_board > 51:
                        new_index_on_main_board -= 52
                    new_index_on_main_board, addition_to_plane_total_distance = handle_plane_at_destination(plane, new_index_on_main_board, addition_to_plane_total_distance)
                self.change_cell(part,index,None)
                plane.total_distance += addition_to_plane_total_distance
                self.change_cell("x",new_index_on_main_board,plane)
                return
    def help_attack(self, plane, original_index):
        if original_index not in {4,17,30,43}: return
        start_index = original_index + 1
        if start_index+12 > 51:
            index_pairs = [[start_index+1,51],[0,(start_index+12-51-1)]]
            target_planes = []
            for pair in index_pairs:
                target_planes += [self.get_plane(string) for string in self.x[pair[0]:pair[1]] if self.is_plane(string)]
            for p in target_planes:
                if p.colour != plane.colour:
                    self.kick_to_hangar(p)
        else:
            end_index = start_index + 12
            target_planes = [self.get_plane(string) for string in self.x[start_index:end_index] if self.is_plane(string)]
            for p in target_planes:
                if p.colour != plane.colour:
                    self.kick_to_hangar(p)
    def check_win(self):
        for colour in self.landed_planes.keys():
            if self.landed_planes[colour] == 4:
                self.winner = colour
                self.endgame()
    def endgame(self):
        print(self)
        print(f"{Board.expander}                    Player {Board.player_to_emoji[self.winner]} won! 🎉")
        exit()
    def change_player(self):
        player_to_next_player = {"y":"g","g":"r","r":"b","b":"y"}
        self.current_player = player_to_next_player[self.current_player]
    def update_board(self):
        die_result = random.randint(1, 6)
        print(self)
        die_result_to_emoji = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        print(f"{Board.expander}         Current player: {Board.player_to_emoji[self.current_player]}    |      Rolled: {die_result_to_emoji[die_result]} {die_result}")
        enable_hangar_planes = die_result % 2 == 0
        colour_to_planes = {"r" : [Board.plane_a, Board.plane_b, Board.plane_c, Board.plane_d], "g": [Board.plane_e, Board.plane_f, Board.plane_g, Board.plane_h], "y": [Board.plane_i, Board.plane_j, Board.plane_k, Board.plane_l], "b": [Board.plane_m, Board.plane_n, Board.plane_o, Board.plane_p]}
        plane_uid = []
        for plane in colour_to_planes[self.current_player]:
            part, index = self.locate(plane)
            if "n" in part: continue
            if "h" in part:
                if index == 4:
                    if not self.is_plane(self.x[Board.colour_to_start_pt[self.current_player]]):
                        plane_uid.append(plane.uid.upper())
                    else:
                        other_plane = self.get_plane(self.x[Board.colour_to_start_pt[self.current_player]])
                        if other_plane.colour != plane.colour:
                            plane_uid.append(plane.uid.upper())
                        else: continue
                else:
                    if enable_hangar_planes and not self.is_plane(eval(f"self.h{plane.colour}")[4]):
                        plane_uid.append(plane.uid.upper())
                    else: continue
            else:
                plane_uid.append(plane.uid.upper())
        if plane_uid != []:
            def ask(plane_uid):
                prompt = f"\n{Board.expander}         Choose a plane to move:"
                for uid in plane_uid:
                    prompt += f"  {uid}"
                prompt += "    "
                uid_to_move = input(prompt)
                try:
                    if not uid_to_move in plane_uid:
                        uid_to_move = ask(plane_uid)
                        return uid_to_move
                except:
                    uid_to_move = ask(plane_uid)
                    return uid_to_move
                return uid_to_move
            uid_to_move = ask(plane_uid) # REMEMBER TO UNCOMMENT THIS
            plane = eval(f"Board.plane_{uid_to_move.lower()}")
            part, index = self.locate(plane)
            if "h" in part and 0 <= index < 4:
                self.move(plane,0,prepareTakeOff=True)
            elif "h" in part and index==4:
                # When taking off
                self.move(plane,0,takeOff=True)
            else:
                self.move(plane, die_result)
        else:
            prompt = f"\n{Board.expander}      No planes available. Press ENTER to continue."
            input(prompt)

        self.change_player()