import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import sys
from src.exception import CustomException

# Page configuration - MUST BE FIRST
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        font-size: 16px;
        border-radius: 8px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #e8f5e9;
        border-left: 5px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("🎓 Student Performance Predictor")
st.markdown("""
This application predicts a student's **Math Score** based on various demographic 
and academic factors using Machine Learning.
""")

st.divider()

# Sidebar - About section
with st.sidebar:
    st.title("📊 About")
    st.info("""
    This ML model predicts student math scores based on:
    - Demographics (gender, ethnicity)
    - Parental education
    - Lunch type
    - Test preparation
    - Reading & Writing scores
    """)
    
    st.divider()
    
    st.title("🎯 Model Info")
    st.metric("Model Accuracy", "88%", "R² Score")
    
    st.divider()
    
    st.markdown("### 📚 Instructions")
    st.write("""
    1. Fill in all student information
    2. Click 'Predict Math Score'
    3. View the prediction result
    """)

# Main content - Two columns layout
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Student Information")
    
    # Create form for inputs
    with st.form("prediction_form"):
        
        # Row 1: Gender and Ethnicity
        row1_col1, row1_col2 = st.columns(2)
        
        with row1_col1:
            gender = st.selectbox(
                "Gender",
                options=["male", "female"],
                help="Select student's gender"
            )
        
        with row1_col2:
            ethnicity = st.selectbox(
                "Race/Ethnicity",
                options=["group A", "group B", "group C", "group D", "group E"],
                help="Select student's racial/ethnic group"
            )
        
        # Row 2: Parental Education
        parental_education = st.selectbox(
            "Parental Level of Education",
            options=[
                "some high school",
                "high school",
                "some college",
                "associate's degree",
                "bachelor's degree",
                "master's degree"
            ],
            help="Highest education level of parents"
        )
        
        # Row 3: Lunch and Test Prep
        row3_col1, row3_col2 = st.columns(2)
        
        with row3_col1:
            lunch = st.selectbox(
                "Lunch Type",
                options=["standard", "free/reduced"],
                help="Type of lunch program"
            )
        
        with row3_col2:
            test_prep = st.selectbox(
                "Test Preparation Course",
                options=["none", "completed"],
                help="Whether student completed test prep course"
            )
        
        st.divider()
        
        # Row 4: Scores
        st.subheader("📝 Academic Scores")
        
        score_col1, score_col2 = st.columns(2)
        
        with score_col1:
            reading_score = st.slider(
                "Reading Score",
                min_value=0,
                max_value=100,
                value=70,
                step=1,
                help="Student's reading test score (0-100)"
            )
            st.progress(reading_score / 100)
        
        with score_col2:
            writing_score = st.slider(
                "Writing Score",
                min_value=0,
                max_value=100,
                value=70,
                step=1,
                help="Student's writing test score (0-100)"
            )
            st.progress(writing_score / 100)
        
        st.divider()
        
        # Submit button
        submitted = st.form_submit_button("🎯 Predict Math Score", use_container_width=True)

with col2:
    st.header("Quick Stats")
    
    # Display input summary
    st.metric("Reading Score", f"{reading_score}/100")
    st.metric("Writing Score", f"{writing_score}/100")
    
    avg_score = (reading_score + writing_score) / 2
    st.metric("Average Score", f"{avg_score:.1f}/100")
    
    # Score interpretation
    if avg_score >= 80:
        st.success("🌟 Excellent Performance")
    elif avg_score >= 60:
        st.info("📘 Good Performance")
    else:
        st.warning("📙 Needs Improvement")

