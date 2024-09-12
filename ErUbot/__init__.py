import asyncio
import re
import os
import sys
import time
from os import environ, execle
from datetime import datetime
from pyrogram import *

from pyrogram.handlers import *
from pyrogram.types import *
from ErUbot.utils.dbfunctions import get_pref