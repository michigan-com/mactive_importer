# -*- coding: utf-8 -*-
"""
    deathnotice_importer
    ~~~~~~~~~~~~~~~~~~~~

    Parses an XML file and adds obituraties to our `death_notice` mySQL database.

    It starts by reading an XML file, usually named `deathnotices.txt`.
    Then it parses the XML file for obituaries from the mactive adbase management
    system.  It then saves the obits into our mySQL database.

    Finally it copies all associated images into its respective directory under
    the mideathnotices app, usually:
        `50.57.27.19:/mnt/nfs/docs/http-detroitnewspapers/mideathnotices/assets/images/dnimages/<YEAR>/<MONTH>/`.
"""

__version__ = '0.0.1'

if __name__ == '__main__':
    pass
