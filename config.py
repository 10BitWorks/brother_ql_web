"""
This are the default settings. (DONT CHANGE THIS FILE)
Adjust your settings in 'instance/application.py'
"""

import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    LOG_LEVEL = logging.WARNING

    SERVER_PORT = 8013
    SERVER_HOST = '0.0.0.0'

    PRINTER_MODEL = 'QL-500'
    PRINTER_PRINTER = 'file:///dev/usb/lp1'

    LABEL_DEFAULT_ORIENTATION = 'standard'
    LABEL_DEFAULT_SIZE = '62'
    LABEL_DEFAULT_FONT_SIZE = 70
    LABEL_DEFAULT_QR_SIZE = 10
    LABEL_DEFAULT_LINE_SPACING = 100
    LABEL_DEFAULT_FONT_FAMILY = 'Barlow Condensed'
    LABEL_DEFAULT_FONT_STYLE = 'Bold'

    IMAGE_DEFAULT_MODE = 'grayscale'
    IMAGE_DEFAULT_BW_THRESHOLD = 70

    LABEL_DEFAULT_MARGIN_TOP = 24
    LABEL_DEFAULT_MARGIN_BOTTOM = 24
    LABEL_DEFAULT_MARGIN_LEFT = 35
    LABEL_DEFAULT_MARGIN_RIGHT = 35

    FONT_FOLDER = ''

    # Bundled 10BitWorks brand typefaces, source of truth: https://10bitworks.org/brand-assets/
    BRAND_FONT_FOLDER = os.path.join(basedir, 'app', 'static', 'fonts', 'brand')
    BRAND_FONT_FAMILIES = ('Barlow Condensed', 'Barlow', 'JetBrains Mono')
