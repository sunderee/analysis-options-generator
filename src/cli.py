from argparse import ArgumentParser

from src.models.enums import RuleSetEnum


class CLI:
    @staticmethod
    def parse_arguments() -> tuple[RuleSetEnum, bool]:
        parser = ArgumentParser(description='Tool for automatically populating analysis_options.yaml file with all '
                                            'the available linting rules described by the official documentation.')

        parser.add_argument('-r', '--rule-set',
                            dest='rule_set',
                            choices=['core', 'recommended', 'flutter'],
                            help='Sets the rule set that analysis_options.yaml will contain. Defaults to core.')
        parser.add_argument('-s', '--soft-mode',
                            dest='soft_mode',
                            action='store_true',
                            default=False,
                            help='Sets the severity of enabled linting rules to "warning"')
        arguments = parser.parse_args()

        match str(arguments.rule_set):
            case 'core':
                return RuleSetEnum.CORE, bool(arguments.soft_mode)
            case 'recommended':
                return RuleSetEnum.RECOMMENDED, bool(arguments.soft_mode)
            case 'flutter':
                return RuleSetEnum.FLUTTER, bool(arguments.soft_mode)
            case _:
                return RuleSetEnum.CORE, bool(arguments.soft_mode)
