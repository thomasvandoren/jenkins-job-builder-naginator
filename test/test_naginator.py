# -*- coding: utf-8 -*-

import os.path
from testscenarios.testcase import TestWithScenarios
from testtools import TestCase
from jenkins_jobs.modules import publishers
from base import get_scenarios, BaseTestCase  # copied from jenkins-job-builder


class TestCaseModulePublishersNaginator(TestWithScenarios, TestCase,
                                        BaseTestCase):
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    scenarios = get_scenarios(fixtures_path)
    klass = publishers.Publishers
