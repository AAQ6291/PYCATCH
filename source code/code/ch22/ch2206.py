#!/usr/bin/env python
# -*- coding: cp950 -*-

import py2exe
from distutils.core import setup

class target:
   def __init__(self, **kw):
      self.__dict__.update(kw)
      self.version = "1.0"
      self.company_name = "PythonTW"
      self.copyright = "copyright PythonTW"
      self.name = u"����������"
      self.description = u"��@�����Ҧ�������"


manifest_template = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
/>
<description>%(prog)s Program</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
'''

com = target(
   script = "ch2204.py",
   other_resources = [(24, 1, manifest_template % dict(prog="ch2204"))],
   icon_resources = [(1, "python.ico")],
   dest_base = "ch2204")

setup(
   options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 1,
                          "bundle_files": 1}},
   zipfile = None,
   windows = [com],
    )
