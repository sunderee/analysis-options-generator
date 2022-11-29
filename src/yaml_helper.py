from typing import TextIO

from src.models.enums import RuleSetEnum, MaturityLevelEnum
from src.models.rule_model import RuleModel

lints_core_import = 'include: package:lints/core.yaml'
lints_recommended_import = 'include: package:lints/recommended.yaml'
flutter_lints_import = 'include: package:flutter_lints/flutter.yaml'

analyzer_section = '''
analyzer:
  exclude: ["build/**"]
  language:
    strict-casts: true
    strict-inference: true
    strict-raw-types: true
'''


class YAMLHelper:
    @staticmethod
    def generate_analysis_options(path: str, rules: list[RuleModel], rule_set: RuleSetEnum, soft_mode: bool) -> None:
        with open(f'{path}/analysis_options.yaml', 'w') as file:
            match rule_set:
                case RuleSetEnum.CORE:
                    file.write(lints_core_import)
                case RuleSetEnum.RECOMMENDED:
                    file.write(lints_recommended_import)
                case RuleSetEnum.FLUTTER:
                    file.write(flutter_lints_import)
                case _:
                    file.write(lints_core_import)

            file.write('\n')
            file.write(analyzer_section)

            YAMLHelper.__write_rules_to_file(rules=rules, rule_set=rule_set, soft_mode=soft_mode, file=file)

    @staticmethod
    def __write_rules_to_file(rules: list[RuleModel], rule_set: RuleSetEnum, soft_mode: bool, file: TextIO) -> None:
        applicable_rules = [rule.id for rule in rules
                            if YAMLHelper.__is_rule_legible_for_display(maturity_level=rule.maturity,
                                                                        selected_rule_set=rule_set,
                                                                        available_rule_sets=rule.rule_sets)]
        file.write('  errors:\n')
        for applicable_rule in applicable_rules:
            file.write(f'    {applicable_rule}: {"warning" if soft_mode else "error"}\n')

        file.write('\nlinter:\n  rules:\n')
        for rule in rules:
            file.write(f'    # {rule.description}\n')
            if rule.maturity == MaturityLevelEnum.EXPERIMENTAL:
                file.write(f'    # This rule is experimental. Use at your own risk.\n')
            if rule.maturity == MaturityLevelEnum.DEPRECATED:
                file.write(f'    # This rule is deprecated. Do not use it.\n')

            if YAMLHelper.__is_rule_legible_for_display(maturity_level=rule.maturity,
                                                        selected_rule_set=rule_set,
                                                        available_rule_sets=rule.rule_sets):
                file.write(f'    - {rule.id}\n\n')
            else:
                file.write(f'    # - {rule.id}\n\n')

    @staticmethod
    def __is_rule_legible_for_display(maturity_level: MaturityLevelEnum, selected_rule_set: RuleSetEnum,
                                      available_rule_sets: list[RuleSetEnum]) -> bool:
        if maturity_level != MaturityLevelEnum.STABLE:
            return False

        return selected_rule_set in available_rule_sets
