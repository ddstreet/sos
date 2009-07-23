"""
setup.py - Setup package with the help from Python's DistUtils
"""

from distutils.core import setup

setup(
	name = 'sos',
    version = '1.8',
    author = 'Adam Stokes',
    author_email = 'ajs@redhat.com',
    url = 'http://fedorahosted.org/sos',
    description = 'SOS - son of sysreport',
	packages = ['sos', 'sos.plugins'],
	scripts = [],
	package_dir = {'': 'lib',},
	data_files = [ ('/etc', [ 'sos.conf']), 
    ('/usr/sbin', ['sosreport', 'extras/sysreport/sysreport.legacy']), 
    ('/usr/bin', ['extras/rh-upload-core']),
    ('/usr/share/sos/',['gpgkeys/rhsupport.pub']),
    ('/usr/share/sysreport', ['extras/sysreport/text.xsl', 'extras/sysreport/functions', 'extras/sysreport/sysreport-fdisk']), 
    ('/usr/share/man/man1', ['sosreport.1.gz']),
	('/usr/share/locale/af/LC_MESSAGES', ['po/af/sos.mo']),
	('/usr/share/locale/am/LC_MESSAGES', ['po/am/sos.mo']),
	('/usr/share/locale/ar/LC_MESSAGES', ['po/ar/sos.mo']),
	('/usr/share/locale/as/LC_MESSAGES', ['po/as/sos.mo']),
	('/usr/share/locale/be/LC_MESSAGES', ['po/be/sos.mo']),
	('/usr/share/locale/bg/LC_MESSAGES', ['po/bg/sos.mo']),
	('/usr/share/locale/bn/LC_MESSAGES', ['po/bn/sos.mo']),
	('/usr/share/locale/bn_IN/LC_MESSAGES', ['po/bn_IN/sos.mo']),
	('/usr/share/locale/bs/LC_MESSAGES', ['po/bs/sos.mo']),
	('/usr/share/locale/ca/LC_MESSAGES', ['po/ca/sos.mo']),
	('/usr/share/locale/cs/LC_MESSAGES', ['po/cs/sos.mo']),
	('/usr/share/locale/cy/LC_MESSAGES', ['po/cy/sos.mo']),
	('/usr/share/locale/da/LC_MESSAGES', ['po/da/sos.mo']),
	('/usr/share/locale/de/LC_MESSAGES', ['po/de/sos.mo']),
	('/usr/share/locale/el/LC_MESSAGES', ['po/el/sos.mo']),
	('/usr/share/locale/en/LC_MESSAGES', ['po/en/sos.mo']),
	('/usr/share/locale/en_GB/LC_MESSAGES', ['po/en_GB/sos.mo']),
	('/usr/share/locale/es/LC_MESSAGES', ['po/es/sos.mo']),
	('/usr/share/locale/et/LC_MESSAGES', ['po/et/sos.mo']),
	('/usr/share/locale/eu_ES/LC_MESSAGES', ['po/eu_ES/sos.mo']),
	('/usr/share/locale/fa/LC_MESSAGES', ['po/fa/sos.mo']),
	('/usr/share/locale/fi/LC_MESSAGES', ['po/fi/sos.mo']),
	('/usr/share/locale/fr/LC_MESSAGES', ['po/fr/sos.mo']),
	('/usr/share/locale/gl/LC_MESSAGES', ['po/gl/sos.mo']),
	('/usr/share/locale/gu/LC_MESSAGES', ['po/gu/sos.mo']),
	('/usr/share/locale/he/LC_MESSAGES', ['po/he/sos.mo']),
	('/usr/share/locale/hi/LC_MESSAGES', ['po/hi/sos.mo']),
	('/usr/share/locale/hr/LC_MESSAGES', ['po/hr/sos.mo']),
	('/usr/share/locale/hu/LC_MESSAGES', ['po/hu/sos.mo']),
	('/usr/share/locale/hy/LC_MESSAGES', ['po/hy/sos.mo']),
	('/usr/share/locale/id/LC_MESSAGES', ['po/id/sos.mo']),
	('/usr/share/locale/ilo/LC_MESSAGES', ['po/ilo/sos.mo']),
	('/usr/share/locale/is/LC_MESSAGES', ['po/is/sos.mo']),
	('/usr/share/locale/it/LC_MESSAGES', ['po/it/sos.mo']),
	('/usr/share/locale/ja/LC_MESSAGES', ['po/ja/sos.mo']),
	('/usr/share/locale/ka/LC_MESSAGES', ['po/ka/sos.mo']),
	('/usr/share/locale/kn/LC_MESSAGES', ['po/kn/sos.mo']),
	('/usr/share/locale/ko/LC_MESSAGES', ['po/ko/sos.mo']),
	('/usr/share/locale/ku/LC_MESSAGES', ['po/ku/sos.mo']),
	('/usr/share/locale/lo/LC_MESSAGES', ['po/lo/sos.mo']),
	('/usr/share/locale/lt/LC_MESSAGES', ['po/lt/sos.mo']),
	('/usr/share/locale/lv/LC_MESSAGES', ['po/lv/sos.mo']),
	('/usr/share/locale/mk/LC_MESSAGES', ['po/mk/sos.mo']),
	('/usr/share/locale/ml/LC_MESSAGES', ['po/ml/sos.mo']),
	('/usr/share/locale/mr/LC_MESSAGES', ['po/mr/sos.mo']),
	('/usr/share/locale/ms/LC_MESSAGES', ['po/ms/sos.mo']),
	('/usr/share/locale/my/LC_MESSAGES', ['po/my/sos.mo']),
	('/usr/share/locale/nb/LC_MESSAGES', ['po/nb/sos.mo']),
	('/usr/share/locale/nl/LC_MESSAGES', ['po/nl/sos.mo']),
	('/usr/share/locale/nn/LC_MESSAGES', ['po/nn/sos.mo']),
	('/usr/share/locale/nso/LC_MESSAGES', ['po/nso/sos.mo']),
	('/usr/share/locale/or/LC_MESSAGES', ['po/or/sos.mo']),
	('/usr/share/locale/pa/LC_MESSAGES', ['po/pa/sos.mo']),
	('/usr/share/locale/pl/LC_MESSAGES', ['po/pl/sos.mo']),
	('/usr/share/locale/pt/LC_MESSAGES', ['po/pt/sos.mo']),
	('/usr/share/locale/pt_BR/LC_MESSAGES', ['po/pt_BR/sos.mo']),
	('/usr/share/locale/ro/LC_MESSAGES', ['po/ro/sos.mo']),
	('/usr/share/locale/ru/LC_MESSAGES', ['po/ru/sos.mo']),
	('/usr/share/locale/si/LC_MESSAGES', ['po/si/sos.mo']),
	('/usr/share/locale/sk/LC_MESSAGES', ['po/sk/sos.mo']),
	('/usr/share/locale/sl/LC_MESSAGES', ['po/sl/sos.mo']),
	('/usr/share/locale/sq/LC_MESSAGES', ['po/sq/sos.mo']),
	('/usr/share/locale/sr/LC_MESSAGES', ['po/sr/sos.mo']),
	('/usr/share/locale/sr@latin/LC_MESSAGES', ['po/sr@latin/sos.mo']),
	('/usr/share/locale/sv/LC_MESSAGES', ['po/sv/sos.mo']),
	('/usr/share/locale/ta/LC_MESSAGES', ['po/ta/sos.mo']),
	('/usr/share/locale/te/LC_MESSAGES', ['po/te/sos.mo']),
	('/usr/share/locale/th/LC_MESSAGES', ['po/th/sos.mo']),
	('/usr/share/locale/tr/LC_MESSAGES', ['po/tr/sos.mo']),
	('/usr/share/locale/uk/LC_MESSAGES', ['po/uk/sos.mo']),
	('/usr/share/locale/ur/LC_MESSAGES', ['po/ur/sos.mo']),
	('/usr/share/locale/vi/LC_MESSAGES', ['po/vi/sos.mo']),
	('/usr/share/locale/zh_CN/LC_MESSAGES', ['po/zh_CN/sos.mo']),
	('/usr/share/locale/zh_TW/LC_MESSAGES', ['po/zh_TW/sos.mo']),
	('/usr/share/locale/zu/LC_MESSAGES', ['po/zu/sos.mo']),
	]
)
