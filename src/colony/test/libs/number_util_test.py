#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (C) 2008 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 3219 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2009-05-26 11:52:00 +0100 (ter, 26 Mai 2009) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.libs.test_util
import colony.libs.number_util

class NumberTest(colony.libs.test_util.ColonyTestCase):
    """
    Class that tests the number various functions method.
    """

    def test_to_fixed(self):
        """
        Tests the to fixed function.
        """

        # creates the the same value using an "infinite"
        # (repeating decimal) approach (through the 0.33)
        # and using the final and fixed value, this will create
        # problems in a normal float comparison
        infinite_float_value = 0.33 + 0.11 - 0.09 - 0.33
        correct_float_value = 0.02

        # verifies that the "infinite" (repeating decimal) based
        # float number is not the same as the non "infinite" based
        # number in a normal based float comparison
        self.assertNotEqual(infinite_float_value, correct_float_value)

        # converts both values into the fixed representation to test them
        # into a fixed based comparison, that must be valid
        infinite_fixed_value = colony.libs.number_util.to_fixed(infinite_float_value, 2)
        correct_fixed_value = colony.libs.number_util.to_fixed(correct_float_value, 2)

        # verifies that the comparison of the fixed based values should
        # be valid (this time the comparison takes no side effects)
        self.assertEqual(infinite_fixed_value, correct_fixed_value)