import urllib.request
from json import dumps
from os import getcwd

from bs4 import BeautifulSoup, Tag

from src.models.enums import RuleSetEnum, MaturityLevelEnum
from src.models.rule_model import RuleModel


class Parser:
    @staticmethod
    def find_all_rules() -> list[RuleModel]:
        html: str = Parser.__get_documentation_html()

        soup = BeautifulSoup(html, 'html.parser')
        rule_models: list[RuleModel] = []
        tags: list[Tag] = [element for element
                           in soup.find('main').find('article').find('div').children
                           if isinstance(element, Tag)]

        for index, tag in enumerate(tags):
            if tag.name == 'h3':
                rule_id: str = tag.text.strip()
                description: str = tags[index + 1].text.strip()

                try:
                    is_still_paragraph = True
                    count = 2
                    paragraphs: list[str] = []
                    while is_still_paragraph:
                        if tags[index + count].name != 'h3':
                            if tags[index + count].name == 'p':
                                paragraphs.append(tags[index + count].text)
                            count += 1
                        else:
                            is_still_paragraph = False

                    has_quick_fix = False
                    rule_set: RuleSetEnum | None = None
                    maturity_level: MaturityLevelEnum = MaturityLevelEnum.STABLE

                    for paragraph in paragraphs:
                        if paragraph.__contains__('This rule has a quick fix available'):
                            has_quick_fix = True
                        if paragraph.__contains__('Rule sets:'):
                            if paragraph.__contains__('flutter'):
                                rule_set = RuleSetEnum.FLUTTER
                            elif paragraph.__contains__('recommended'):
                                rule_set = RuleSetEnum.RECOMMENDED
                            else:
                                rule_set = RuleSetEnum.CORE
                        if paragraph.__contains__('DEPRECATED:') \
                                or paragraph.__contains__('This rule is currently deprecated'):
                            maturity_level = MaturityLevelEnum.DEPRECATED
                        if paragraph.__contains__('This rule is currently experimental'):
                            maturity_level = MaturityLevelEnum.EXPERIMENTAL

                    rule_models.append(RuleModel(
                        id=rule_id,
                        description=description,
                        has_quick_fix=has_quick_fix,
                        rule_set=rule_set,
                        maturity=maturity_level))
                except IndexError:
                    rule_models.append(RuleModel(
                        id=rule_id,
                        description=description,
                        has_quick_fix=False,
                        rule_set=None,
                        maturity=MaturityLevelEnum.STABLE
                    ))

        return rule_models

    @staticmethod
    def pack_rules_to_json(rules: list[RuleModel]):
        with open(f'{getcwd()}/rules.json', 'w') as file:
            file.write(dumps([rule.to_object() for rule in rules]))

    @staticmethod
    def __get_documentation_html() -> str:
        with urllib.request.urlopen('https://dart.dev/tools/linter-rules') as request:
            body_bytes: bytes = request.read()
            return body_bytes.decode('utf8')
