import os
#import numpy as np
import pandas as pd
import gzip
import shutil

#Creating the table 'Aliases'
def CreateTableAliases(titleAkas):
    print("creating table")
    aliasColumn=titleAkas[['titleId','ordering','title','region','language','types']]
    aliasColumn=aliasColumn.rename(columns={
    'titleId':'title_id',
    'isOrginalTitle':'is_original_title'
    })
    aliasColumn.to_csv('Aliases.tsv',na_rep=r'\N',sep='\t',index=False)

def CreateTableAliasTypes(titleAkas):
    print("\t creating alias types tables")
    aliasTypes = titleAkas[['titleId','ordering','types']]
    aliasTypes = aliasTypes.rename(columns = {
    'titleId':'title_id',
    'types':'type'
    })
    aliasTypes.to_csv('Alias_types.tsv',na_rep=r'\N',sep='\t',index=False)
 
def CreateTableAliasAttributes(titleAkas):
    print("\tcreating alias attributes")
    aliasAttributes=titleAkas[['titleId','ordering','attributes']]
    aliasAttributes=aliasAttributes.rename(columns={
    'titleId':'title_id',
    'attributes':'attribute'
    })
    aliasAttributes=aliasAttributes.dropna()
    aliasAttributes.to_csv('Alias_attributes.tsv', na_rep=r'\N',sep='\t',index=False)
 
def CreateTableDirectorsAndWriters(titleCrew):
    print("\t creating directors and writers table")
    tableDirectors=titleCrew[['tconst','directors']]
    tableWriters=titleCrew[['tconst','writers']]
    
    tableDirectors=tableDirectors.rename(columns={
    'tconst':'title_id',
    'directors':'name_id'
    })
    tableWriters=tableWriters.rename(columns={
    'tconst':'title_id',
    'writers':'name_id'
    })
    
    tableDirectors=tableDirectors.dropna()
    tableWriters=tableWriters.dropna()
    
    tableDirectors=tableDirectors.assign(name_id=tableDirectors.name_id.str.split(',')).explode('name_id').reset_index(drop=True)
    tableWriters=tableWriters.assign(name_id=tableWriters.name_id.str.split(',')).explode('name_id').reset_index(drop=True)
    
    tableDirectors.to_csv('Directors.tsv', na_rep=r'\N',sep='\t',index=False)
    tableWriters.to_csv('Writers.tsv',na_rep=r'\N',sep='\t',index=False)
    
def CreateTableEpisodeBelongsTo(titleEpisode):
    print("\t Creating Episode Belongs to table")
    episodeBelongsTo=titleEpisode.rename(columns={
    'tconst':'title_id',
    'parentTconst':'parent_tv_show_title_id',
    'seasonNumber':'season_number',
    'episodeNumber':'episode_number'
    })
    episodeBelongsTo.to_csv('Episode_belongs_to.tsv',na_rep=r'\N',sep='\t',index=False)

def CreateTableNames(nameBasics):
    print("\t Creating Names table")
    tableNames=nameBasics[['nconst','primaryName','birthYear','deathYear']]
    
    tableNames=tableNames.rename(columns={
    'nconst':'name_id',
    'primaryName':'name_',
    'birthYear':'birth_year',
    'dethYear':'death_year'
    })
    
    tableNames.to_csv('Names_.tsv',na_rep=r'\N',sep='\t',index=False)

def CreateTableNameWorkedAs(nameBasics):
    print("\t Creating name worked as table")
    nameWorkedAs=nameBasics[['nconst','primaryProfession']]
    nameWorkedAs=nameWorkedAs.dropna()
    nameWorkedAs=nameWorkedAs.rename(columns={
    'nconst':'name_id',
    'primaryProfession':'profession'
    })
    
    nameWorkedAs=nameWorkedAs.assign(profession=nameWorkedAs.profession.str.split(',')).explode('profession').reset_index(drop=True)
    nameWorkedAs.to_csv('Name_worked_as.tsv',na_rep=r'\N',sep='\t',index=False)

def CreateTableKnownFor(nameBasics):
    print("\t Creating table known for")
    knownFor=nameBasics[['nconst','knownForTitles']]
    knownFor=knownFor.dropna()
    knownFor=knownFor.rename(columns={
    'nconst':'name_id',
    'knownForTitles':'title_id'
    })
    
    knownFor=knownFor.assign(title_id=knownFor.title_id.str.split(',')).explode('title_id').reset_index(drop=True)
    
    knownFor.to_csv('Known_for.tsv',na_rep=r'\N',sep='\t',index=False)
    
