# Financial Data Analyzer

## Overview
Financial Data Analyzer is an AI-powered tool that simplifies stock trend analysis by predicting stock prices based on historical data. It enables users to select a stock and time span to receive structured price forecasts.

## Features
- AI-driven stock price predictions
- User-friendly Streamlit-based interface
- Support for multiple time spans (1 year, 3 years, 5 years)
- CSV data processing for trend analysis
- Readable and structured financial insights

## Tech Stack
- **Frontend:** Streamlit
- **AI Model:** OpenAI API (GPT-4o-mini)
- **Backend & Data Processing:** Python
- **Data Source:** CSV financial datasets

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/NikhilVarma2204/Financial-Data-Analyzer.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Financial-Data-Analyzer
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Select a stock from the dropdown.
2. Choose a time span (1 year, 3 years, 5 years).
3. Click **Analyze Data** to view predictions.

## Future Enhancements
- Expand stock coverage
- Integrate real-time data feeds
- Enhance AI models for improved accuracy
- Add interactive visualizations

