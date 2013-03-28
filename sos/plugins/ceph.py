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

from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin

class ceph(Plugin, RedHatPlugin, UbuntuPlugin):
    """information on CEPH
    """
    optionList = [("log", "gathers all ceph logs", "slow", False)]

    packages = ('ceph',
                'ceph-mds',
                'ceph-common',
                'libcephfs1',
                'ceph-fs-common')

    def setup(self):
        self.add_copy_specs(["/etc/ceph/",
                           "/var/log/ceph/"])

        self.add_cmd_output("/usr/bin/ceph status")
        self.add_cmd_output("/usr/bin/ceph health")
        self.add_cmd_output("/usr/bin/ceph osd tree")
        self.add_cmd_output("/usr/bin/ceph osd stat")
        self.add_cmd_output("/usr/bin/ceph osd dump")
        self.add_cmd_output("/usr/bin/ceph mon stat")
        self.add_cmd_output("/usr/bin/ceph mon dump")

