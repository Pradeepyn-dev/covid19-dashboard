# 🦠 COVID-19 Dashboard

This project is a **COVID-19 Dashboard** built using **Streamlit** and **Plotly**. It visualizes COVID-19 data globally, allowing users to analyze and compare COVID-19 statistics across different countries. 📊

## 🚀 Features
- View the latest COVID-19 data for any selected country 🌍
- Historical data visualization for confirmed cases and daily new cases 📈
- Global statistics overview for total confirmed, deaths, recovered, and active cases 🌐
- Top 10 countries with the highest confirmed, recovered, deaths, and active cases 📊
- Country comparison for COVID-19 cases 🏆
- Interactive heatmap for COVID-19 statistics across different countries 🗺️

## 📂 Project Structure
- `app.py`: The main file for running the Streamlit app
- `requirements.txt`: List of dependencies required to run the app
- `archive/`: Folder containing the CSV data files used in this project

## 📦 Requirements
- Python 3.7+
- Streamlit
- Plotly
- Pandas

## 📝 Installation and Setup
Follow these steps to get a local copy of the project and run the app:

1. **Clone the Repository** 📥
   ```bash
   git clone https://github.com/your-username/COVID-19-Dashboard.git
   cd COVID-19-Dashboard
   ```

2. **Create a Virtual Environment** 🐍  
   It's recommended to create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment** 🌱  
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies** 📦  
   Make sure you have Python installed. Then, install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App** ▶️  
   Start the Streamlit app using the command:
   ```bash
   streamlit run app.py
   ```
   The app will open in your default web browser.

6. **Explore the Dashboard** 🌐  
   - Select a country from the dropdown to see its latest COVID-19 statistics.
   - View historical data, global statistics, and compare data between countries.
   - Check the heatmap and explore the top 10 countries with the most cases.

## 🗂️ Folder Structure
```
COVID-19-Dashboard/
├── app.py                  # Main application file
├── requirements.txt        # Dependencies file
└── archive/                # Folder containing CSV data files
    ├── country_wise_latest.csv
    ├── covid_19_clean_complete.csv
    ├── day_wise.csv
    ├── full_grouped.csv
    ├── usa_county_wise.csv
    └── worldometer_data.csv
```

## 💡 How to Contribute
1. Fork the repository
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📊 Data Sources
The data used in this project comes from various sources and is updated regularly:
- [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
- [Worldometer](https://www.worldometers.info/coronavirus/)

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🌟 Acknowledgments
- Big thanks to the data providers for making COVID-19 data publicly available 🙌
- Special thanks to Streamlit and Plotly for providing great tools for data visualization 📈

Feel free to ⭐️ the repository if you find it helpful!

Happy coding! 🚀

This updated README now includes instructions on creating and activating a virtual environment, ensuring users have a smooth setup process.
