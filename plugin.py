# Copyright (C) 2023  Gerard Roche
#
# This file is part of ShowAsciiValue.
#
# ShowAsciiValue is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ShowAsciiValue is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ShowAsciiValue.  If not, see <https://www.gnu.org/licenses/>.

import sublime
import sublime_plugin


class ShowAsciiValue(sublime_plugin.EventListener):

    def on_selection_modified(self, view):
        region = view.sel()[-1]
        point = region.b - 1 if region.a < region.b else region.b
        c_str = view.substr(point)
        c_ord = ord(c_str)
        c_hex = hex(c_ord)
        c_oct = oct(c_ord)
        c_not = _char_to_notation(c_str)

        sublime.status_message(
            '%7s %3s,  Hex %4s,  Octal %5s' %
            (c_not, c_ord, c_hex, c_oct))


def _char_to_notation(char: str) -> str:
    # Convert a char to a key notation. Uses vim key notation.
    # See https://vimhelp.appspot.com/intro.txt.html#key-notation
    char_notation_map = {
        '\0': "Nul",
        ' ': "Space",
        '\t': "Tab",
        '\n': "NL"
    }

    if char in char_notation_map:
        char = char_notation_map[char]

    return "<" + char + ">"
