import octoprint.plugin

class PrintlogPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("Starting up Printlog")

    def get_settings_defaults(self):
        return dict(username="", api_key="")
__plugin_pythoncompat__ = '>=3.7'
__plugin_implementation__ = PrintlogPlugin()
