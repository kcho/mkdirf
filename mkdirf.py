#!python
import os
import argparse
import datetime
import time

def main(args):
    fileName=str(time.strftime("%Y"))+'_'+str(time.strftime("%m"))+'_'+str(time.strftime("%d"))+'_'+str(args)

    print fileName
    os.system('mkdir {0}'.format(fileName))


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Creates a folder with a name that follows the script with data")
    parser.add_argument('--t',default=None, help="name of the folder")
    args=parser.parse_args()

    main(args.t)



