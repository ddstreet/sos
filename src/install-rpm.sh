rm -rf $RPM_BUILD_ROOT
python setup.py install --optimize 1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# 'brp-compress' gzips the man pages without distutils knowing... fix this
sed -i -e 's@man/man\([[:digit:]]\)/\(.\+\.[[:digit:]]\)$@man/man\1/\2.gz@g' INSTALLED_FILES
