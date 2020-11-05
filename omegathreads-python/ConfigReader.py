import os
from parglare import Grammar, Parser

ConfigGrammerFile = 'ConfigFileGrammer.pg'
this_folder = os.path.dirname(__file__)

class ConfigReader:
    def __init__(self, filepath, debug=False):
        self.grammar_file = os.path.join(this_folder, 'ConfigFileGrammer.pg')
        self.grammer_obj = Grammar.from_file(self.grammar_file, debug=debug)
        self.parser = Parser(self.grammer_obj, build_tree=True, debug=debug)
        self.config_file = open(filepath, 'r')
        self.parse_result = self.parser.parse(self.config_file.read())
        self.IdValueList = []
        self.collect_list(self.parse_result, "")

    def collect_list(self, start_node, current_path):
        
        if isinstance(start_node, str):
            str_sym = start_node
        else:
            str_sym = str(start_node.symbol)

        if str_sym == "Comment":
            pass
        elif str_sym == "Object":
            obj_id = ""
            for sub_nodes in start_node:
                if str(sub_nodes.symbol) == "ID":
                    obj_id = sub_nodes.value

            for child in start_node:
                self.collect_list(child, current_path + obj_id + ".")        
        elif str_sym == "IdValuePair":
            Id = ""
            Val = ""
            for sub_nodes in start_node:
                if str(sub_nodes.symbol) == "ID":
                    Id = sub_nodes.value
                elif str(sub_nodes.symbol) == "VALUE":
                    Val = sub_nodes.value            

            self.IdValueList.append([current_path + Id,Val])
        else:
            for child in start_node:
                self.collect_list(child, current_path)
        

    def print_list(self):
        for pair in self.IdValueList:
            Id = pair[0]
            Val = pair[1]
            print(Id + " = " + Val)

    def print_tree(self):
        print(self.parse_result.tree_str())

    def get_value_string(self, cfg_id):
        for pair in self.IdValueList:
            if pair[0] == cfg_id:
                return pair[1][1:len(pair[1])-1]
        return ""
