import os


class Parser:
    def __init__(self, code, modules, path="modules/"):
        self.code = code
        self.modules = modules
        self.path = path

    def loadModules(self):
        """Modules loader for Py3PHP
        :return loaded_modules:
        """
        loaded_modules = {
            "vars": [],
            "functions": [],
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



