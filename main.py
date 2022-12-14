from src.cli import CLI
from src.scraper import Scraper
from src.yaml_helper import YAMLHelper


def main():
    rule_set, path, for_softies = CLI.parse_arguments()
    YAMLHelper.generate_analysis_options(path=path,
                                         rules=Scraper.find_all_rules(),
                                         rule_set=rule_set,
                                         soft_mode=for_softies)


if __name__ == '__main__':
    main()
