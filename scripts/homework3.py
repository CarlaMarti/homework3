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

    def _init_(self, df):
        """
        Aceptar un DataFrame (df) como argumento y asignarlo al atributo df del objeto.
        """
        self.df = df

    def filter_by_genre(self, genre):
        """
        Filter the DataFrame based on a specified genre.
        """
        return self.df[self.df["Genre"] == genre]
    
    def filter_by_year(self, year):
        """
        Filter the Dataset by a given minimum year.
        """
        return self.df[self.df["Year"] > int(year)] 


import os 
import click
import pandas as pd

@click.command(short_help='Parser to manage inputs for BooksDataset')#info
@click.option('-id','--input_data', required=True, help='Path to my input dataset')
@click.option('-o','--output', default="outputs", help="Folder to save all outputs")
@click.option('-f','--filtering', is_flag=True, help="Set a filtering or not")
@click.option('-g', "--genre", help="Set a genre (you have to write the genre like this: Action)")
@click.option('-y', "--year", help="Set a year (you have to write it like this: 2002)")
@click.option('-n', '--name', help = "Set a name to your result!")


#python scripts/homework3.py -id FilmGenreStats.csv


#python scripts/homework3.py -id FilmGenreStats.csv -o Results -f -g Action -y 2002

def main(input_data, output, filtering, genre, year, name):
    """
    Deal with the input data and send to other functions, in this case inside the class filter_data.
    """
    print("WE WILL BE WORKING WITH THE FOLLOWING DATASET:", input_data)
    print("\n\n\n")

    try:
        df = pd.read_csv(input_data, sep=',')
    except FileNotFoundError as e:
        raise FileNotFoundError(f"\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CAUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n FILE COULDN'T BE FOUND: {e}\n\n\n\n")

    #import pdb;pdb.set_trace()

    #used this debugger to know the names of the columns of a given dataframe, these were: df.columns
    # Index(['index', 'Genre', 'Year', 'Movies Released', 'Gross', 'Tickets Sold',
    #    'Inflation-Adjusted Gross', 'Top Movie', 'Top Movie Gross (That Year)',
    #    'Top Movie Inflation-Adjusted Gross (That Year)'],
    #    dtype='object')


    print("HERE YOU HAVE A SAMPLE!\n\n\n",df.sample())
    

    if not os.path.exists(output):              #if the directory output is not found, we will generate one called as the user said
        os.makedirs(output)
    
    df.to_csv(f'{output}/{name}.csv', index=None)
    #we save the file where we want (output) or it will save it in "outputs"




if __name__ == '__main__':
    print("\n\n\nTHIS IS WORKING!!\n\n\n")
    main()