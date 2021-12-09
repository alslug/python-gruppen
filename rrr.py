#!/usr/bin/python3

import os
import shutil
from zipfile import ZipFile
import zipfile


class minklasse():

    def __init__(self, mappecounter, udFolder):
        self.mappecounter = mappecounter
        self.unZipMappeCount = 0 
        self.udFolder = udFolder
        self.tempFolder = os.path.join('/mnt/minlvhdd/Xmindisk/', 'temp')
        if not os.path.isdir(self.tempFolder):
            os.mkdir(self.tempFolder)

    def naestefil(self)->int:
        self.mappecounter += 1 
        return f'{self.mappecounter}'

    def naesteUnzipMappe(self):
        self.unZipMappeCount += 1
        return os.path.join( self.tempFolder, f'Z{self.unZipMappeCount}') 

    def sorter(self, minfil)-> None:

        if (minfil[-4:] == '.txt'):
            if minfil[-5:] == '8.txt':
                targetFolder = 'utf'
                targetFile = self.naestefil() +'8.txt'
            else:
                targetFolder = 'txt'
                targetFile = self.naestefil() +'.txt'

        elif minfil.endswith('.pdf'):
            targetFolder = 'pdf'
            targetFile = self.naestefil() + '.pdf'
        elif minfil.endswith('.mp3'):
            targetFolder = 'mp3'
            targetFile = self.naestefil() +'.mp3'
        else:
            targetFolder = 'andrefiler'
            targetFile = self.naestefil() + minfil[-4:]
#     targetFolder = os.path.join( sortfolder('andrefiler/'), str(str(self.naestefil()) + fileName[-4:]))

        target = os.path.join( self.udFolder, targetFolder, targetFile)
        print(f'kopierer {minfil} til {target}')
        try :
            shutil.copy( minfil, target)
        except IOError:
            print('kopiering ikke mulig')

    def myunzip(self, zipfil ):

        print(f'{zipfil=}')

        unzipMappe = self.naesteUnzipMappe()
        if not os.path.isdir(unzipMappe):
            os.mkdir(unzipMappe)
        with ZipFile(zipfil, 'r') as zipObject:
            try:
                zipObject.extractall(unzipMappe)
            except ValueError :
                print('udpakning ikke ok')
        return unzipMappe

    def gennemGaaMappe(self, mappeNavn) :
        for denneMappe, _, filnavne in os.walk(mappeNavn):
            print(f'{denneMappe=}')
            for fil in filnavne:
                pFil = os.path.join( denneMappe, fil )
                print(fil)
                if fil.endswith('.zip'):
                    nyMappe = self.myunzip( pFil )
                    self.gennemGaaMappe(nyMappe)
                    # Slet nyMappe
                else :
                    self.sorter( pFil )


def mkSortDir(folder):
    folder = os.path.join( highestsortfolder, folder )
    if not os.path.isdir(folder):
        os.mkdir(folder)


if __name__ == '__main__':
    pwd = '/mnt/minlvhdd/Xmindisk/'
    highestfolder = os.path.join( pwd, 'gutenbergzip/' )
    highestsortfolder = os.path.join(pwd, 'output/')

    # lav mappe struktur

    if not os.path.isdir(highestsortfolder):
        os.mkdir(highestsortfolder)

    mkSortDir('utf')
    mkSortDir( 'txt' )
    mkSortDir( 'pdf' )
    mkSortDir( 'mp3' )
    mkSortDir( 'andrefiler' )


    system1 = minklasse(100, highestsortfolder)

    system1.gennemGaaMappe(highestfolder)
