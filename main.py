"""
Simple-Video-Converter - Version 1.0

Copyright © Gaëtan Sencie 2025
Tous droits réservés.
"""

import os
import subprocess
import shutil
import re
from datetime import datetime
import sys
import platform
import json
import concurrent.futures
import logging # Import the logging module
import webbrowser # Import the webbrowser module

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QGroupBox, QLabel, QLineEdit, QPushButton,
    QProgressBar, QTextEdit, QFileDialog, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QSlider,
    QRadioButton, QButtonGroup, QCheckBox, QAbstractItemView,
    QMenu, QComboBox, QSizePolicy, QSplashScreen, QToolTip
)
from PySide6.QtCore import (
    QThread, Signal, Slot, Qt, QTimer, QMimeData, QDir, QUrl, QElapsedTimer, QPoint, QSettings
)
from PySide6.QtGui import (
    QDragEnterEvent, QDropEvent, QDragMoveEvent, QDesktopServices,
    QColor, QIntValidator, QValidator, QIcon, QPixmap,
    QPalette, QFont # <-- Ajout de QPalette et QFont ici
)



--------> CODE UNDER LICENSE


    sys.exit(app.exec())