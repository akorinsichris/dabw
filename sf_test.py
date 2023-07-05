import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Employee Details')

conn = snowflake.connector.connect(**streamlit.secrets["snowflake"])

# execute a query
cursor = conn.cursor()
cursor.execute("SELECT * FROM resource_data")
results = cursor.fetchall()

# Displat query results
for row in results:
  st.write(row)

# Close Snowflake connection
cursor.close()
conn.close()
