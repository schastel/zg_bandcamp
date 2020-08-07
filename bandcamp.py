#!/usr/bin/env python3

import sys
import os
import zipfile

DEBUG = True

def debug(message):
    if DEBUG:
        import datetime
        sys.stdout.write("%s | %s\n" % (datetime.datetime.now().isoformat(), message))
        pass
    return

def process(targetdir, zipfilename):
    debug("processing %s" % zipfilename)
    zipbasename = zipfilename.split('/')[-1]
    bandname = None
    album = ""
    for elt in zipbasename.split('-'):
        if bandname is None:
            bandname = elt
        else:
            album = "%s%s" % (album, elt)
    bandname = bandname.strip()
    album = album.replace(".zip", "").strip()
    debug("bandname = %s" % bandname)
    debug("album = %s" % album)
    finaltargetdir = '%s/%s/%s' % (targetdir, bandname, album)
    try:
        os.makedirs(finaltargetdir)
    except OSError as e:
        debug("%s" % e)
        pass
    with zipfile.ZipFile(zipfilename, 'r') as zip_ref:
        zip_ref.extractall(finaltargetdir)
        pass
    return
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("\n%s <rootdir> [file.zip...]\n" % sys.argv[0])
        sys.stderr.write("\tFor each zipfile, create <rootdir>/<bandname>/<album> and unzip the file there\n")
        sys.stderr.write("\n")
        sys.stderr.write("e.g. %s ~/Music \"~/Downloads/The Vision Bleak - Carpathia – A Dramatic Poem (Luxus).zip\"\n" % sys.argv[0])
        sys.stderr.write("\n")
        sys.exit(1)
        pass
    targetdir = sys.argv[1]
    zipfilenames = sys.argv[2:]
    debug("Filenames = %s" % zipfilenames)
    for zipfilename in zipfilenames:
        process(targetdir, zipfilename)
