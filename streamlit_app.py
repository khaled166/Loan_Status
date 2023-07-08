import streamlit as st
import joblib
import pandas as pd


Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")


def prediction_Inputs(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term,Credit_History,Property_Area, TotalIncome,LoanAmount_Ratio,CoAplicant_Status):

    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    test_df.at[0,"TotalIncome"] = TotalIncome
    test_df.at[0,"LoanAmount_Ratio"] = LoanAmount_Ratio
    test_df.at[0,"CoAplicant_Status"] = CoAplicant_Status
    
    result = Model.predict(test_df)
    return result[0]

def main():

    
    Gender = st.selectbox("Gender" ,['Female', 'Male'])
    Married  = st.selectbox("Married" , ['No', 'Yes'])
    Dependents = st.selectbox("Dependents" ,[0, 1, 2, 3])
    Education = st.selectbox("Education" ,['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed" , ['No', 'Yes'])
    ApplicantIncome = st.slider("ApplicantIncome" , 150,100000)
    CoapplicantIncome = st.slider("CoapplicantIncome" , 0,100000)
    LoanAmount = st.slider("LoanAmount" , 0,100000)
    Loan_Amount_Term = st.selectbox("Loan_Amount_Term" , [12.0, 36.0, 60.0, 84.0, 120.0, 180.0, 240.0, 300.0, 342.0, 360.0, 480.0])
    Credit_History = st.selectbox("Credit_History" ,[0,1])
    Property_Area = st.selectbox("Property_Area",['Rural', 'Semiurban', 'Urban'])
    TotalIncome = st.slider("TotalIncome",0,100000)
    LoanAmount_Ratio = st.slider("LoanAmount_Ratio",0,1)
    CoAplicant_Status = st.selectbox("CoAplicant_Status" , [0, 1])
    if st.button("predict"):
        results = prediction_Inputs(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term,Credit_History,Property_Area, TotalIncome,LoanAmount_Ratio,CoAplicant_Status)
        if results == "Y":
            st.text(f"Loan Status is:{results}, Customer desirve loan as meets Criteria")
        else:
            st.text(f"Loan Status is:{results} Customer does not desirve loan")


if __name__ == '__main__':
    main()
    
