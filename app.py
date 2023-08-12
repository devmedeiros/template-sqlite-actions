# Import librarys
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	page_title='SQLite Actions Viz',  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

# Create db connection
engine = create_engine('sqlite:///data.db')

# Load the dataframe
df = pd.read_sql('''select people, strftime('%Y-%m-%d', load_date) as "load_date", avg("values") "values" from data group by 1, 2;''', con=engine)
df.load_date = pd.to_datetime(df['load_date'], format='%Y-%m-%d').dt.strftime("%Y-%m-%d")
max_date = max(df.load_date)
df = df.pivot(index='load_date', columns='people', values='values')

st.title('🎈 Template SQLite Actions Visualizations')

st.header('Line Chart for the Data')
st.line_chart(df)
st.caption(f'The last data arrived at: {max_date}')