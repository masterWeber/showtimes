from unittest import TestCase

from src.domain.schedule.schedule_rule.date_rule import DateRule
from src.domain.schedule.schedule_rule.date_rule_type import DateRuleType


class TestDateRule(TestCase):

    def test_from_(self):
        rule = DateRule.from_('*')

        self.assertIsInstance(rule, DateRule)
        self.assertEqual(rule.value, '*')
        self.assertEqual(rule.type, DateRuleType.EVERYONE)

        rule = DateRule.from_('30')

        self.assertIsInstance(rule, DateRule)
        self.assertEqual(rule.value, '30')
        self.assertEqual(rule.type, DateRuleType.NUMBER)

        rule = DateRule.from_('30-31')

        self.assertIsInstance(rule, DateRule)
        self.assertEqual(rule.value, '30-31')
        self.assertEqual(rule.type, DateRuleType.RANGE)

        self.assertRaises(ValueError, DateRule.from_, '32')
        self.assertRaises(ValueError, DateRule.from_, '0')
        self.assertRaises(ValueError, DateRule.from_, '-1')
        self.assertRaises(ValueError, DateRule.from_, 'INVALID_TYPE_VALUE')
