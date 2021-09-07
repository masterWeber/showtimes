import random
from datetime import date
from unittest import TestCase
from unittest.mock import patch

from src.domain.schedule.schedule_rule.date_rule import DateRule
from src.domain.schedule.schedule_rule.schedule_rule import ScheduleRule
from src.domain.common.weekday import Weekday
from src.domain.schedule.schedule_rule.schedule_rule_id import ScheduleRuleId


class TestScheduleRule(TestCase):

    @patch('src.domain.time_interval.time_interval.TimeInterval')
    @patch('src.domain.schedule.schedule_rule.schedule_rule_id_generator.ScheduleRuleIdGenerator')
    @patch('src.domain.schedule.schedule_rule.date_rule.DateRule')
    def test_create(
            self,
            time_interval_mock,
            schedule_rule_id_generator_mock,
            date_rule_mock,
    ) -> None:
        time_interval = time_interval_mock()
        schedule_rule_id_generator = schedule_rule_id_generator_mock()
        date_rule = date_rule_mock()

        schedule_rule = ScheduleRule.create(
            schedule_rule_id_generator,
            time_interval,
            date_rule,
            Weekday.MONDAY
        )

        self.assertIsInstance(
            schedule_rule,
            ScheduleRule
        )

    @patch('src.domain.time_interval.time_interval.TimeInterval')
    def test_match(self, time_interval_mock) -> None:
        time_interval = time_interval_mock()
        date_rule = DateRule.from_('*')

        schedule_rule = ScheduleRule(
            ScheduleRuleId(random.randint(1, 99)),
            time_interval,
            date_rule,
            Weekday.MONDAY
        )

        self.assertFalse(
            schedule_rule.match(date.fromisoformat('2021-09-07'))
        )

        schedule_rule.date = DateRule.from_('1')
        schedule_rule.weekday = Weekday.WEDNESDAY
        self.assertTrue(
            schedule_rule.match(date.fromisoformat('2021-09-01'))
        )

        schedule_rule.weekday = Weekday.WEDNESDAY
        self.assertTrue(
            schedule_rule.match(date.fromisoformat('2021-09-01'))
        )

        schedule_rule.date = DateRule.from_('1-3')
        schedule_rule.weekday = None
        self.assertTrue(
            schedule_rule.match(date.fromisoformat('2021-09-02'))
        )
