
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="BO Engagement Tracker", layout="wide")
st.title("📞 BO Engagement Tracker")

uploaded_file = st.file_uploader("Upload Engagement Excel File", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="Engagement Tracker")
    summary_df = pd.read_excel(uploaded_file, sheet_name="PA Performance Summary")
    script_df = pd.read_excel(uploaded_file, sheet_name="BO Call Script")

    st.sidebar.header("🔍 Filters")
    selected_pa = st.sidebar.multiselect("Select PA(s)", options=df["PA Name"].unique(), default=df["PA Name"].unique())
    selected_bo = st.sidebar.multiselect("Select BO(s)", options=df["Bus Operator"].unique(), default=df["Bus Operator"].unique())
    selected_date = st.sidebar.date_input("Select Date Range", [])

    # Filter data
    df_filtered = df[df["PA Name"].isin(selected_pa) & df["Bus Operator"].isin(selected_bo)]
    if len(selected_date) == 2:
        df_filtered = df_filtered[
            (pd.to_datetime(df_filtered["Date"]) >= pd.to_datetime(selected_date[0])) &
            (pd.to_datetime(df_filtered["Date"]) <= pd.to_datetime(selected_date[1]))
        ]

    st.subheader("Filtered Engagement Tracker")
    st.dataframe(df_filtered)

    st.subheader("📊 Summary Charts")

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(df_filtered, x="PA Name", title="Interactions per PA")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.histogram(df_filtered[df_filtered["Accepted"] == "Yes"], x="PA Name", title="Accepted Suggestions per PA", color="Accepted")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📈 GMV Impact by PA")
    gmv_df = df_filtered.groupby("PA Name")["Estimated GMV Impact"].sum().reset_index()
    fig3 = px.bar(gmv_df, x="PA Name", y="Estimated GMV Impact", title="Total GMV Impact")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📋 PA Performance Summary")
    st.dataframe(summary_df)

    st.subheader("📞 BO Call Script Template")
    st.table(script_df)

else:
    st.info("Please upload the BO_Engagement_Report.xlsx file to begin.")

    st.subheader("📤 Export Filtered Data")
    export_button = st.download_button(
        label="Download Filtered Data as CSV",
        data=df_filtered.to_csv(index=False).encode("utf-8"),
        file_name="filtered_bo_engagement_data.csv",
        mime="text/csv"
    )
