"""Install instructions for Chipster server.
"""
import os

from fabric.api import *
from fabric.contrib.files import *

from shared import (_if_not_installed)

@_if_not_installed("chipsterserver")
def install_chipsterserver(env):
    """Install Chipster server environment (single node install)

    http://chipster.sourceforge.net
    """
    run("wget http://www.nic.funet.fi/pub/sci/molbio/chipster/dist/versions/2.0.0/chipster-2.0.0.tar.gz")
    run("tar -xzf chipster-2.0.0.tar.gz")
    run("rm -f chipster-2.0.0.tar.gz")
    run("touch chipster/auto-config-to-be-run")
    run("mv chipster /opt")

