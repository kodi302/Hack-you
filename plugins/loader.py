import importlib
import os

PLUGIN_DIR = "plugins"


class PluginLoader:

    def __init__(self):
        self.plugins = []

    def load(self):

        if not os.path.exists(PLUGIN_DIR):
            return []

        for file in os.listdir(PLUGIN_DIR):

            if file.endswith(".py"):

                if file.startswith("__"):
                    continue

                name = file[:-3]

                module = importlib.import_module(
                    f"plugins.{name}"
                )

                self.plugins.append(module)

        return self.plugins