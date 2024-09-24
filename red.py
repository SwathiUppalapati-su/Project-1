import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px 
import pandas as pd
import pymysql
import time

# kerala bus

lists_k=[]
df_k=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_k.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_AP=[]
df_AP=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_AP.csv")
for i,r in df_AP.iterrows():
    lists_AP.append(r["Route_name"])

#Telangana bus
lists_T=[]
df_T=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Goa bus
lists_G=[]
df_G=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_G.csv")
for i,r in df_G.iterrows():
    lists_G.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


# South bengal bus 
lists_S=[]
df_S=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_S.csv")
for i,r in df_S.iterrows():
    lists_S.append(r["Route_name"])

# Haryana bus
lists_H=[]
df_H=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Chandigar bus
lists_C=[]
df_C=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_C.csv")
for i,r in df_C.iterrows():
    lists_C.append(r["Route_name"])

#PUNJAB bus
lists_P=[]
df_P=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_P.csv")
for i,r in df_P.iterrows():
    lists_P.append(r["Route_name"])

#UTTAR PRADESH bus
lists_U=[]
df_U=pd.read_csv("C:/Users/phani/Downloads/capstone/redbus/df_U.csv")
for i,r in df_U.iterrows():
    lists_U.append(r["Route_name"])

# SETUP STREAMLIT PAGE
slt.set_page_config(layout="wide")

web = option_menu(menu_title="Redbus",
                  options=["Home", "States and Routes"],
                  icons=["house", "info-circle"],
                  orientation="centered")

# Home page setting
if web == "Home":
    slt.image("C:/Users/phani/OneDrive/Desktop/bus.jpg", width=300)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":red[Domain:] Transportation")
    slt.subheader(":red[Objective:]")
    slt.markdown("""
    The objective of the Redbus project involving data scraping with Selenium and filtering with Streamlit is to create a comprehensive solution for collecting, analyzing, and visualizing bus travel data from the Redbus platform. Here are the key components and objectives:
    - Use Selenium to scrape data from the Redbus website.
    - Use Pandas for data processing.
    - Use Streamlit to provide an interactive UI for filtering the data.
    - Visualize bus data with charts and tables using Plotly.
    """)
    slt.subheader(":red[Overview:]")
    slt.markdown("""
    The objective of this Redbus project is to create a solution for collecting, analyzing, and visualizing bus travel data from the Redbus platform. The key components are:
    - Scraping data using Selenium.
    - Processing the scraped data with Pandas.
    - Interactive filtering with Streamlit.
    - Visualizing bus data with charts and tables using Plotly.
    """)

    # Overview of the Technologies
    
    slt.markdown("""
    **Selenium** is a tool for automating web browsers, commonly used for:
    - Web testing automation.
    - Web scraping for dynamic websites.
    - Cross-browser automation.

    Key Components:
    - Selenium WebDriver for browser control.
    - Selenium IDE for recording tests.
    - Selenium Grid for parallel testing across browsers.
    """)

    slt.markdown("""
    **Pandas** is a powerful data manipulation library used for:
    - Data wrangling and analysis.
    - Handling structured data using DataFrames.
    """)

    slt.markdown("""
    **MySQL** is an open-source relational database management system, often used for:
    - Storing structured data in tables.
    - Performing queries with SQL for data retrieval and manipulation.
    """)

    slt.markdown("""
    **Streamlit** is a user-friendly framework for creating interactive data visualization and analysis applications.
    """)
    
    
    slt.subheader(":red[Skills used in this project:]")
    slt.markdown("Python, Selenium, Pandas, MySQL, mysql-connector-python, Streamlit.")
    slt.subheader(":red[Developed-by:] Swathi Uppalapati")

# States and Routes page setting
if web == "States and Routes":
    slt.write(web)
    S = slt.selectbox("Lists of States", ["Kerala", "AndhraPradesh", "Telangana", "Goa", "Rajastan", 
                                          "SouthBengal", "Haryana", "chandigar", "Uttar Pradesh", "punjab"])
    
    col1, col2 = slt.columns(2)
    with col1:
        select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
    TIME = slt.time_input("Select the time")
    
     #Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("List of routes",lists_k)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes9 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

    # Andhra Pradesh bus fare filtering
    if S=="Andhra pradesh":
        A=slt.selectbox("list of routes",lists_AP)

        def type_and_fare_AP(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM  bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AP}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_AP(select_type, select_fare)
        slt.dataframe(df_result)
          

    # Telangana bus fare filtering
    if S=="Telangana":
        T=slt.selectbox("list of routes",lists_T)

        def type_and_fare_T(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_type, select_fare)
        slt.dataframe(df_result)

    # Goa bus fare filtering
    if S=="Goa":
        G=slt.selectbox("list of routes",lists_G)

        def type_and_fare_G(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM  bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{G}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_G(select_type, select_fare)
        slt.dataframe(df_result)

    # Rajastan bus fare filtering
    if S=="Rajastan":
        R=slt.selectbox("list of routes",lists_R)

        def type_and_fare_R(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM  bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_R(select_type, select_fare)
        slt.dataframe(df_result)
          

    # South Bengal bus fare filtering       
    if S=="South Bengal":
        SB=slt.selectbox("list of rotes",lists_S)

        def type_and_fare_S(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM  bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{S}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_SB(select_type, select_fare)
        slt.dataframe(df_result)
    
    # Haryana bus fare filtering
    if S=="Haryana":
        H=slt.selectbox("list of rotes",lists_H)

        def type_and_fare_H(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM  bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_H(select_type, select_fare)
        slt.dataframe(df_result)


    # Chandigar bus fare filtering
    if S=="chandigar":
        C=slt.selectbox("list of rotes",lists_C)

        def type_and_fare_C(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{C}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_C(select_type, select_fare)
        slt.dataframe(df_result)

    # Uttar Pradesh bus fare filtering
    if S=="Uttar Pradesh":
        U=slt.selectbox("list of rotes",lists_U)

        def type_and_fare_U(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM  bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{U}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_U(select_type, select_fare)
        slt.dataframe(df_result)

    # punjab bus fare filtering
    if S=="punjab":
        P=slt.selectbox("list of rotes",lists_P)

        def type_and_fare_P(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="root", database="SQLPYTHON2")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes9
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{P}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time  DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_P(select_type, select_fare)
        slt.dataframe(df_result)


