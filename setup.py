from src.parser import Parser

if __name__ == '__main__':
    rules = Parser.find_all_rules()
    Parser.pack_rules_to_json(rules)
