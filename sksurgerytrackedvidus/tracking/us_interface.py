# coding=utf-8

"""
Module to interface with the Ultrasonix Machine
"""

import os
import time
import numpy as np
import sksurgeryultrasonix
import cv2


class USFrameManager():
    """
    A class to manage the connection to Ultrasonix
    machine.
    """
    def __init__(self,
                 ultrasonix_ip) -> None:
        """
        Instantiating the ultrasonix link using the
        config ip.
        :param ultrasonix_ip: str, format "X.Y.Z.A", IP
        address of the ultrasonix machine.
        """
        self.ip = ultrasonix_ip
        self.instantiate_ultrasonix()

    def instantiate_ultrasonix(self) -> None:
        """
        Instantiate and connect a ultrasonix connection
        instance.
        """
        ultrasonix_item = sksurgeryultrasonix.Ultrasonix.CreateInstance()
        ultrasonix_item.Connect(self.ip)
        self.ultrasonix_connection = ultrasonix_item

    def get_frame(self) -> None:
        """
        Gets a singular frame of data, returns np arrays.
        """
        # Timestamp the grabbing
        x = np.array(self.ultrasonix_connection.GetBuffer(), dtype=np.uint8)
        x=x.reshape(480,640)
        cv2.imshow('x',x)
        cv2.waitKey(1)
        # Do something with this data.
