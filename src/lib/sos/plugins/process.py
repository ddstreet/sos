### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools

class process(sos.plugintools.PluginBase):
    """process information
    """
    def setup(self):
        self.collectExtOutput("/bin/ps auxww", root_symlink = "ps")
        self.collectExtOutput("/usr/bin/pstree", root_symlink = "pstree")
        self.collectExtOutput("/usr/bin/ipcs -a")
        self.collectExtOutput("/usr/bin/ipcs -u")
        self.collectExtOutput("/usr/bin/ipcs -l")
        return

