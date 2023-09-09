# The PEP 484 type hints stub file for the QtTextToSpeech module.
#
# Generated by SIP 6.7.10
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QTextToSpeech(QtCore.QObject):

    class State(enum.Enum):
        Ready = ... # type: QTextToSpeech.State
        Speaking = ... # type: QTextToSpeech.State
        Paused = ... # type: QTextToSpeech.State
        Error = ... # type: QTextToSpeech.State

    class ErrorReason(enum.Enum):
        NoError = ... # type: QTextToSpeech.ErrorReason
        Initialization = ... # type: QTextToSpeech.ErrorReason
        Configuration = ... # type: QTextToSpeech.ErrorReason
        Input = ... # type: QTextToSpeech.ErrorReason
        Playback = ... # type: QTextToSpeech.ErrorReason

    class BoundaryHint(enum.Enum):
        Default = ... # type: QTextToSpeech.BoundaryHint
        Immediate = ... # type: QTextToSpeech.BoundaryHint
        Word = ... # type: QTextToSpeech.BoundaryHint
        Sentence = ... # type: QTextToSpeech.BoundaryHint

    @typing.overload
    def __init__(self, engine: typing.Optional[str], params: typing.Dict[typing.Optional[str], typing.Any], parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, engine: typing.Optional[str], parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    errorOccurred: typing.ClassVar[QtCore.pyqtSignal]
    engineChanged: typing.ClassVar[QtCore.pyqtSignal]
    voiceChanged: typing.ClassVar[QtCore.pyqtSignal]
    volumeChanged: typing.ClassVar[QtCore.pyqtSignal]
    pitchChanged: typing.ClassVar[QtCore.pyqtSignal]
    rateChanged: typing.ClassVar[QtCore.pyqtSignal]
    localeChanged: typing.ClassVar[QtCore.pyqtSignal]
    stateChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setVoice(self, voice: 'QVoice') -> None: ...
    def setVolume(self, volume: float) -> None: ...
    def setPitch(self, pitch: float) -> None: ...
    def setRate(self, rate: float) -> None: ...
    def setLocale(self, locale: QtCore.QLocale) -> None: ...
    def resume(self) -> None: ...
    def pause(self, boundaryHint: 'QTextToSpeech.BoundaryHint' = ...) -> None: ...
    def stop(self, boundaryHint: 'QTextToSpeech.BoundaryHint' = ...) -> None: ...
    def say(self, text: typing.Optional[str]) -> None: ...
    @staticmethod
    def availableEngines() -> typing.List[str]: ...
    def volume(self) -> float: ...
    def pitch(self) -> float: ...
    def rate(self) -> float: ...
    def availableVoices(self) -> typing.List['QVoice']: ...
    def voice(self) -> 'QVoice': ...
    def locale(self) -> QtCore.QLocale: ...
    def availableLocales(self) -> typing.List[QtCore.QLocale]: ...
    def state(self) -> 'QTextToSpeech.State': ...
    def errorString(self) -> str: ...
    def errorReason(self) -> 'QTextToSpeech.ErrorReason': ...
    def engine(self) -> str: ...
    def setEngine(self, engine: typing.Optional[str], params: typing.Dict[typing.Optional[str], typing.Any] = ...) -> bool: ...


class QVoice(PyQt6.sip.simplewrapper):

    class Age(enum.Enum):
        Child = ... # type: QVoice.Age
        Teenager = ... # type: QVoice.Age
        Adult = ... # type: QVoice.Age
        Senior = ... # type: QVoice.Age
        Other = ... # type: QVoice.Age

    class Gender(enum.Enum):
        Male = ... # type: QVoice.Gender
        Female = ... # type: QVoice.Gender
        Unknown = ... # type: QVoice.Gender

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QVoice') -> None: ...

    def __eq__(self, other: object): ...
    def __ne__(self, other: object): ...
    def locale(self) -> QtCore.QLocale: ...
    def swap(self, other: 'QVoice') -> None: ...
    @staticmethod
    def ageName(age: 'QVoice.Age') -> str: ...
    @staticmethod
    def genderName(gender: 'QVoice.Gender') -> str: ...
    def age(self) -> 'QVoice.Age': ...
    def gender(self) -> 'QVoice.Gender': ...
    def name(self) -> str: ...
