import os


class Parser:
    def __init__(self, code=None, loaded=None, path="modules/"):
        self.code = code
        self.loaded = loaded
        self.path = path

    def loadModules(self):
        """Modules loader for Py3PHP
        :return loaded_modules:
        """
        loaded_modules = {
            "vars": [],
            "external": [],
            "builtins": []
        }
        for dir in os.listdir(self.path):
            for file in os.listdir(self.path + dir):
                if dir == "builtins":
                    file = open(self.path + dir + "/" + file, "r")
                    for line in file.read().split("\n"):
                        loaded_modules["builtins"].append(line)
                elif dir == "external":
                    file = open(self.path + dir + "/" + file, "r")
                    for line in file.read().split("\n"):
                        loaded_modules["external"].append(line)
                elif dir == "vars":
                    file = open(self.path + dir + "/" + file, "r")
                    for line in file.read().split("\n"):
                        loaded_modules["vars"].append(line)
        return loaded_modules

    def splitter(self):
        splitted_modules = {
            "builtins": [],
            "external": [],
            "vars": []
        }
        for mod in self.loaded:
            if len(mod) > 0:
                temp_array = {
                    "python_function": "",
                    "php_function": "",
                    "args": {}
                }
                if mod == "builtins":
                    for m in self.loaded[mod]:
                        split = m.split(":")
                        args_split = split[2].replace("(", "").replace(")", "").split(",")
                        temp_array["python_function"] = split[0]
                        temp_array["php_function"] = split[1]
                        for arg in args_split:
                            temp_array["args"].setdefault(arg.split("|")[0], arg.split("|")[1])
                        splitted_modules["builtins"].append(temp_array)
                elif mod == "external":
                    for m in self.loaded[mod]:
                        split = m.split(":")
                        args_split = split[2].replace("(", "").replace(")", "").split(",")
                        temp_array["python_function"] = split[0]
                        temp_array["php_function"] = split[1]
                        for arg in args_split:
                            temp_array["args"].setdefault(arg.split("|")[0], arg.split("|")[1])
                        splitted_modules["external"].append(temp_array)
                elif mod == "vars":
                    for m in self.loaded[mod]:
                        split = m.split(":")
                        args_split = split[2].replace("(", "").replace(")", "").split(",")
                        temp_array["python_function"] = split[0]
                        temp_array["php_function"] = split[1]
                        for arg in args_split:
                            temp_array["args"].setdefault(arg.split("|")[0], arg.split("|")[1])
                        splitted_modules["vars"].append(temp_array)
        return splitted_modules
    def replacer(self, content):

        """Replacer for Py3PHP
        :param content: str
        """
        # TODO: make a basic replacer

        # Das geladene wird im Format von ./modules/builtins/test.txt aussehen d.h. das replaces muss dann daran
        # php function in py umwandeln und dann print 200IQ
        argsSplitter = ((content.split("(")[1]).split(")")[0]).split(", ")
        args = []

        for arg in argsSplitter:
            args.insert(0, arg.strip())

    def errorManger(self, error_type, error_specific):

        """Error manger for Py3PHP
    
        :param error_type: str
        :param error_specific: str
        :return:
        """""
        error_types = [
            "MISSING_SOMETHING",
            "WRONG_TYPE",
            "OUT_OF_RANGE",
            "INCORRECT"
            # Muss off
            # Kannst einfach bei der liste hier helfen kk suche kurz errors nullpointer geht auch nh oder das exception
        ]



