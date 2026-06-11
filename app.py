import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(to right, #eef4ff, #f8fbff);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: #dbeafe;
    padding-top:20px;
}

/* Sidebar Text */
[data-testid="stSidebar"] *{
    color:#1e293b;
}

/* Metric Cards */
.metric-card{
    background:white;
    padding:22px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    border:1px solid #dbeafe;
}

/* Chart Cards */
.chart-card{
    background:white;
    padding:15px;
    border-radius:18px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

/* Titles */
h1,h2,h3,h4{
    color:#1e293b;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#2563eb;
    color:white;
    border:none;
    border-radius:12px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1d4ed8;
}

/* Inputs */
.stNumberInput input{
    background:white;
    color:#1e293b;
}

.stTextInput input{
    background:white;
    color:#1e293b;
}

/* Dataframe */
[data-testid="stDataFrame"]{
    background:white;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(
    r"C:\Users\komal\OneDrive\Desktop\Jupyter Notebook\risk_prediction_model.pkl"
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🏥 Healthcare Menu")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Dashboard", "Prediction", "Reports"]
)

# =========================================================
# SAMPLE DASHBOARD DATA
# =========================================================

df = pd.DataFrame({

    "City": [
        "Delhi","Mumbai","Indore","Pune",
        "Delhi","Mumbai","Indore","Pune",
        "Delhi","Mumbai","Indore","Pune"
    ],

    "Disease": [
        "Diabetes","Flu","Asthma","Heart Disease",
        "Diabetes","Flu","Asthma","Heart Disease",
        "Flu","Asthma","Diabetes","Heart Disease"
    ],

    "Risk": [
        "High","Medium","Low","High",
        "Medium","Low","High","Medium",
        "Low","Medium","High","High"
    ],

    "Gender": [
        "Male","Female","Male","Female",
        "Male","Female","Male","Female",
        "Male","Female","Male","Female"
    ],

    "Patients": [
        50,40,30,60,
        45,35,25,55,
        20,30,40,50
    ]
})

# =========================================================
# FILTERS
# =========================================================

st.sidebar.markdown("---")

city_filter = st.sidebar.selectbox(
    "📍 Select City",
    ["All"] + list(df["City"].unique())
)

disease_filter = st.sidebar.selectbox(
    "🦠 Select Disease",
    ["All"] + list(df["Disease"].unique())
)

# =========================================================
# FILTER LOGIC
# =========================================================

filtered_df = df.copy()

if city_filter != "All":

    filtered_df = filtered_df[
        filtered_df["City"] == city_filter
    ]

if disease_filter != "All":

    filtered_df = filtered_df[
        filtered_df["Disease"] == disease_filter
    ]

# =========================================================
# HOME PAGE
# =========================================================

if page == "Home":

    st.markdown("""
    <h1 style='text-align:center;'>
    🏥 HEALTHCARE ANALYTICS DASHBOARD
    </h1>
    """, unsafe_allow_html=True)

    st.write("")

    st.info("""
    Welcome to AI Healthcare Risk Prediction System.

    Features:
    - AI Risk Prediction
    - Patient Records
    - Interactive Dashboard
    - Downloadable Reports
    - Dynamic Filters
    """)

    st.write("")

    # =====================================================
    # KPI CARDS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("""
        <div class='metric-card'>
        <h1>1250</h1>
        <h3>Total Patients</h3>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class='metric-card'>
        <h1>320</h1>
        <h3>High Risk Patients</h3>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class='metric-card'>
        <h1>870</h1>
        <h3>Recovered Patients</h3>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown("""
        <div class='metric-card'>
        <h1>10.6K</h1>
        <h3>Avg Treatment Cost</h3>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# DASHBOARD PAGE
# =========================================================

elif page == "Dashboard":

    st.title("📊 Healthcare Analytics Dashboard")

    # =====================================================
    # KPI SECTION
    # =====================================================

    total_patients = filtered_df["Patients"].sum()

    male_count = filtered_df[
        filtered_df["Gender"] == "Male"
    ]["Patients"].sum()

    female_count = filtered_df[
        filtered_df["Gender"] == "Female"
    ]["Patients"].sum()

    high_risk = filtered_df[
        filtered_df["Risk"] == "High"
    ]["Patients"].sum()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(f"""
        <div class='metric-card'>
        <h1>{total_patients}</h1>
        <h3>Total Patients</h3>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class='metric-card'>
        <h1>{male_count}</h1>
        <h3>Male Patients</h3>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class='metric-card'>
        <h1>{female_count}</h1>
        <h3>Female Patients</h3>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
        <div class='metric-card'>
        <h1>{high_risk}</h1>
        <h3>High Risk</h3>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # =====================================================
    # CHART DATA
    # =====================================================

    risk_data = filtered_df.groupby(
        "Risk"
    )["Patients"].sum().reset_index()

    city_data = filtered_df.groupby(
        "City"
    )["Patients"].sum().reset_index()

    disease_data = filtered_df.groupby(
        "Disease"
    )["Patients"].sum().reset_index()

    gender_data = filtered_df.groupby(
        "Gender"
    )["Patients"].sum().reset_index()

    # =====================================================
    # ROW 1
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.pie(
            risk_data,
            names="Risk",
            values="Patients",
            title="Risk Distribution",
            hole=0.4
        )

        fig1.update_layout(
            paper_bgcolor="white",
            font_color="#1e293b"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with col2:

        fig2 = px.bar(
            city_data,
            x="City",
            y="Patients",
            color="Patients",
            title="Patients by City"
        )

        fig2.update_layout(
            paper_bgcolor="white",
            font_color="#1e293b"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # =====================================================
    # ROW 2
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        fig3 = px.bar(
            disease_data,
            x="Disease",
            y="Patients",
            color="Patients",
            title="Disease Analysis"
        )

        fig3.update_layout(
            paper_bgcolor="white",
            font_color="#1e293b"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with col2:

        fig4 = px.pie(
            gender_data,
            names="Gender",
            values="Patients",
            title="Gender Distribution"
        )

        fig4.update_layout(
            paper_bgcolor="white",
            font_color="#1e293b"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    # =====================================================
    # INSIGHTS SECTION
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class='metric-card'>

        <h3>🧠 Key Insights</h3>

        ✅ Diabetes cases are increasing.<br><br>

        ✅ High-risk patients mostly belong to metro cities.<br><br>

        ✅ Male patients are slightly higher.<br><br>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class='metric-card'>

        <h3>💡 Recommendations</h3>

        ✔ Increase preventive healthcare awareness.<br><br>

        ✔ Improve early diagnosis systems.<br><br>

        ✔ Focus on high-risk patient monitoring.<br><br>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PREDICTION PAGE
# =========================================================

elif page == "Prediction":

    st.title("🩺 AI Risk Prediction")

    st.write("### Enter Patient Details")

    # =====================================================
    # INPUT FIELDS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        patient_name = st.text_input(
            "Patient Name"
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=25
        )

        bmi = st.number_input(
            "BMI",
            value=27.0
        )

    with col2:

        city = st.selectbox(
            "City",
            ["Delhi", "Mumbai", "Indore", "Pune"]
        )

        disease = st.selectbox(
            "Disease",
            [
                "Diabetes",
                "Flu",
                "Asthma",
                "Heart Disease"
            ]
        )

        bp = st.number_input(
            "Blood Pressure",
            value=120
        )

        sugar = st.number_input(
            "Sugar Level",
            value=140
        )

        cholesterol = st.number_input(
            "Cholesterol",
            value=200
        )

    # =====================================================
    # PREDICT BUTTON
    # =====================================================

    if st.button("🔍 Predict Risk"):

        # =================================================
        # MODEL INPUT
        # =================================================

        model_input = pd.DataFrame(
            [[age, bmi, bp, sugar, cholesterol]],
            columns=[
                "Age",
                "BMI",
                "BP",
                "Sugar_Level",
                "Cholesterol"
            ]
        )

        # =================================================
        # PREDICTION
        # =================================================

        prediction = model.predict(
            model_input
        )

        risk_result = prediction[0]

        # =================================================
        # RISK SCORE
        # =================================================

        if risk_result == "High Risk":

            st.error("⚠️ High Risk Detected")

            risk_score = 85

        elif risk_result == "Medium Risk":

            st.warning("🟡 Medium Risk")

            risk_score = 55

        else:

            st.success("✅ Low Risk")

            risk_score = 20

        # =================================================
        # GAUGE CHART
        # =================================================

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=risk_score,

            title={'text': "Health Risk Score"},

            gauge={

                'axis': {'range': [0, 100]},

                'bar': {'color': "#2563eb"},

                'steps': [

                    {
                        'range': [0, 40],
                        'color': "#bbf7d0"
                    },

                    {
                        'range': [40, 70],
                        'color': "#fde68a"
                    },

                    {
                        'range': [70, 100],
                        'color': "#fca5a5"
                    }
                ]
            }
        ))

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =================================================
        # SAVE PATIENT RECORD
        # =================================================

        patient_record = pd.DataFrame({

            "Patient Name": [patient_name],

            "Gender": [gender],

            "City": [city],

            "Disease": [disease],

            "Age": [age],

            "BMI": [bmi],

            "Blood Pressure": [bp],

            "Sugar Level": [sugar],

            "Cholesterol": [cholesterol],

            "Prediction": [risk_result]
        })

        try:

            old_data = pd.read_csv(
                "patient_records.csv"
            )

            updated_data = pd.concat(
                [old_data, patient_record],
                ignore_index=True
            )

        except:

            updated_data = patient_record

        updated_data.to_csv(
            "patient_records.csv",
            index=False
        )

        st.success(
            "✅ Patient record saved successfully"
        )

# =========================================================
# REPORT PAGE
# =========================================================

elif page == "Reports":

    st.title("📄 Patient Records")

    try:

        report_data = pd.read_csv(
            "patient_records.csv"
        )

        # =================================================
        # SEARCH BAR
        # =================================================

        search = st.text_input(
            "🔍 Search Patient"
        )

        if search:

            report_data = report_data[
                report_data["Patient Name"]
                .str.contains(
                    search,
                    case=False
                )
            ]

        # =================================================
        # DISPLAY TABLE
        # =================================================

        st.dataframe(
            report_data,
            use_container_width=True
        )

        # =================================================
        # DOWNLOAD BUTTON
        # =================================================

        csv = report_data.to_csv(index=False)

        st.download_button(
            label="⬇ Download Patient Records",
            data=csv,
            file_name="patient_records.csv",
            mime="text/csv"
        )

    except:

        st.warning(
            "No patient records available yet."
        )