def CreateTablePrincipals(titlePrincipals):
    print("\t Creating Principals table")
    tablePrincipals=titlePrincipals[['tconst','ordering','nconst','category','job']]
    
    tablePrincipals=tablePrincipals.rename(columns={
    'tconst':'title_id',
    'nconst':'name_id',
    'category':'job_category'
    })
    tablePrincipals.to_csv('Principals.tsv',na_rep=r'\N',sep='\t',index=False)
    
def CreateTableHadRole(titlePrincipals):
    print("\t Creating Had Role table")
    hadRole=titlePrincipals[['tconst','nconst','characters']]
    hadRole=hadRole.rename(columns={
    'tconst':'title_id',
    'nconst':'name_id',
    'characters':'role_'
    })
    hadRole=hadRole.dropna()
    hadRole['role_']=hadRole['role_'].str.replace('[\"\[\]]','',regex=True)
    hadRole['role_']=hadRole['role_'].str.replace('\\','|')
    hadRole=hadRole.assign(role_=hadRole.role_.str.split(',')).explode('role_').reset_index(drop=True)
    hadRole['role_']=hadRole['role_'].str.title()
    hadRole['role_']=hadRole['role_'].str.replace('^|$','',regex=True)
    hadRole.drop_duplicates(keep=False,inplace=True)
    hadRole.to_csv('Had_role.tsv',index=False,na_rep=r'\N',sep='\t')

def CreateTableTitles(titleBasics):
    print("\t Creating Title table")
    tableTitles=titleBasics[['tconst','titleType','primaryTitle','originalTitle','isAdult','startYear','endYear','runtimeMinutes']]
    tableTitles=tableTitles.rename(columns={
    'tconst':'title_id',
    'titleType':'title_type',
    'primaryTitle':'primary_title',
    'originalTitle':'original_title',
    'isAdult':'is_adult',
    'startYear':'start_year',
    'endYear':'end_year',
    'runtimeMinutes':'runtime_minutes'
    })
    tableTitles.to_csv('Title.tsv',na_rep=r'\N',sep='\t',index=False)

def CreateTableTitleGenres(titleBasics):
    print("\t Creating title genres table")
    titleGenres=titleBasics[['tconst','genres']]
    titleGenres=titleGenres.rename(columns={
    'tconst':'title_id',
    'genres':'genre'
    })
    titleGenres=titleGenres.dropna()
    titleGenres=titleGenres.assign(genre=titleGenres.genre.str.split(',')).explode('genre').reset_index(drop=True)
    titleGenres.to_csv('Title_genres.tsv',na_rep=r'\N',sep='\t',index=False)
    
def CreateTitleRating(titleRatings):
    print("\t Creating Title Rating table")
    titleRatings=titleRatings.rename(columns={
    'tconst':'title_id',
    'averageRating':'average_rating',
    'numVotes':'num_votes'
    })
    titleRatings.to_csv('Title_ratings.tsv',na_rep=r'\N',sep='\t',index=False)
    
dataPath_akas='C:/Users/maruthi/Desktop/SEM2/DMQL/Final_Project/DataSets/title.akas.tsv'
print('Scanning for data in: ',dataPath_akas,'\n')

titleAkas=pd.read_csv(os.path.join(dataPath_akas,'data.tsv'),
    dtype={'titleId':'str','ordering':'int','title':'str',
    'region':'str',
    'language':'str','types':'str','attributes':'str',
    'isOrginalTitle':'Int64'},
    sep='\t',na_values='\\N',quoting=3)
    
del titleAkas
dataPath_crew='C:/Users/maruthi/Desktop/SEM2/DMQL/Final_Project/DataSets/title.crew.tsv'
print('\n','Reading title.crew.tsv','\n')
titleCrew=pd.read_csv(os.path.join(dataPath_crew,'data.tsv'),sep='\t',na_values='\\N')
del titleCrew
dataPath_episode = 'C:/Users/maruthi/Desktop/SEM2/DMQL/Final_Project/DataSets/title.episode.tsv'
print('\n','Reading title.episode.tsv','\n')
titleEpisode=pd.read_csv(os.path.join(dataPath_episode,'data.tsv'),
dtype={'tconst':'str','parentTconst':'str','seasonNumber':'Int64', 'episodeNumber':'Int64'},sep='\t',na_values='\\N')
del titleEpisode
dataPath_name = 'C:/Users/maruthi/Desktop/SEM2/DMQL/Final_Project/DataSets/name.basics.tsv'
print('\n','Reading name.basics.tsv','\n')
nameBasics=pd.read_csv(os.path.join(dataPath_name,'data.tsv'),
    dtype={'nconst':'str','primaryName':'str','birthYear':'Int64','deathYear':'Int64','primaryProfession':'str','knownForTitles':'str'},
    sep='\t',na_values='\\N')
CreateTableNames(nameBasics)
CreateTableNameWorkedAs(nameBasics)
CreateTableKnownFor(nameBasics)

    

    