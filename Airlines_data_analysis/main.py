import warnings
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import json
from gtts import gTTS
import streamlit as st
from io import BytesIO

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

    # Conclusion for the first plot
    conclusion_text_1 = """
    Conclusion for the first plot goes here.
    """

    # Function to generate audio from text
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_bytes_io = BytesIO()
        tts.write_to_fp(audio_bytes_io)
        return audio_bytes_io

    # Button text
    button_text_1 = "Listen Conclusion 1"

    # Button to play/pause audio for conclusion 1
    button_clicked_1 = st.button(button_text_1)

    # Play audio if button is clicked for conclusion 1
    if button_clicked_1:
        audio_bytes_io = generate_audio(conclusion_text_1)
        st.audio(audio_bytes_io, format='audio/mp3', start_time=0)

    # Optionally, you can display the text in the app as well
    st.text(conclusion_text_1)

    # Your existing code for other plots...

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

    # Conclusion for the second plot
    conclusion_text_2 = """
    Conclusion for the second plot goes here.
    """

    # Button text for conclusion 2
    button_text_2 = "Listen Conclusion 2"

    # Button to play/pause audio for conclusion 2
    button_clicked_2 = st.button(button_text_2)

    # Play audio if button is clicked for conclusion 2
    if button_clicked_2:
        audio_bytes_io = generate_audio(conclusion_text_2)
        st.audio(audio_bytes_io, format='audio/mp3', start_time=0)

    # Optionally, you can display the text in the app as well
    st.text(conclusion_text_2)

    # Your existing code continues...

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

    # Conclusion for potential increase in total annual turnover
    potential_turnover_conclusion = f"""
    Potential Increase in Total Annual Turnover:
    Current Total Annual Turnover: {current_turnover}
    Potential Total Annual Turnover with 10% Increase in Occupancy Rate: {potential_turnover}
    Increase in Total Annual Turnover: {increase_in_turnover}
    """

    # Button text for potential turnover conclusion
    potential_turnover_button_text = "Listen Potential Turnover Conclusion"

    # Button to play/pause audio for potential turnover conclusion
    potential_turnover_button_clicked = st.button(potential_turnover_button_text)

    # Play audio if button is clicked for potential turnover conclusion
    if potential_turnover_button_clicked:
        audio_bytes_io = generate_audio(potential_turnover_conclusion)
        st.audio(audio_bytes_io, format='audio/mp3', start_time=0)

    # Optionally, you can display the text in the app as well
    st.text(potential_turnover_conclusion)

if __name__ == "__main__":
    main()
