import click
import dynamotable
import starfile
import pandas as pd
from eulerangles import convert_eulers
from .utils import sanitise_m_starfile_name, find_tomo_name


def dynamo2relion(input_table_file, output_star_file, ts_directory, binning):
    # Read table file into dataframe
    table = dynamotable.read(input_table_file)
    
    # Prep data for star file in dict
    data = {}

    # extract xyz into dict with relion style headings  convert binned coordinates to unbinned coordinates
    for axis in ('x', 'y', 'z'):
        heading = f'rlnCoordinate{axis.upper()}'
        shift_axis = f'd{axis}'
        data[heading] = (table[axis] + table[shift_axis]) * int(binning)
     
    # extract and convert eulerangles
    eulers_dynamo = table[['tdrot', 'tilt', 'narot']].to_numpy()
    eulers_warp = convert_eulers(eulers_dynamo,
                                 source_meta='dynamo',
                                 target_meta='warp')
    data['rlnAngleRot'] = eulers_warp[:, 0]
    data['rlnAngleTilt'] = eulers_warp[:, 1]
    data['rlnAnglePsi'] = eulers_warp[:, 2]
    
    # look for ts names in ts_directory
    
    table_tomon = table['tomo'].to_numpy()
    data['rlnTomoName'] = find_tomo_name(table_tomon,ts_directory)
    
    # Keep track of individual objects within each tomogram with rlnObjectNumber (i.e. Dynamo table column 21)
    
    data['rlnObjectNumber'] = table['reg']

    # convert dict to dataframe
    df = pd.DataFrame.from_dict(data)

    # write out STAR file
    starfile.write(df, output_star_file, overwrite=True)

    # echo to console
    click.echo(
        f"Done! Converted '{input_table_file}' to RELION compatible STAR file '{output_star_file}'")

    return

@click.command()
@click.option('--input_table_file', '-i',
              prompt='Input Dynamo table file',
              type=click.Path(),
              required=True)
@click.option('--output_star_file', '-o',
              prompt='Output STAR file',
              type=click.Path(),
              required=True)
@click.option('--ts_directory', '-ts',
              prompt='Path to directory containing TS folders',
              type=click.Path(),
              required=True)
@click.option('--binning', '-bi',
              prompt='Binning level of Dynamo table (enter 1 for unbinned, binning is done using IMOD convention)',
              type=click.Path(),
              required=True)
	      
def cli(input_table_file, output_star_file, ts_directory, binning):
    dynamo2relion(input_table_file, output_star_file, ts_directory, binning)
