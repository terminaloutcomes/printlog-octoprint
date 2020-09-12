""" octoprint printlog plugin """

import json

from loguru import logger
import octoprint.plugin
from octoprint.printer.profile import PrinterProfileManager
EVENTS_I_WANT = ['PrintDone', 'PrintCancelled']
PLUGIN_NAME = "Printlog"

class PrintlogPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.EventHandlerPlugin):
    def on_after_startup(self):
        self._logger.info("Starting up Printlog")
        logger.info("Starting up Printlog")
        printer_profiles = octoprint.printer.profile.PrinterProfileManager()
        #logger.debug(json.dumps(printer_profiles))
        print(printer_profiles)

    def get_settings_defaults(self):
        return dict(username="", api_key="")
    def get_assets(self):
        return dict(
            #js=["js/helloworld.js"],
            #css=["css/helloworld.css"]
        )
    def on_event(self, event, payload):
        """ handles events """
        if event in EVENTS_I_WANT:
            logger.debug(f"EVENT TRIGGERED: {json.dumps(event)}")
            logger.debug(f"EVENT PAYLOAD: {json.dumps(payload)}")
    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            PrintlogPlugin=dict(
                displayName=PLUGIN_NAME,
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="terminaloutcomes",
                repo="printlog-octoprint",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/terminaloutcomes/printlog-octoprint/archive/{target_version}.zip"
            )
        )

# PrintDone
# A print completed successfully.
# Payload:
# name: the file’s name
# path: the file’s path within its storage location
# origin: the origin storage location of the file, either local or sdcard
# size: the file’s size in bytes (if available)
# owner: the user who started the print job (if available)
# time: the time needed for the print, in seconds (float)


# PrintCancelled
# The print has been cancelled.
# Payload:
# name: the file’s name
# path: the file’s path within its storage location
# origin: the origin storage location of the file, either local or sdcard
# size: the file’s size in bytes (if available)
# owner: the user who started the print job (if available)
# time: the elapsed time of the print when it was cancelled, in seconds (float)
# user: the user who cancelled the print job (if available)
# position: the print head position at the time of cancelling (if available, not available if recording of the position on cancel is disabled)
# position.x: x coordinate, as reported back from the firmware through M114
# position.y: y coordinate, as reported back from the firmware through M114
# position.z: z coordinate, as reported back from the firmware through M114
# position.e: e coordinate (of currently selected extruder), as reported back from the firmware through M114
# position.t: last tool selected through OctoPrint (note that if you did change the printer’s selected tool outside of OctoPrint, e.g. through the printer controller, or if you are printing from SD, this will NOT be accurate)
# position.f: last feedrate for move commands sent through OctoPrint (note that if you modified the feedrate outside of OctoPrint, e.g. through the printer controller, or if you are printing from SD, this will NOT be accurate)

__plugin_pythoncompat__ = '>=3.7'
__plugin_implementation__ = PrintlogPlugin()
