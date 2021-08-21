from google.cloud import bigquery

"""
BigQuery
    - web service that lets you apply SQL to huge datasets
"""

# Client object
client = bigquery.Client()

# reference to the dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# api request to fetch the dataset
dataset = client.get_dataset(dataset_ref)

# all datasets are just collections of tables (rows & columns)

# create a list of the tables in the dataset
tables = list(client.list_tables(dataset))

# Print names of all tables in the dataset (there are four!)
for table in tables:
    print(table.table_id)

# construct a reference to the "full" table
table_ref = dataset_ref.table("full")

# api request to fetch table
table = client.get_table(table_ref)

# Table Schema
"""
schema: 
    - structure of a table 
"""

table.schema
"""
[SchemaField('title', 'STRING', 'NULLABLE', 'Story title', (), None),
 SchemaField('url', 'STRING', 'NULLABLE', 'Story url', (), None),
 SchemaField('text', 'STRING', 'NULLABLE', 'Story or comment text', (), None),
 SchemaField('dead', 'BOOLEAN', 'NULLABLE', 'Is dead?', (), None),
 SchemaField('by', 'STRING', 'NULLABLE', "The username of the item's author.", (), None),
 SchemaField('score', 'INTEGER', 'NULLABLE', 'Story score', (), None),
 SchemaField('time', 'INTEGER', 'NULLABLE', 'Unix time', (), None),
 SchemaField('timestamp', 'TIMESTAMP', 'NULLABLE', 'Timestamp for the unix time', (), None),
 SchemaField('type', 'STRING', 'NULLABLE', 'Type of details (comment, comment_ranking, poll, story, job, pollopt)', (), None),
 SchemaField('id', 'INTEGER', 'NULLABLE', "The item's unique id.", (), None),
 SchemaField('parent', 'INTEGER', 'NULLABLE', 'Parent comment ID', (), None),
 SchemaField('descendants', 'INTEGER', 'NULLABLE', 'Number of story or poll descendants', (), None),
 SchemaField('ranking', 'INTEGER', 'NULLABLE', 'Comment ranking', (), None),
 SchemaField('deleted', 'BOOLEAN', 'NULLABLE', 'Is deleted?', (), None)]
"""


"""
Each SchemaField tells us about a specific column (which we also refer to as a field). In order, the information is:

The name of the column
The field type (or datatype) in the column
The mode of the column ('NULLABLE' means that a column allows NULL values, and is the default)
A description of the data in that column

The first field has the SchemaField:

SchemaField('by', 'string', 'NULLABLE', "The username of the item's author.",())

This tells us:

the field (or column) is called by,
the data in this field is strings,
NULL values are allowed, and
it contains the usernames corresponding to each item's author.
"""

"""
we can use list_rows() method to check x amount of lines in the full tbale to make sure it's right
* This returns a BigQuery RowIterator object that can quickly be converted into a pandas DataFrame obbject
by calling to_dataframe()
"""

# Preview the first five lines of the "full" table
client.list_rows(table, max_results=5).to_dataframe()

# Exercises
"""
1.
How many tables are in the Chicago Crime dataset?
tables = list(client.list_tables(dataset))
len(tables)
num_tables = 1
"""

"""
2.
How many columns in the crime table have TIMESTAMP data?

table_ref = dataset_ref.table("crime")
table = client.get_table(table_ref)
table.schema
num_timestamp_fields = 2
"""


"""
3.
If you wanted to create a map with a dot at the location of each crime, what are the names of the two fields you likely need to pull out of the crime table to plot the crimes on a map?
table_ref = dataset_ref.table("crime")
table = client.get_table(table_ref)
table.schema
fields_for_plotting = ['latitude', 'longitude'] 
Look at schema to see what the most relevant columns are
"""

