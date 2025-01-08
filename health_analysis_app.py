import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title("Global Health Metrics Analyzer")
st.write("Upload an Excel file to analyze trends in global health metrics like life expectancy, healthcare expenditure, and disease rates.")

# File upload
uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])

if uploaded_file:
    try:
        # Load the data
        data = pd.read_excel(uploaded_file)

        # Display dataset
        st.subheader("Uploaded Data")
        st.write(data.head())

        # Check for required columns
        required_columns = ['Country/Region', 'Year', 'Life Expectancy', 'Healthcare Expenditure (% of GDP)', 'Disease Rates']
        if not all(col in data.columns for col in required_columns):
            st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
        else:
            st.success("Data successfully uploaded and validated!")

            # Trend Analysis
            st.subheader("Trend Analysis")
            country = st.selectbox("Select a Country/Region", options=data['Country/Region'].unique())

            # Filter data for the selected country
            country_data = data[data['Country/Region'] == country]

            # Line plot for trends over time
            fig, ax = plt.subplots()
            sns.lineplot(x='Year', y='Life Expectancy', data=country_data, label='Life Expectancy', ax=ax)
            sns.lineplot(x='Year', y='Healthcare Expenditure (% of GDP)', data=country_data, label='Healthcare Expenditure (% of GDP)', ax=ax)
            ax.set_title(f"Trends for {country}")
            ax.legend()
            st.pyplot(fig)

            # Correlation Analysis
            st.subheader("Correlation Analysis")
            corr = data[['Life Expectancy', 'Healthcare Expenditure (% of GDP)', 'Disease Rates']].corr()
            st.write("Correlation Matrix:")
            st.write(corr)

            # Heatmap of correlations
            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            ax.set_title("Correlation Heatmap")
            st.pyplot(fig)

            # Insights
            st.subheader("Insights and Recommendations")
            st.write("Key trends and correlations identified from the analysis will appear here.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.write("\n\n**Note**: Deploy this app on Netlify or similar platforms. Ensure required dependencies are installed.")
