from bs4 import BeautifulSoup
import requests

url = "https://www.datacamp.com/courses/introduction-to-relational-databases-in-python"

text = requests.get(url).text

soup = BeautifulSoup(text, 'lxml')
tag = soup.findAll('h5')
tag
sub_list =[i.text for i in tag]
sub_list= [
 'Introduction to Databases',
 'Relational Model',
 'Connecting to your Database',
 'Engines and Connection Strings',
 'Autoloading Tables from a Database',
 'Viewing Table Details',
 'Introduction to SQL',
 'Selecting data from a Table: raw SQL',
 'Selecting data from a Table with SQLAlchemy',
 'Handling a ResultSet',
 'Congratulations!',
 'Filtering and Targeting Data',
 'Connecting to a PostgreSQL Database',
 'Filter data selected from a Table - Simple',
 'Filter data selected from a Table - Expressions',
 'Filter data selected from a Table - Advanced',
 'Overview of Ordering',
 'Ordering by a Single Column',
 'Ordering in Descending Order by a Single Column',
 'Ordering by Multiple Columns',
 'Counting, Summing and Grouping Data',
 'Counting Distinct Data',
 'Count of Records by State',
 'Determining the Population Sum by State',
 "Let's use Pandas and Matplotlib to visualize our Data",
 'SQLAlchemy ResultsProxy and Pandas Dataframes',
 'From SQLAlchemy results to a Graph',
 'Calculating Values in a Query',
 'Connecting to a MySQL Database',
 'Calculating a Difference between Two Columns',
 'Determining the Overall Percentage of Females',
 'SQL Relationships',
 'Automatic Joins with an Established Relationship',
 'Joins',
 'More Practice with Joins',
 'Working with Hierarchical Tables',
 'Using alias to handle same table joined queries',
 'Leveraging Functions and Group_bys with Hierarchical Data',
 'Dealing with Large ResultSets',
 'Working on Blocks of Records',
 'Creating Databases and Tables',
 'Creating Tables with SQLAlchemy',
 'Constraints and Data Defaults',
 'Inserting Data into a Table',
 'Inserting a single row with an insert() statement',
 'Inserting Multiple Records at Once',
 'Loading a CSV into a Table',
 'Updating Data in a Database',
 'Updating individual records',
 'Updating Multiple Records',
 'Correlated Updates',
 'Removing Data From a Database',
 'Deleting all the records from a table',
 'Deleting specific records',
 'Deleting a Table Completely',
 'Census Case Study',
 'Setup the Engine and MetaData',
 'Create the Table to the Database',
 'Populating the Database',
 'Reading the Data from the CSV',
 'Load Data from a list into the Table',
 'Example Queries',
 'Build a Query to Determine the Average Age by Population',
 'Build a Query to Determine the Percentage of Population by Gender and State',
 'Build a Query to Determine the Difference by State from the 2000 and 2008 Censuses',
 'Congratulations']

def prettify(a):
    s = ''
    for i in a:

        s = s+'* ['+i+'](#'+ ''.join([k[0] for k in i.split(' ')])+')'+'\n'
    print(s)


prettify(sub_list)

def markdowner(mylist):
    s1 = "###"
    s2 = "<p id = '"
    s3 = "'><p>\n"
    l1 = [s1+i for i in sub_list]
    l2 = [s1+''.join([k[0] for k in i.split(' ')])+s2  for i in sub_list]
    list_of_lists = [list(elem) for elem in list(zip(l2, l1))]
    list_dict = [{"cell_type": "markdown","metadata": {},"source": i} for i in list_of_lists]
    print(list_dict)


markdowner(sub_list)
