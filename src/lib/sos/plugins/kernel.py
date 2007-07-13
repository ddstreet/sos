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
import commands, os, re

class kernel(sos.plugintools.PluginBase):
    """kernel related information
    """
    optionList = [("modinfo", 'Gathers module information on all modules', 'fast', 1),
                  ('sysrq', 'Trigger SysRq dumps', 'fast', 1)]
    moduleFile = ""
    taintList = [
        {'regex':'mvfs*', 'description':'Clearcase module'},
        {'regex':'vnode*', 'description':'Clearcase module'},
        {'regex':'vxfs*', 'description':'Veritas file system module'},
        {'regex':'vxportal*', 'description':'Veritas module'},
        {'regex':'vxdmp*', 'description':'Veritas dynamic multipathing module'},
        {'regex':'vxio*', 'description':'Veritas module'},
        {'regex':'vxspec*"', 'description':'Veritas module'},
        {'regex':'dcd*', 'description':'Dell OpenManage Server Administrator module'},
        {'regex':'ocfs', 'description':'Oracle cluster filesystem module'},
        {'regex':'oracle*', 'description':'Oracle module'},
        {'regex':'vmnet*', 'description':'VMware module'},
        {'regex':'vmmon*', 'description':'VMware module'},
        {'regex':'egenera*', 'description':'Egenera module'},
        {'regex':'emcp*', 'description':'EMC module'},
        {'regex':'ocfs*', 'description':'OCFS module'},
        {'regex':'nvidia', 'description':'NVidia module'},
        {'regex':'ati-', 'description':'ATI module'}
        ]

        # HP
        #
        #

    
    def setup(self):
        self.collectExtOutput("/bin/uname -a", root_symlink = "uname")
        self.moduleFile = self.collectOutputNow("/sbin/lsmod", root_symlink = "lsmod")
        if self.isOptionEnabled('modinfo'):
          runcmd = ""
          for kmod in commands.getoutput('/sbin/lsmod | /bin/cut -f1 -d" " 2>/dev/null | /bin/grep -v Module 2>/dev/null').split('\n'):
            if '' != kmod.strip():
              runcmd = runcmd + " " + kmod
          if len(runcmd):
            self.collectExtOutput("/sbin/modinfo " + runcmd)
        self.collectExtOutput("/sbin/ksyms")
        self.addCopySpec("/proc/filesystems")
        self.addCopySpec("/proc/ksyms")
        self.addCopySpec("/proc/slabinfo")
        kver = commands.getoutput('/bin/uname -r')
        depfile = "/lib/modules/%s/modules.dep" % (kver,)
        self.addCopySpec(depfile)
        self.addCopySpec("/etc/conf.modules")
        self.addCopySpec("/etc/modules.conf")
        self.addCopySpec("/etc/modprobe.conf")
        self.collectExtOutput("/usr/sbin/dmidecode")
        self.collectExtOutput("/usr/sbin/dkms status")
        self.addCopySpec("/proc/cmdline")
        self.addCopySpec("/proc/driver")
        self.addCopySpec("/proc/sys/kernel/tainted")
        # trigger some sysrq's.  I'm not sure I like doing it this way, but
        # since we end up with the sysrq dumps in syslog whether we run the 
        # syslog report before or after this, I suppose I can live with it.
        if self.isOptionEnabled('sysrq') and os.access("/proc/sysrq-trigger", os.W_OK) and os.access("/proc/sys/kernel/sysrq", os.R_OK):
          sysrq_state = commands.getoutput("/bin/cat /proc/sys/kernel/sysrq")
          commands.getoutput("/bin/echo 1 > /proc/sys/kernel/sysrq")
          for key in ['m', 'p', 't']:
            commands.getoutput("/bin/echo %s > /proc/sysrq-trigger" % (key,))
          commands.getoutput("/bin/echo %s > /proc/sys/kernel/sysrq" % (sysrq_state,))
          # No need to grab syslog here if we can't trigger sysrq, so keep this
          # inside the if
          self.addCopySpec("/var/log/messages")
        
        return

    def analyze(self):
        infd = open("/proc/modules", "r")
        modules = infd.readlines()
        infd.close()

        for modname in modules:
            modname=modname.split(" ")[0]
            modinfo_srcver = commands.getoutput("/sbin/modinfo -F srcversion %s" % modname)
            if not os.access("/sys/module/%s/srcversion" % modname, os.R_OK):
                continue
            infd = open("/sys/module/%s/srcversion" % modname, "r")
            sys_srcver = infd.read().strip("\n")
            infd.close()
            if modinfo_srcver != sys_srcver:
                self.addAlert("Loaded module %s differs from the one present on the file-system")

            # this would be a good moment to check the module's signature
            # but at the moment there's no easy way to do that outside of
            # the kernel. i will probably need to write a C lib (derived from
            # the kernel sources to do this verification.

        savedtaint = os.path.join(self.cInfo['dstroot'], "/proc/sys/kernel/tainted")
        infd = open(savedtaint, "r")
        line = infd.read()
        infd.close()
        line = line.strip()
        if (line != "0"):
            self.addAlert("Kernel taint flag is <%s>\n" % line)


        infd = open(self.moduleFile, "r")
        modules = infd.readlines()
        infd.close()

        #print(modules)
        for tainter in self.taintList:
            p = re.compile(tainter['regex'])
            for line in modules:
                if p.match(line) != None:
                    # found a taint match, create an alert
                    moduleName = line.split()[0]
                    self.addAlert("Check for tainted kernel by module %s, which is %s" % (moduleName, tainter['description']))
        return
