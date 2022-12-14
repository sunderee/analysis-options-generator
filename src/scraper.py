import urllib.request

from bs4 import BeautifulSoup, Tag

from src.models.enums import RuleSetEnum, MaturityLevelEnum
from src.models.rule_model import RuleModel


class Scraper:
    @staticmethod
    def find_all_rules() -> list[RuleModel]:
        html: str = Scraper.__get_documentation_html()

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
                    rule_sets: list[RuleSetEnum] = []
                    maturity_level: MaturityLevelEnum = MaturityLevelEnum.STABLE

                    for paragraph in paragraphs:
                        if paragraph.__contains__('This rule has a quick fix available'):
                            has_quick_fix = True

                        if paragraph.__contains__('Rule sets:'):
                            paragraph = paragraph.strip().replace('\n', ' ')
                            if paragraph.__contains__('flutter'):
                                rule_sets.append(RuleSetEnum.FLUTTER)
                            if paragraph.__contains__('recommended'):
                                rule_sets.append(RuleSetEnum.RECOMMENDED)
                            if paragraph.__contains__('core'):
                                rule_sets.append(RuleSetEnum.CORE)
                        if paragraph.__contains__('DEPRECATED:') \
                                or paragraph.__contains__('This rule is currently deprecated'):
                            maturity_level = MaturityLevelEnum.DEPRECATED
                        if paragraph.__contains__('This rule is currently experimental'):
                            maturity_level = MaturityLevelEnum.EXPERIMENTAL

                    rule_models.append(RuleModel(
                        id=rule_id,
                        description=description,
                        has_quick_fix=has_quick_fix,
                        rule_sets=rule_sets,
                        maturity=maturity_level))
                except IndexError:
                    rule_models.append(RuleModel(
                        id=rule_id,
                        description=description,
                        has_quick_fix=False,
                        rule_sets=[],
                        maturity=MaturityLevelEnum.STABLE
                    ))

        return rule_models

    @staticmethod
    def __get_documentation_html() -> str:
        with urllib.request.urlopen('https://dart.dev/tools/linter-rules') as request:
            body_bytes: bytes = request.read()
            return body_bytes.decode('utf8')
