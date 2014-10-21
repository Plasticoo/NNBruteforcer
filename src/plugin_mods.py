from yapsy.PluginManager import PluginManager

class UserModules():

    usr_modules = {}

    def get_modules(self):
        manager = PluginManager()
        manager.setPluginPlaces(["plugins"])
        manager.collectPlugins()

        for plugin in manager.getAllPlugins():
            manager.activatePluginByName(plugin.name)
            self.usr_modules[plugin.name] = plugin.plugin_object

    def __init__(self):
        self.get_modules()