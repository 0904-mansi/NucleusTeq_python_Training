import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import matplotlib.cm as cm
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio

import warnings
warnings.filterwarnings('ignore')
conn = sqlite3.connect("travel.sqlite")
cursor = conn.cursor()


cursor.execute("""select name from sqlite_master where type ='table';""")
print('List of tables present in the database')
table_list = [table[0] for table in cursor.fetchall()]
print(table_list)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)

def tables(table_name, conn):
    # iterating over each available table in the list
    for table in table_name:
        # storing the table into a dataframe by reading them using the read_sql_query
        df = pd.read_sql_query(f"""select * from {table}""", conn)
        # introducing a global variable
        globals()[table] = df
    return dict

table_names = ['aircrafts_data','boarding_passes','bookings','flights','seats','ticket_flights','tickets']
tables(table_names, conn)

airports_data = pd.read_sql_query("select * from airports_data", conn)
airports_data['airport_name'] = airports_data['airport_name'].apply(lambda x: json.loads(x)['en'])
airports_data['city'] = airports_data['city'].apply(lambda x: json.loads(x)['en'])
# airports_data



def main():
    st.subheader("Airlines Data Analysis for profit Maximization")
        # Set seaborn style
    sns.set_style('whitegrid')

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='model', y='range', data=aircrafts_data, palette='crest', color='purple', ax=ax)
    for container in ax.containers:
        ax.bar_label(container)

    # Customize plot
    plt.title('Airplane Models with Their Ranges')
    plt.xticks(rotation=45)

    # Display plot using st.pyplot()
    st.pyplot(fig)

    df = pd.read_sql_query("""select aircraft_code, count(*) as num_seats from seats
                        group by aircraft_code having num_seats >100""", conn)

    df.to_csv('aircraft_seats.csv')
    # Set seaborn style
    sns.set_style('whitegrid')

    # Create the plot
    st.subheader("Aircraft Codes vs Number of Seats")

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='aircraft_code', y='num_seats', data=df, palette='crest', ax=ax)
    for container in ax.containers:
        ax.bar_label(container)

    # Customize plot
    plt.title('Aircraft Codes vs Number of Seats')
    plt.xticks(rotation=45)

    # Display plot using st.pyplot()
    st.pyplot(fig)

    # Observation text
    observation_text = """
Utilized a line chart visualization to analyze the trend of ticket bookings and revenue earned.
The number of tickets booked showed a gradual increase from June 22nd to July 7th.
From July 8th until August, ticket bookings remained relatively stable with a noticeable peak in bookings on a single day.
The revenue earned by the company is closely correlated with the number of tickets booked.
The total revenue earned followed a similar trend throughout the analyzed time period.
Further exploration of the factors contributing to the peak in ticket bookings could help increase overall revenue and optimize operational strategies.
"""

    # Function to generate audio from text
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_bytes_io = BytesIO()
        tts.write_to_fp(audio_bytes_io)
        return audio_bytes_io

    # Button text
    button_text = "Listen Conclusion"

    # Button to play/pause audio
    button_clicked = st.button(button_text)

    # Play audio if button is clicked
    if button_clicked:
        audio_bytes_io = generate_audio(observation_text)
        st.audio(audio_bytes_io, format='audio/mp3', start_time=0)

        # Change button text to "Click to Pause"
        
    # Optionally, you can display the text in the app as well
    # st.text(observation_text)

    crafts = pd.read_sql("""SELECT aircraft_code, model
                        FROM aircrafts_data
                        where aircraft_code IN (319, 320, 321, 733, 763, 773);""", conn)
    tickets = pd.read_sql_query("""select * from tickets inner join bookings
                    on tickets.book_ref = bookings.book_ref""", conn)

    tickets['book_date'] = pd.to_datetime(tickets['book_date'])
    tickets['date'] = tickets['book_date'].dt.date
    tickets_count = tickets.groupby('date')[['date']].count()

    # Plotting
    plt.figure(figsize=(18, 6))
    plt.fill_between(tickets_count.index, tickets_count['date'], color=cm.get_cmap('crest')(0.5), alpha=0.3)
    plt.plot(tickets_count.index, tickets_count['date'], color=cm.get_cmap('crest')(0.5), linewidth=2, marker='o', markersize=8)
    plt.title('Number of Tickets Booked on Each Date', fontsize=30)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Number of Tickets', fontsize=20)
    plt.grid('b')

    # Display plot using st.pyplot()
    st.pyplot(plt)


    # Load bookings data
    bookings = pd.read_sql_query("select * from bookings", conn)

    # Convert 'book_date' to datetime and extract date
    bookings['book_date'] = pd.to_datetime(bookings['book_date'])
    bookings['date'] = bookings['book_date'].dt.date

    # Group by date and calculate total amount earned
    booking_amount = bookings.groupby('date')[['total_amount']].sum()

    # Plotting
    plt.figure(figsize=(18, 6))
    plt.fill_between(booking_amount.index, booking_amount['total_amount'], color=cm.get_cmap('crest')(0.5), alpha=0.3)
    plt.title('Total Amount Earned on Each Date', fontsize=30)
    plt.xlabel('Date', fontsize=20)
    plt.ylabel('Total Amount Earned', fontsize=20)
    plt.grid('b')

    # Display plot using st.pyplot()
    st.pyplot(plt)

    # Additionally, if you want to display both plots side by side, you can use st.pyplot() for the second plot as well:
    st.pyplot(plt)

        # Display class-wise average flight prices
    df = pd.read_csv('fare_avg_amount.csv')
    sns.set_style('whitegrid')
    fig, axes = plt.subplots(figsize=(12, 8))
    ax = sns.barplot(x='aircraft_code', y='avg(amount)', hue='fare_conditions', data=df, palette='crest')
    for container in ax.containers:
        ax.bar_label(container)
    plt.title('Class wise Average Flight Prices')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Display number of crafts by aircraft code
    # st.subheader('Number of Crafts by Aircraft Code')
    # sns.barplot(x='aircraft_code', y='model', data=crafts)
    # st.pyplot()

    occupancy_rate = pd.read_sql_query("""select a.aircraft_code,avg(a.seats_count) as booked_seats, b.num_seats, avg(a.seats_count)/b.num_seats as occupancy_rate from
                (select aircraft_code,flights.flight_id,count(*) as seats_count from boarding_passes
                    inner join flights
                    on boarding_passes.flight_id = flights.flight_id
                    group by aircraft_code,flights.flight_id) as a
                    inner join
                    (select aircraft_code,count(*) as num_seats from seats
                    group by aircraft_code) as b
                    on a.aircraft_code = b.aircraft_code group by a.aircraft_code""", conn
                  )
    
    total_revenue = pd.read_sql_query("""select aircraft_code,sum(amount) as total_revenue from ticket_flights
                        join flights on ticket_flights.flight_id = flights.flight_id
                        group by aircraft_code""", conn)



    # Display correlation between booked seats and occupancy rate
    sns.set_style('whitegrid')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(x="booked_seats", y="occupancy_rate", data=occupancy_rate, ax=ax)
    plt.title('Correlation between Booked Seats and Occupancy Rate')
    plt.xlabel('Booked Seats')
    plt.ylabel('Occupancy Rate')
    st.pyplot(fig)

    
        # Display occupancy rate and total revenue tables
    st.subheader('Occupancy Rate and Total Revenue Tables')
    st.write("Occupancy Rate Table:")
    st.dataframe(occupancy_rate)
    st.write("Total Revenue Table:")
    st.dataframe(total_revenue)

    # Additional calculations and display
    occupancy_rate['inc occupancy rate'] = occupancy_rate['occupancy_rate'] + occupancy_rate['occupancy_rate'] * 0.1
    occupancy_rate['inc Total Annual Turnover'] = (total_revenue['total_revenue'] / occupancy_rate['occupancy_rate']) * occupancy_rate['inc occupancy rate']
    st.subheader('Additional Calculations:')
    st.write(occupancy_rate)


    # Define the values
    current_turnover = 1000000  # Example current total annual turnover
    potential_occupancy_rate = 0.70  # Example potential occupancy rate after increase
    increase_in_occupancy_rate = 0.10  # Example increase in occupancy rate
    num_flights_per_year = 1000  # Example number of flights per year
    average_revenue_per_flight = 5000  # Example average revenue per flight

    # Calculate the potential increase in occupancy rate
    potential_occupancy_rate = potential_occupancy_rate + increase_in_occupancy_rate

    # Calculate the potential total annual turnover
    potential_turnover = num_flights_per_year * average_revenue_per_flight * potential_occupancy_rate

    # Calculate the increase in total annual turnover
    increase_in_turnover = potential_turnover - current_turnover

    # Display the results in the Streamlit interface
    st.title("Potential Increase in Total Annual Turnover")
    st.write("Current Total Annual Turnover:", current_turnover)
    st.write("Potential Total Annual Turnover with 10% Increase in Occupancy Rate:", potential_turnover)
    st.write("Increase in Total Annual Turnover:", increase_in_turnover)





if __name__ == "__main__":
    main()
