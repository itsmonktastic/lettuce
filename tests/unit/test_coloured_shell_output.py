# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2011>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lettuce.plugins.colored_shell_output import height_of_wrapped_string

from nose.tools import eq_

def test_string_less_than_width():
    "Shouldn't wrap, should return 1"
    eq_(height_of_wrapped_string("foo", 4), 1)

def test_string_one_more_than_width():
    "Should wrap, should return 2"
    eq_(height_of_wrapped_string("foofo", 4), 2)

def test_string_more_than_twice_the_length():
    "Should wrap, should return 3"
    eq_(height_of_wrapped_string("foobarbaz", 4), 3)

