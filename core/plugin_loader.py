import importlib
import os

PLUGIN_DIR = "plugins"


def load_plugins():

    plugins = []

    if not os.path.exists(PLUGIN_DIR):
        return plugins

    for file in os.listdir(PLUGIN_DIR):

        if file.endswith(".py") and file != "__init__.py":

            name = file[:-3]

            module = importlib.import_module(f"plugins.{name}")

            plugins.append(module)

    return plugins
