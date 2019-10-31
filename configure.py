#! /usr/bin/env python3

import sys
from string import Template
import os
import json

SETTINGS_XML_TMPL = "templates/resources/m2/settings.xml.tmpl"
SETTINGS_XML =      "generated/resources/m2/settings.xml"

MVN_SH_TMPL =       "templates/scripts/mvn.sh.tmpl"
MVN_SH =            "generated/scripts/mvn.sh"

TOP_LVL_MVN_SH =    "mvn.sh"

def setBasedir (argv):
    scriptpath = os.path.realpath(argv[0])
    scriptdir = os.path.dirname(scriptpath)
    basedir = scriptdir
    os.environ['BASEDIR'] = basedir

def readTemplate (filename):
    with open(filename) as f:
        template = f.read()
    return template

def injectOsEnvironment (template):
    return Template(template).safe_substitute(os.environ)

def writeText (filename, s):
    f = open (filename, 'w')
    f.write (s)
    f.close()
    
# Business Logic

def createSettingsXML():
    template = readTemplate (os.path.join(os.environ['BASEDIR'], SETTINGS_XML_TMPL))
    text = injectOsEnvironment (template)
    filename = os.path.join (os.environ['BASEDIR'], SETTINGS_XML)
    writeText (filename, text)

def createMvnSh():
    template = readTemplate (os.path.join(os.environ['BASEDIR'], MVN_SH_TMPL))
    text = injectOsEnvironment (template)
    filename = os.path.join (os.environ['BASEDIR'], MVN_SH)
    writeText (filename, text)

def createToplevelMvnSh():
    basedir = os.environ['BASEDIR']
    text = """\
#! /usr/bin/env bash
exec {mvnscript}
""".format(mvnscript = os.path.join(basedir, MVN_SH))
    filename = os.path.join(basedir, TOP_LVL_MVN_SH)
    writeText(filename, text)

# Entrypoint

def main(argv):
    setBasedir(argv)

    # Business Logic
    createSettingsXML()
    createMvnSh()
    createToplevelMvnSh()

if __name__ == '__main__':
    main (sys.argv)