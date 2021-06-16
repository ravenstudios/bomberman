class Make_map:
    def __init__(self):
        pass

    def get_list(self, file_path):
        map_list = ""
        # reads the file and splits every new line into a list
        with open(file_path) as file:
            map_list = file.read().split("\n")
        # filter out all "#" and empty strings
        map_list = list(filter(self.is_comment, map_list))

        #finally split by csv
        for m in range(len(map_list)):
            map_list[m] = map_list[m].split(",")

        return map_list

    # filters out comments and blank strings
    def is_comment(self, string):
        if not string:
            return False
        if string[0] == "#":
            return False
        return True


m = Make_map()
print(m.get_list("map.map"))
