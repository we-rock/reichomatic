# Copyright (C) 2022 David E. Lambert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <https://www.gnu.org/licenses/>.

__version__ = '0.1'

import sys
import random
import subprocess
import shlex
from pathlib import Path

from PyQt5.QtCore import (Qt,
                          QRunnable,
                          QThreadPool,
                          pyqtSlot)
from PyQt5.QtGui import (QIcon,
                         QPixmap,
                         QKeySequence,
                         QFontDatabase,
                         QFont)
from PyQt5.QtWidgets import *

HERE = Path(__file__).parent.resolve()

def generate(bpm=120):
    length = (60 / bpm) * 4
    div = (3, 4, 5, 6, 7, )
    dum, tek = random.sample(div, k=2)
    dum_rest = length / dum
    tek_rest = length / tek
    
    print('BPM: {}  MEASURE LENGTH: {}  DUM: {}  TEK: {}'
          .format(bpm, length, dum, tek))
    
    d = 0
    while d < dum - 1:
        print('DUM, time.sleep({}))'.format(dum_rest))
        d += 1
    print('DUM ==============')
        
    t = 0
    while t < tek - 1:
        print('TEK, time.sleep({}))'.format(tek_rest))
        t += 1
    print('TEK ==============')
    
generate()
    