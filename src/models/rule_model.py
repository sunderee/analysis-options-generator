from dataclasses import dataclass

from src.models.enums import RuleSetEnum, MaturityLevelEnum


@dataclass
class RuleModel:
    id: str
    description: str
    has_quick_fix: bool
    rule_sets: list[RuleSetEnum]
    maturity: MaturityLevelEnum

    def to_object(self) -> dict[str, str | bool | list[RuleSetEnum] | MaturityLevelEnum | None]:
        return {
            'id': self.id,
            'description': self.description,
            'has_quick_fix': self.has_quick_fix,
            'rule_sets': [item.name for item in self.rule_sets],
            'maturity_level': self.maturity.value
        }
