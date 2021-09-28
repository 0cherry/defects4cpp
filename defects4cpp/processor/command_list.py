from collections.abc import MutableMapping
from typing import Dict

from processor.core.command import Command, RegisterCommand


class CommandList(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store: Dict[str, Command] = {
            command: command_type()
            for command, command_type in RegisterCommand.commands.items()
        }
        # self.update(dict(*args, **kwargs))

    def __getitem__(self, key: str):
        return self.store[self._keytransform(key)]

    def __setitem__(self, key: str, value):
        # self.store[self._keytransform(key)] = value
        raise RuntimeError("set operator is not allowed")

    def __delitem__(self, key: str):
        # del self.store[self._keytransform(key)]
        raise RuntimeError("del operator is not allowed")

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def _keytransform(self, key: str):
        return key