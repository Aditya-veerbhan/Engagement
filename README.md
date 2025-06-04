
# 📞 BO Engagement Tracker – Streamlit App

This Streamlit-based dashboard enables Pricing Analyst teams to track, visualize, and analyze daily interactions with Key Bus Operators (BOs). It includes filtering tools, performance summaries, visual charts, and exportable insights to drive data-backed decision-making.

---

## 🔧 Features

- ✅ Upload engagement reports in `.xlsx` format
- 🔍 Filter by **Pricing Analyst**, **Bus Operator**, and **Date Range**
- 📊 Visualize:
  - Total interactions per PA
  - Accepted suggestions
  - Estimated GMV impact
- 📋 View PA-wise performance summary
- 📞 Built-in BO call script for consistency
- 📤 Export filtered data to CSV
- 🚀 Ready for deployment on Streamlit Community Cloud

---

## 📂 File Structure

```
📁 streamlit_bo_engagement/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies for deployment
```

---

## 🚀 Deployment (Streamlit Community Cloud)

1. Clone or fork this repo
2. Upload it to your GitHub account
3. Go to [Streamlit Cloud](https://share.streamlit.io/)
4. Paste your GitHub repo link
5. Set the main file as `app.py`
6. (Optional) Add authentication using `streamlit-authenticator`

---

## 📥 Sample Engagement File

To test the app, upload the sample report:  
**BO_Engagement_Report.xlsx**  
(*Contains Engagement Logs, PA Summary, and Call Scripts*)

---

## 📌 Future Enhancements (Optional)

- Role-based authentication for Managers and Analysts
- Google Sheets integration for real-time data sync
- Auto-reminders for low-engagement PAs

---

## 👨‍💻 Built With

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
- [Pandas](https://pandas.pydata.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)

---

## 📬 Feedback & Contributions

Feel free to open issues or submit pull requests to enhance this app further!
