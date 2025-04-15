from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

import screen_brightness_control as pct

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from geopy.geocoders import Nominatim
from timezonefinder import timezonefinder
