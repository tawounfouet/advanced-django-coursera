from unittest import mock

from django.test import TestCase


class Question5TestCase(TestCase):
    @mock.patch("assessment.views.logging")
    def test_logging_calls(self, mock_logging_module):
        mock_logger = mock.MagicMock()
        mock_logging_module.getLogger.return_value = mock_logger
        request = mock.MagicMock()

        import assessment.views

        self.assertIsNotNone(assessment.views.logger)

        assessment.views.logger = mock_logger
        assessment.views.question5(request)

        mock_logging_module.getLogger.asert_called_with("assessment.views")

        mock_logger.debug.assert_called_with("A Debug Message")
        mock_logger.warning.assert_called_with("A Warning Message")
        mock_logger.critical.assert_called_with("A Critical Message")
