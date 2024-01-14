# HOMEWORK:

# Download dataset FilmGenreStats from the Moodle

# Let’s create a script within our folder that is connected to Github. This script should have:

        # - Classes
        # - Click
        # - Try & Except
        # - Maybe some import pdb;pdb.set_trace()
        
# Every meaningful step we take should correspond with a commit

"""
Script of practice 2 of making updates in GitHub
"""

class filter_data:
    """
    Class to filter data by year and genre.
    """


import os 
import click
import pandas as pd

@click.command(short_help='Parser to manage inputs for BooksDataset')#info
@click.option('-id','--input_data', required=True, help='Path to my input dataset')
@click.option('-o','--output', default="outputs", help="Folder to save all outputs")
@click.option('-f','--filtering', is_flag=True, help="Set a filtering or not")
@click.option("-g", "--genre", help="Set a genre (you have to write the genre like this: Action)", required=True)
@click.option("-y", "--year", help="Set a year (you have to write it like this: 2002)", required=True)

#python scripts/homework3.py -id FilmGenreStats.csv


#python scripts/homework3.py -id FilmGenreStats.csv -o Results -f -g Action -y 2002

def main():
    """
    Deal with the input data and send to other functions, in this case inside the class filter_data.
    """



if __name__ == '__main__':
    print("\n\n\nTHIS IS WORKING!!\n\n\n")
    main()