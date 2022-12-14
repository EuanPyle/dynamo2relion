import re
import os
import sys
import numpy as np

from pathlib import Path
from typing import Optional

class IOConverter:
    def __init__(self, input_table: Path, output_name: Optional[Path] = None):
        self.input_table: Path = input_table
        if output_name is not None:
            self.output_name: str = output_name
        else:
            self.output_name: str = self.generate_output_file_name(self.input_table) 
    
    def generate_output_file_name(self, input_table: Path) -> Path:
        """
	Generate output file name as identical to input file name with .star extention
	"""
        output_name = input_table.stem + '.star'
        return output_name

def find_tomo_name(table_tomon, tilt_series_directory: str) -> str:
    # get list of directories in tilt_series_directory
    ts_list = []
    for file in os.listdir(tilt_series_directory):
        d=os.path.join(tilt_series_directory,file)
        if os.path.isdir(d):
            ts_list.append(file)
        
    tomo_name_list = [''] * len(table_tomon)
    
    # extract ts naming convention and TS number	
    for tomo_name in ts_list:
        ts_string=re.split('(\d+)',tomo_name)
        while('' in ts_string) :
            ts_string.remove('')
        if len(ts_string) > 2:
            sys.exit('Check the folder names in tilt_series_directory. Should only contain folders with variations of the ts_01 TS_15 etc. naming convention')
        tomo_num = int(ts_string[1])
	
	# assign tomo_name to correct particles
        tomon_indices = np.asarray(np.where(table_tomon == tomo_num))[0]

        for i in tomon_indices:
            tomo_name_list[i] = tomo_name
    return tomo_name_list

