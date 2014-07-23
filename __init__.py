# -*- coding: utf-8 -*-
"""
/***************************************************************************
 replaceGeometry
                                 A QGIS plugin
 a tool for easy replacing of a feature geometry
                             -------------------
        begin                : 2014-07-23
        copyright            : (C) 2014 by Enrico Ferreguti
        email                : enricofer@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load replaceGeometry class from file replaceGeometry.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .replaceGeometry import replaceGeometry
    return replaceGeometry(iface)
