from src.cli import CLI


def main():
    rule_set, is_for_weaklings = CLI.parse_arguments()
    print(f'Selected rule set: {rule_set}. Used by a weakling: {is_for_weaklings}')


if __name__ == '__main__':
    main()