# Prediction section
if submitted:
    st.divider()
    st.header("🎯 Prediction Result")
    
    try:
        # Show loading spinner
        with st.spinner("🔮 Analyzing student data and predicting..."):
            
            # Create CustomData object
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_education,
                lunch=lunch,
                test_preparation_course=test_prep,
                reading_score=reading_score,
                writing_score=writing_score
            )
            
            # Convert to DataFrame
            pred_df = data.get_data_as_dataframe()
            
            # Display input data
            with st.expander("📋 View Input Data"):
                st.dataframe(pred_df, use_container_width=True)
            
            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            predicted_score = round(results[0], 2)
        
        # Display result in a nice box
        st.success("✅ Prediction Complete!")
        
        # Create three columns for result display
        result_col1, result_col2, result_col3 = st.columns([1, 2, 1])
        
        with result_col2:
            st.markdown(f"""
            <div class="prediction-box">
                <h2 style='text-align: center; color: #2e7d32;'>
                    Predicted Math Score
                </h2>
                <h1 style='text-align: center; color: #1b5e20; font-size: 60px;'>
                    {predicted_score} / 100
                </h1>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        # Performance analysis
        st.subheader("📊 Performance Analysis")
        
        analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
        
        with analysis_col1:
            st.metric(
                "Reading Score",
                f"{reading_score}/100",
                delta=f"{reading_score - predicted_score:.1f}"
            )
        
        with analysis_col2:
            st.metric(
                "Predicted Math",
                f"{predicted_score}/100",
                delta="Prediction"
            )
        
        with analysis_col3:
            st.metric(
                "Writing Score",
                f"{writing_score}/100",
                delta=f"{writing_score - predicted_score:.1f}"
            )
        
        # Score interpretation
        st.divider()
        st.subheader("💡 Interpretation")
        
        if predicted_score >= 80:
            st.success("""
            **🌟 Excellent Performance Expected**
            
            The student is predicted to achieve an excellent math score. This indicates:
            - Strong foundational skills
            - Good comprehension abilities
            - Potential for advanced coursework
            """)
        elif predicted_score >= 60:
            st.info("""
            **📘 Good Performance Expected**
            
            The student is predicted to achieve a good math score. This indicates:
            - Solid understanding of concepts
            - Room for improvement with focused practice
            - Should continue regular study habits
            """)
        elif predicted_score >= 40:
            st.warning("""
            **📙 Average Performance Expected**
            
            The student is predicted to achieve an average math score. Recommendations:
            - Additional tutoring may be beneficial
            - Focus on strengthening fundamentals
            - Increase practice time
            """)
        else:
            st.error("""
            **📕 Below Average Performance Expected**
            
            The student may need additional support. Recommendations:
            - Immediate intervention recommended
            - One-on-one tutoring
            - Review basic concepts
            - Consider test preparation courses
            """)
        
        # Factors affecting prediction
        with st.expander("🔍 Factors Affecting Prediction"):
            st.write("**Key factors considered in this prediction:**")
            
            factors_col1, factors_col2 = st.columns(2)
            
            with factors_col1:
                st.write(f"✓ Gender: {gender}")
                st.write(f"✓ Race/Ethnicity: {ethnicity}")
                st.write(f"✓ Parental Education: {parental_education}")
            
            with factors_col2:
                st.write(f"✓ Lunch Type: {lunch}")
                st.write(f"✓ Test Prep: {test_prep}")
                st.write(f"✓ Reading Score: {reading_score}")
                st.write(f"✓ Writing Score: {writing_score}")
        
        # Download option
        st.divider()
        
        # Create downloadable report
        report_data = {
            "Student Information": [
                f"Gender: {gender}",
                f"Race/Ethnicity: {ethnicity}",
                f"Parental Education: {parental_education}",
                f"Lunch Type: {lunch}",
                f"Test Prep: {test_prep}",
                f"Reading Score: {reading_score}",
                f"Writing Score: {writing_score}",
                f"Predicted Math Score: {predicted_score}"
            ]
        }
        
        report_df = pd.DataFrame(report_data)
        
        csv = report_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Prediction Report",
            data=csv,
            file_name=f"prediction_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
    except Exception as e:
        st.error(f"❌ An error occurred during prediction: {str(e)}")
        st.info("Please make sure the model files are present in the 'artifacts' folder")
        
        with st.expander("🐛 Debug Information"):
            st.code(f"Error: {str(e)}")

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>Made with ❤️ using Streamlit | Student Performance Prediction System</p>
        <p><small>Based on Machine Learning algorithms trained on student performance data</small></p>
    </div>
    """, unsafe_allow_html=True)