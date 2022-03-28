from enum import Enum
from django.utils.translation import gettext_lazy as _


class BaseEnum(str, Enum):
    def __new__(cls, value, label=None):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.label = label or value
        return obj

    @classmethod
    def choices(cls):
        return [(key.label, key.name) for key in cls]

    def to_tuple(self):
        return (self.value, self.name)


class FundType(BaseEnum):
    FUND_TYPE_1 = ('FUND_TYPE_1', _('Fund Type 1'))
    FUND_TYPE_2 = ('FUND_TYPE_2', _('Fund Type 2'))
    FUND_TYPE_3 = ('FUND_TYPE_3', _('Fund Type 3'))


class FundClass(BaseEnum):
    FUND_CLASS_1 = ('FUND_CLASS_1', _('Fund Class 1'))
    FUND_CLASS_2 = ('FUND_CLASS_2', _('Fund Class 2'))
    FUND_CLASS_3 = ('FUND_CLASS_3', _('Fund Class 3'))


class FundSubclass(BaseEnum):
    FUND_SUBCLASS_1 = ('FUND_SUBCLASS_1', _('Fund Subclass 1'))
    FUND_SUBCLASS_2 = ('FUND_SUBCLASS_2', _('Fund Subclass 2'))
    FUND_SUBCLASS_3 = ('FUND_SUBCLASS_3', _('Fund Subclass 3'))
