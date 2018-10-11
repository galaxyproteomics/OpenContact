#!/usr/bin/env python


from __future__ import print_function


# import fortran modules
import argparse
import os
import re
import shutil
import sys
import time

from contact import contact

from it import inpututil


def convert_to_tsv(txtfile, tsvfile):
    pat = '^([A-Z]{3})\s{0,5}(\d{1,6})\s?([A-Z0-9]{1,4})\s{0,7}(\d{1,6}) ' +\
        '([A-Z]{3})\s{0,5}(\d{1,6})\s?([A-Z0-9]{1,4})\s{0,7}(\d{1,6})' +\
        '\s{2,3}([+-]?\S+)\s{2,3}([+-]?\S+)\s{2,3}([+-]?\S+)$'
    prog = re.compile(pat)
    with open(tsvfile, 'w') as wtr:
        with open(txtfile, 'r') as rdr:
            for i, line in enumerate(rdr):
                try:
                    wtr.write('%s\n' % '\t'.join(prog.match(line).groups()))
                except Exception as e:
                    exit('Error parsing %s %d %s: %s ' % (txtfile,i,line,e))



def __main__():
    parser = argparse.ArgumentParser(
        description='OpenContact')
    parser.add_argument(
        '-a', '--protA', default=None,
        help='Path to proteinA.pdb')
    parser.add_argument(
        '-b', '--protB', default=None,
        help='Path to proteinB.pdb')
    parser.add_argument(
        '-A', '--protA_chain', default=None,
        help='proteinA chain')
    parser.add_argument(
        '-B', '--protB_chain', default=None,
        help='proteinB chain')
    parser.add_argument(
        '-t', '--tabular', default=False,
        action='store_true',
        help='Create tab separated map files')
    args = parser.parse_args()

    if not all([args.protA, args.protB, args.protA_chain, args.protB_chain]):
        parser.print_usage()
        sys.exit(1)

    # resource files need to be in working directory
    resource_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    resource_files = ['ctresc03.pdb', 'ctresc03n.pdb', 'residc03n.pdb', 'residc03.pdb', 'ntresc03n.pdb', 'ntresc03.pdb', 'ljresidn', 'ljresid']
    for f in resource_files:
        shutil.copyfile(resource_path+os.sep+f, "."+os.sep+f)
    start_time = time.time()
    # opencontact has hard coded input filenames
    shutil.copyfile(args.protA, "."+os.sep+"prota.pdb")
    shutil.copyfile(args.protB, "."+os.sep+"protb.pdb")

    inpututil(args.protA_chain, args.protB_chain)
    contact()
    end_time = time.time()
    print('Done %s' % (end_time - start_time))
    if args.tabular:
        convert_to_tsv('coarsedata.txt', 'coarsedata.tsv')
        convert_to_tsv('finedata.txt', 'finedata.tsv')


if __name__ == "__main__":
    __main__()
