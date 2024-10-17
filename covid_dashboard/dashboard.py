import pandas as pd
import streamlit as st
import plotly.express as px

# File paths
country_wise_latest_path = r"C:\Users\prade\OneDrive\Desktop\project2\archive\country_wise_latest.csv"
covid_19_clean_complete_path = r"C:\Users\prade\OneDrive\Desktop\project2\archive\covid_19_clean_complete.csv"
day_wise_path = r"C:\Users\prade\OneDrive\Desktop\project2\archive\day_wise.csv"
full_grouped_path = r"C:\Users\prade\OneDrive\Desktop\project2\archive\full_grouped.csv"
usa_county_wise_path = r"C:\Users\prade\OneDrive\Desktop\project2\archive\usa_county_wise.csv"
worldometer_data_path = r"C:\Users\prade\OneDrive\Desktop\project2\archive\worldometer_data.csv"

# Load datasets with caching
@st.cache_data
def load_data():
    country_wise_latest = pd.read_csv(country_wise_latest_path)
    covid_19_clean_complete = pd.read_csv(covid_19_clean_complete_path)
    day_wise = pd.read_csv(day_wise_path)
    full_grouped = pd.read_csv(full_grouped_path)
    usa_county_wise = pd.read_csv(usa_county_wise_path)
    worldometer_data = pd.read_csv(worldometer_data_path)
    return country_wise_latest, covid_19_clean_complete, day_wise, full_grouped, usa_county_wise, worldometer_data

country_wise_latest, covid_19_clean_complete, day_wise, full_grouped, usa_county_wise, worldometer_data = load_data()

# Streamlit app
st.title("COVID-19 Dashboard")
st.markdown("### Analyzing COVID-19 Data Globally")

# Country selection
countries = country_wise_latest['Country/Region'].unique()
default_country = 'India'  # Set India as the default country
selected_country = st.selectbox("Select a country:", countries, index=list(countries).index(default_country))

# Latest data for selected country
latest_data = country_wise_latest[country_wise_latest['Country/Region'] == selected_country].iloc[0]

st.subheader(f"Latest Data for {selected_country}")
st.write(f"**Confirmed Cases:** {latest_data['Confirmed']}")
st.write(f"**Deaths:** {latest_data['Deaths']}")
st.write(f"**Recovered:** {latest_data['Recovered']}")
st.write(f"**Active Cases:** {latest_data['Active']}")
st.write(f"**New Cases:** {latest_data['New cases']}")
st.write(f"**New Deaths:** {latest_data['New deaths']}")

# Fetch historical data for the selected country
st.subheader("Historical Data")
country_historical_data = covid_19_clean_complete[covid_19_clean_complete['Country/Region'] == selected_country]
if not country_historical_data.empty:
    country_historical_data['Date'] = pd.to_datetime(country_historical_data['Date'])

    # Calculate new cases if the column is not present
    if 'New cases' not in country_historical_data.columns:
        country_historical_data['New cases'] = country_historical_data['Confirmed'].diff().fillna(0).astype(int)

    # Plot historical confirmed cases over time
    fig_confirmed = px.line(country_historical_data, x='Date', y='Confirmed', title=f'COVID-19 Confirmed Cases Over Time in {selected_country}',
                             labels={'Date': 'Date', 'value': 'Number of Cases'}, line_shape='linear')
    fig_confirmed.update_traces(line=dict(color='blue'))
    fig_confirmed.update_layout(xaxis_title='Date', yaxis_title='Number of Cases', template='plotly_dark')
    st.plotly_chart(fig_confirmed)

    # Plot daily new cases
    new_cases = country_historical_data[['Date', 'New cases']].copy()
    new_cases.set_index('Date', inplace=True)

    fig_new_cases = px.line(new_cases, x=new_cases.index, y='New cases', title='Daily New COVID-19 Cases',
                             labels={'Date': 'Date', 'New cases': 'Number of New Cases'}, line_shape='linear')
    fig_new_cases.update_traces(line=dict(color='orange'))
    fig_new_cases.update_layout(xaxis_title='Date', yaxis_title='Number of New Cases', template='plotly_dark')
    st.plotly_chart(fig_new_cases)
else:
    st.write("No historical data available for this country.")

# Additional analysis and visualizations
st.subheader("Global Analysis")
st.write("### Worldwide COVID-19 Statistics")

