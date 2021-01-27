import os


class Parser:
    def __init__(self, code, modules):
        self.code = code
        self.modules = modules

    def loadModules(self):
        """Modules loader for Py3PHP
        :return loaded_modules:
        """
        loaded_modules = {
            "vars": [],
            "functions": [],
            "builtins": []
        }
        for m in self.modules:
            if len(m):
                for dir in os.listdir(m):
                    for file in os.listdir(dir):
                        if dir == "builtins":
                            file = open(file, "r")
                            for line in file.readline():
                                loaded_modules["builtins"].append(line)
                        elif dir == "external":
                            file = open(file, "r")
                            for line in file.readline():
                                loaded_modules["external"].append(line)
                        elif dir == "vars":
                            file = open(file, "r")
                            for line in file.readline():
                                loaded_modules["vars"].append(line)
            return loaded_modules

    def replacer(self, content):
        """Replacer for Py3PHP
        :param content: str
        """
        #TODO: make a basic replacer

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







