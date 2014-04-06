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

## This plugin enables collection of logs for Power systems and more
## specific logs for Pseries, PowerNV platforms.

import os
from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin

class PowerPC(Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin):
    """IBM Power System related information
    """

    plugin_name = 'powerpc'

    def check_enabled(self):
        return (self.policy().get_arch() == "ppc64")

    def setup(self):
        try:
            with open('/proc/cpuinfo', 'r') as fp:
                contents = fp.read()
                ispSeries = "pSeries" in contents
                isPowerNV = "PowerNV" in contents
        except:
            ispSeries = False
            isPowerNV = False

        if ispSeries or isPowerNV:
            self.add_copy_specs([
                "/proc/device-tree/",
                "/proc/loadavg",
                "/proc/locks",
                "/proc/misc",
                "/proc/swaps",
                "/proc/version",
                "/dev/nvram",
                "/var/log/platform",
                "/var/lib/lsvpd/"
            ])
            self.add_cmd_output("ppc64_cpu --smt")
            self.add_cmd_output("ppc64_cpu --cores-present")
            self.add_cmd_output("ppc64_cpu --cores-on")
            self.add_cmd_output("ppc64_cpu --run-mode")
            self.add_cmd_output("ppc64_cpu --frequency")
            self.add_cmd_output("ppc64_cpu --dscr")
            self.add_cmd_output("lscfg -vp")
            self.add_cmd_output("lsmcode -A")
            self.add_cmd_output("lsvpd --debug")

        if ispSeries:
            self.add_copy_specs([
                "/proc/ppc64/lparcfg",
                "/proc/ppc64/eeh",
                "/proc/ppc64/systemcfg"
            ])
            self.add_cmd_output("lsvio -des")
            self.add_cmd_output("servicelog --dump")
            self.add_cmd_output("servicelog_notify --list")
            self.add_cmd_output("usysattn")
            self.add_cmd_output("usysident")
            self.add_cmd_output("serv_config -l")
            self.add_cmd_output("bootlist -m both -r")
            self.add_cmd_output("lparstat -i")

        if isPowerNV:
            self.add_copy_specs([
                "/proc/ppc64/",
                "/sys/kernel/debug/powerpc/"
            ])
            if os.path.isdir("/var/log/dump"):
                self.add_cmd_output("ls -l /var/log/dump")


# vim: et ts=4 sw=4
