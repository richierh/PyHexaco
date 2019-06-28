

import os
import platform
import time
import pathlib
import webbrowser

# os.remove(self.options.dest_name)


def printcurrent(thefile):



    webbrowser.open(thefile)
    # if platform.system()=="Linux":
    #     os.system('lp "{}"'.format(thefile))
    #     pass
    
    
    # elif platform.system()=="Windows":
    #     # os.startfile(thefile, "print")
    #     import win32api

    #     win32api.ShellExecute(0, "print", thefile, None,  ".",  0)
    #     time.sleep(10)
    #     # for p in psutil.process_iter(): #Close Acrobat after printing the PDF
    #     #     if 'AcroRd' in str(p):
    #     #         p.kill()

if __name__ == "__main__":

    thefile = "tuto1d.pdf"
    # thefile = str(pathlib.Path(thefile))
    print (thefile)
    printcurrent(thefile)