total_confirmed = country_wise_latest['Confirmed'].sum()
total_deaths = country_wise_latest['Deaths'].sum()
total_recovered = country_wise_latest['Recovered'].sum()
total_active = country_wise_latest['Active'].sum()

st.write(f"**Total Confirmed Cases Globally:** {total_confirmed}")
st.write(f"**Total Deaths Globally:** {total_deaths}")
st.write(f"**Total Recovered Globally:** {total_recovered}")
st.write(f"**Total Active Cases Globally:** {total_active}")

# Pie chart for the distribution of confirmed cases by country
fig_pie = px.pie(country_wise_latest, values='Confirmed', names='Country/Region', title='Distribution of Confirmed Cases by Country',
                 color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig_pie)

# Line chart for global new cases over time
global_new_cases = day_wise[['Date', 'New cases']].groupby('Date').sum().reset_index()
global_new_cases['Date'] = pd.to_datetime(global_new_cases['Date'])

fig_global_new_cases = px.line(global_new_cases, x='Date', y='New cases', title='Global Daily New COVID-19 Cases',
                                labels={'Date': 'Date', 'New cases': 'Number of New Cases'}, line_shape='linear')
fig_global_new_cases.update_traces(line=dict(color='red'))  # Change line color
fig_global_new_cases.update_layout(xaxis_title='Date', yaxis_title='Number of New Cases', template='plotly_dark')
st.plotly_chart(fig_global_new_cases)

# Top 10 countries with more confirmed cases
st.subheader("Top 10 Countries with Highest Confirmed Cases")
top_confirmed = country_wise_latest.nlargest(10, 'Confirmed')
fig_top_confirmed = px.bar(top_confirmed, x='Country/Region', y='Confirmed',
                            title='Top 10 Countries with Highest Confirmed Cases',
                            labels={'Country/Region': 'Country', 'Confirmed': 'Confirmed Cases'},
                            color='Confirmed', color_continuous_scale=px.colors.sequential.Viridis)  # Color scale for bars
fig_top_confirmed.update_layout(template='plotly_dark')
st.plotly_chart(fig_top_confirmed)

# Top 10 countries with highest recoveries
st.subheader("Top 10 Countries with Highest Recoveries")
top_recovered = country_wise_latest.nlargest(10, 'Recovered')
fig_top_recovered = px.bar(top_recovered, x='Country/Region', y='Recovered',
                            title='Top 10 Countries with Highest Recoveries',
                            labels={'Country/Region': 'Country', 'Recovered': 'Recovered Cases'},
                            color='Recovered', color_continuous_scale=px.colors.sequential.Inferno)  # Different color scale
fig_top_recovered.update_layout(template='plotly_dark')
st.plotly_chart(fig_top_recovered)

# Top 10 countries with highest deaths
st.subheader("Top 10 Countries with Highest Deaths")
top_deaths = country_wise_latest.nlargest(10, 'Deaths')
fig_top_deaths = px.bar(top_deaths, x='Country/Region', y='Deaths',
                        title='Top 10 Countries with Highest Deaths',
                        labels={'Country/Region': 'Country', 'Deaths': 'Death Cases'},
                        color='Deaths', color_continuous_scale=px.colors.sequential.Magma)  # Another color scale
fig_top_deaths.update_layout(template='plotly_dark')
st.plotly_chart(fig_top_deaths)

# Top 10 countries with highest active cases
# Top 10 countries with highest active cases
st.subheader("Top 10 Countries with Highest Active Cases")
# Checking if the 'Active' column has data
if 'Active' in country_wise_latest.columns and country_wise_latest['Active'].notna().any():
    top_active = country_wise_latest.nlargest(10, 'Active')
    
    # Verify the data being used for the chart
    st.write("Data for Top 10 Countries with Highest Active Cases:")
    st.write(top_active)
    
    # Plotting the graph
    fig_top_active = px.bar(top_active, x='Country/Region', y='Active',
                             title='Top 10 Countries with Highest Active Cases',
                             labels={'Country/Region': 'Country', 'Active': 'Active Cases'},
                             color='Active', color_continuous_scale=px.colors.sequential.Cividis)  # Choose a color scale
    fig_top_active.update_layout(template='plotly_dark')
    st.plotly_chart(fig_top_active)
else:
    st.write("No data available for Active cases.")
 
