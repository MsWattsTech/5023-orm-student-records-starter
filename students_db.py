# Import sqlalchemy function required to write to database and Classes for defining table columns
from sqlalchemy import create_engine, Column, Integer, Text, Boolean
# Import functions from SQLAlchemy ORM for defining entities and managing connection to SQLite database
from sqlalchemy.orm import declarative_base, sessionmaker
# The following imports are used for printing the records from the database in the terminal
from sqlalchemy.inspection import inspect
from prettytable import PrettyTable

# Connects SQLAlchemy to a records.db SQLite dabase, creating it if it doesn't already exist
engine = create_engine('sqlite:///records.db', echo=True)
# Creates a Base class, which our entity (Student) will inherit from
Base = declarative_base()

# Defines a class for our Student entity, with relevant columns
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    english_mark = Column(Integer)
    mathematics_mark = Column(Integer)
     # TODO: Add column for students' mathematics marks
    science_mark = Column(Integer)
    does_homework = Column(Boolean)
    stays_on_task = Column(Boolean)
    # TODO: Add column for students' stays on task behaviour
    

# This deletes all data in the records.db database, so that we are starting from scratch each time
Base.metadata.drop_all(engine)
# Create the defined class (Student) as a table in the SQLite database file
Base.metadata.create_all(engine)

# Creates a connection session with the SQLite database, so we can read and write to it
Session = sessionmaker(bind=engine)
session = Session()

# Creates a Student object for a student named Jack
jack = Student (
    name = 'Jack',
    english_mark = 90,
    science_mark = 90,
    mathematics_mark = 70,
    # TODO: Add a value for mathematics mark, once you have added that column
    does_homework = True,
    stays_on_task = True,
    # TODO: Add a value for stays on task behaviour, once you have added that column
)
session.add(jack)

# Creates a Student object for a student named Dom
dom = Student (
    name = 'Dom',
    english_mark = 80,
    science_mark = 80,
    mathematics_mark = 90,
    # TODO: Add a value for mathematics mark, once you have added that column
    does_homework = False,
    stays_on_task = True,
    # TODO: Add a value for stays on task behaviour, once you have added that column

)
session.add(dom)

 # TODO: Add code to add another student here
lily = Student (
    name = 'Lily',
    english_mark = 91,
    science_mark = 92,
    mathematics_mark = 93,
    # TODO: Add a value for mathematics mark, once you have added that column
    does_homework = True,
    stays_on_task = True,
    # TODO: Add a value for stays on task behaviour, once you have added that column

)
session.add(lily)
# The changes are committed (saved in the underlying database - records.db)
session.commit()

'''
    The code below prints out a table of the records in the Student table, using the prettytable module.
    You will not need to modify this part of the code, it can stay the same.
    I have added some comments for this part but do not worry if you don't understand all the lines.
    We are unlikely to use code like this in future weeks.
'''

# This creates a list of the column names on the Student class (id, name, ... and so on)
columns = [column.name for column in inspect(Student).c]

# These lines create a PrettyTable object for displaying records, using the column names as headings
display_table = PrettyTable()
display_table.field_names = columns

# The records from the student table are retrieved and put in an Iterable (essentially a list)
rows = session.query(Student).all()

# These lines iterate through each student record and add their details to the PrettyTable object
for row in rows:
    row_data = []
    for column in columns:
        row_data.append(getattr(row, column))
    display_table.add_row(row_data)

# Finally, the details for each record in the student table are printed out
print('\n\nThe students in the database are shown in the table below:')
print(display_table)