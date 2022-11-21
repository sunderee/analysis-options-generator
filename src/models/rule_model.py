from dataclasses import dataclass

from src.models.enums import RuleSetEnum, MaturityLevelEnum


@dataclass
class RuleModel:
    id: str
    description: str
    has_quick_fix: bool
    rule_set: RuleSetEnum | None
    maturity: MaturityLevelEnum

    def to_object(self) -> dict[str, str | bool | RuleSetEnum | MaturityLevelEnum | None]:
        return {
            'id': self.id,
            'description': self.description,
            'has_quick_fix': self.has_quick_fix,
            'rule_set': self.rule_set.value if self.rule_set is not None else None,
            'maturity_level': self.maturity.value
        }
