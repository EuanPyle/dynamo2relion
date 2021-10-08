import re
from pathlib import Path
import os
import sys
import numpy as np

def sanitise_m_starfile_name(starfile_name: str) -> str:
    """
    Makes sure STAR filename is properly formatted for import into M (requires _data.star)
    :param starfile_name:
    :return:
    """
    if starfile_name.endswith('_data.star'):
        return starfile_name
    elif starfile_name.endswith('.star') and not starfile_name.endswith('_data.star'):
        return re.sub(r".star", "_data.star", starfile_name)
    else:
        return starfile_name + '_data.star'


def sanitise_dynamo_table_filename(table_file_name: str) -> str:
    """
    Make sure table file ends in .tbl
    :param table_file_name:
    :return:
    """
    if not table_file_name.endswith('.tbl'):
        table_file_name += '.tbl'

    return table_file_name


def reextract_table_filename(table_file_name: str) -> str:
    """

    :param table_file_name:
    :return:
    """
    return table_file_name.replace('.tbl', '.reextract.tbl')


def extract_tomostar_from_image_name(filename: str) -> str:
    """
    from a given filename, expected to be from the 'rlnImageName' column of a STAR file output by M
    extract the tomogram name
    :param filename:
    :return:
    """
    p = Path(filename)
    tomo_name = p.parts[-2]
    tomostar = tomo_name + '.tomostar'
    return tomostar

def find_tomo_name(table_tomon, ts_directory: str) -> str:
    # get list of directories in ts_directory
    ts_list = []
    for file in os.listdir(ts_directory):
        d=os.path.join(ts_directory,file)
        if os.path.isdir(d):
            ts_list.append(file)
        
    tomo_name_list = [''] * len(table_tomon)
    
    # extract ts naming convention and TS number	
    for tomo_name in ts_list:
        ts_string=re.split('(\d+)',tomo_name)
        while('' in ts_string) :
            ts_string.remove('')
        if len(ts_string) > 2:
            sys.exit('Check the folder names in ts_directory. Should only contain folders with variations of the ts_01 TS_15 etc. naming convention')
        tomo_num = int(ts_string[1])
	
	# assign tomo_name to correct particles
        tomon_indices = np.asarray(np.where(table_tomon == tomo_num))[0]

        for i in tomon_indices:
            tomo_name_list[i] = tomo_name
    return tomo_name_list

