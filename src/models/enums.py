from enum import Enum


class RuleSetEnum(Enum):
    CORE = 0
    RECOMMENDED = 1
    FLUTTER = 2


class MaturityLevelEnum(Enum):
    STABLE = 0
    EXPERIMENTAL = 1
    DEPRECATED = 2


def rule_set_from_list(string_list: list[str]) -> list[RuleSetEnum]:
    rule_sets: list[RuleSetEnum] = []
    if 'CORE' in string_list:
        rule_sets.append(RuleSetEnum.CORE)
    if 'RECOMMENDED' in string_list:
        rule_sets.append(RuleSetEnum.RECOMMENDED)
    if 'FLUTTER' in string_list:
        rule_sets.append(RuleSetEnum.FLUTTER)

    return rule_sets


def maturity_level_from_value(value: int) -> MaturityLevelEnum | None:
    match value:
        case 0:
            return MaturityLevelEnum.STABLE
        case 1:
            return MaturityLevelEnum.EXPERIMENTAL
        case 2:
            return MaturityLevelEnum.DEPRECATED
        case _:
            return None
