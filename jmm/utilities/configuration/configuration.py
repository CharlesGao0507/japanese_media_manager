from typing import List
from typing import Optional
from typing import Type
from pydoc import locate
from pydantic import BaseModel
from pydantic import validator
from pydantic import Field

from jmm.crawlers import Base
from jmm.utilities.crawler_group import Router
from jmm.utilities.crawler_group import Rule
from jmm.utilities.crawler_group import CrawlerGroup

class CrawlerConfiguration(BaseModel):
    name: str
    clazz: Type[Base] = Field(alias='class')
    arguments: Optional[dict] = Field(alias='with')

    @validator('clazz', always=True, pre=True)
    def _clazz(cls, value: str) -> Type[Base]:
        clazz = locate(value)
        if not clazz:
            raise ValueError(f'cannot get class from {repr(value)}')
        if not isinstance(clazz, type):
            raise ValueError(f'class {repr(value)} must be a type')
        if clazz is Base:
            raise ValueError(f'class cannot be {Base.__module__}.{Base.__name__}')
        class_name = clazz.__name__
        if not issubclass(clazz, Base):
            raise ValueError(f'class {repr(class_name)} must be a subclass of class {Base.__module__}.{Base.__name__}')
        return clazz

class RoutingRuleConfiguration(BaseModel):
    pattern: str
    crawlers: List[str]

    @validator('crawlers')
    def _crawlers(cls, value: List[str]) -> List[str]:
        if not value:
            raise ValueError('crawlers is empty')
        return value

class Configuration(BaseModel):
    crawlers: List[CrawlerConfiguration]
    routing_rules: List[RoutingRuleConfiguration]

    @validator('crawlers')
    def _crawlers(cls, value: List[CrawlerConfiguration]) -> List[CrawlerConfiguration]:
        if not value:
            raise ValueError('crawlers is empty')
        return value

    @validator('routing_rules')
    def _routing_rules(cls, value: List[RoutingRuleConfiguration]) -> List[RoutingRuleConfiguration]:
        if not value:
            raise ValueError('routing_rules is empty')
        return value

    @property
    def router(self) -> Router:
        crawler_map = {}
        for crawler_configuration in self.crawlers:
            crawler_map[crawler_configuration.name] = crawler_configuration.clazz(**(crawler_configuration.arguments or {}))

        rules = []
        for routing_rule in self.routing_rules:
            rules.append(
                Rule(
                    pattern=routing_rule.pattern,
                    crawler_group=CrawlerGroup(
                        crawlers=[crawler_map[crawler_name] for crawler_name in routing_rule.crawlers]
                    )
                )
            )
        return Router(rules)
