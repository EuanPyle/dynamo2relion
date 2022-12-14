import dynamotable
import starfile
import typer

import pandas as pd

from eulerangles import convert_eulers
from pathlib import Path
from typing import Optional
from ._utils import IOConverter, find_tomo_name

cli = typer.Typer(add_completion=False)
@cli.command(name='dynamo2relion')
def dynamo2relion_cli(
    dynamo_table_file: Path = typer.Option(...),
    relion_star_file: Optional[Path] = typer.Option(None),
    tilt_series_directory: Path = typer.Option(...),
    binning: Optional[float] = typer.Option(1),
    ):
    """
    Converts a RELION STAR file into a Dynamo table file.
    
    Parameters
    ----------
    
    dynamo_table_file: Path
        Path to the Dynamo table to be converted.
    relion_star_file: Optional[Path] 
        Desired file name for the RELION star file.
    tilt_series_directory: Path
        Path to directory containing tilt series directories as specified under Requirements in README.md
    binning: Optional[float]
        Binning level of the coordinates in the Dynamo table (IMOD convention). Default = 1.
    """
    io_names = IOConverter(
        input_table = dynamo_table_file, 
        output_name = relion_star_file,
    )
    # Read table file into dataframe
    table = dynamotable.read(io_names.input_table)
    
    # Prep data for star file in dict
    data = {}

    # extract xyz into dict with relion style headings  convert binned coordinates to unbinned coordinates
    for axis in ('x', 'y', 'z'):
        heading = f'rlnCoordinate{axis.upper()}'
        shift_axis = f'd{axis}'
        data[heading] = (table[axis] + table[shift_axis]) * float(binning)
     
    # extract and convert eulerangles
    eulers_dynamo = table[['tdrot', 'tilt', 'narot']].to_numpy()
    eulers_warp = convert_eulers(eulers_dynamo,
                                 source_meta='dynamo',
                                 target_meta='warp')
    data['rlnAngleRot'] = eulers_warp[:, 0]
    data['rlnAngleTilt'] = eulers_warp[:, 1]
    data['rlnAnglePsi'] = eulers_warp[:, 2]
    
    # look for ts names in tilt_series_directory
    table_tomon = table['tomo'].to_numpy()
    data['rlnTomoName'] = find_tomo_name(table_tomon,tilt_series_directory)
    
    # Keep track of individual objects within each tomogram with rlnObjectNumber (i.e. Dynamo table column 21)
    data['rlnObjectNumber'] = table['reg']

    # convert dict to dataframe
    df = pd.DataFrame.from_dict(data)

    # write out STAR file
    starfile.write(df, io_names.output_name, overwrite=True)
    return
