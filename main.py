# Import librarys
import pandas as pd
import random
from sqlalchemy import create_engine
from datetime import datetime

# Create random data
people = ['Ana', 'Bob', 'Charles', 'Daiana']
values = [random.random(), random.random(), random.random(), random.random()]

# Create db connection
engine = create_engine('sqlite:///data.db')

# Create the dataframe
data = pd.DataFrame({'people': people, 'values': values, 'load_date': datetime.now()})

# Save the dataframe
data.to_sql('data', if_exists='append', con=engine, index=False)