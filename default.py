# -*- coding: UTF-8 -*-
# /*
# *      Copyright (C) Jose Riha
# *
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */
import os

import xbmcaddon
import util
import xbmcprovider
import xbmcutil


__scriptid__ = 'plugin.video.topserialy.sk'
__scriptname__ = 'topserialy.sk'
__addon__ = xbmcaddon.Addon(id=__scriptid__)
__language__ = __addon__.getLocalizedString

sys.path.append(os.path.join(__addon__.getAddonInfo('path'), 'resources', 'lib'))
import topserialy

settings = {'downloads': __addon__.getSetting('downloads'), 'quality': __addon__.getSetting('quality')}

params = util.params()
if params == {}:
    xbmcutil.init_usage_reporting(__scriptid__)
xbmcprovider.XBMCMultiResolverContentProvider(topserialy.TopSerialyContentProvider(), settings, __addon__).run(params)
