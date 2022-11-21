from enum import Enum


class RuleSetEnum(Enum):
    CORE = 0
    RECOMMENDED = 1
    FLUTTER = 2


class MaturityLevelEnum(Enum):
    STABLE = 0
    EXPERIMENTAL = 1
    DEPRECATED = 2
