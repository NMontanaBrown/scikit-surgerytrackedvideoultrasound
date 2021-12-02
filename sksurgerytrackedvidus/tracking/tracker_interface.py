# coding=utf-8

"""
Module with class to grab, manipulate and/or save
output files from the tracker.
"""

import os
import time
import numpy as np
import sksurgerynditracker as sksndi

class TrackingManager():
    """
    Class that handles tracking devices.
    """
    def __init__(self,
                 config:dict,
                 port_map:dict) -> None:
        """
        Instantiate a tracker instance using a config dictionary.
        Map the
        :param config: dict containing NDITracker config
            {tracker type: str, one of ["vega", "polaris", "aurora", "dummy"]
            ip address: str,
            port: int (Code is on the back of marker device(s).),
            romfiles:  List[str] eg: ["/path/to/rom_files/rom_1_id.rom", "/path/to/rom_files/rom_2_id.rom"]
            serial port:
            ports to probe: }
        See https://github.com/UCL/scikit-surgerynditracker for more info
        on configuring NDITracker object.
        :param port_map: dict mapping romfile order to object being tracked
            eg. :
            {0: "Ultrasound",
             1: "Video"}
            or whatever other objects you are referring to.
        """
        self.instantiate_tracker(config)
        self.port_map = port_map

    def instantiate_tracker(self, config:dict) -> None:
        """
        Instantiate a NDITracker instance based on a config.
        Sets tracking to false initially, as there may be a time gap between
        start of tracking and stop tracking.
        """
        self.tracker = sksndi.nditracker.NDITracker(config)
        self.tracking = False

    def start_tracking(self) -> None:
        """
        Starts tracking if device not already tracking.
        """
        if not self.tracking:
            self.tracking = True
            self.tracker.start_tracking()

    def stop_tracking(self) -> None:
        """
        Stops tracking if device is tracking.
        """
        if self.tracking:
            self.tracking = False
            self.tracker.stop_tracking()

    def get_tracker_items(self) -> list:
        """
        Gets tracking items at given time.
        :return: list of items fron NDI Tracker
        """
        items = self.tracker.get_frame()
        return items
