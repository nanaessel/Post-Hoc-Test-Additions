import unittest
from unittest.mock import MagicMock
from typing import Type
from barkylib.domain import commands, events
from barkylib.services import messagebus, unit_of_work
from barkylib.services.messagebus import MessageBus

class TestMessageBus(unittest.TestCase):
    def setUp(self):
        self.uow = MagicMock(spec=unit_of_work.AbstractUnitOfWork)
        self.event_handlers = {
            events.Event: [MagicMock(), MagicMock()],
            events.Event: [MagicMock()]
        }
        self.command_handlers = {
            commands.Command: MagicMock(),
            commands.Command: MagicMock()
        }
        self.message_bus = MessageBus(
            uow=self.uow,
            event_handlers=self.event_handlers,
            command_handlers=self.command_handlers
        )

    def test_handle_command(self):
        command = commands.Command()
        self.message_bus.handle(command)
        self.command_handlers[type(command)].assert_called_once_with(command)
        self.uow.collect_new_events.assert_called_once()

    def test_handle_event(self):
        event = events.Event()
        self.message_bus.handle(event)
        for handler in self.event_handlers[type(event)]:
            handler.assert_called_once_with(event)
        self.uow.collect_new_events.assert_called_once()

    def test_handle_invalid_message(self):
        message = "not a valid message"
        with self.assertRaises(Exception):
            self.message_bus.handle(message)

if __name__ == '__main__':
    unittest.main()
