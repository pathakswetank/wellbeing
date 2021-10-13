
import warnings
warnings.filterwarnings("ignore")
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('stress.pkl', 'rb') 
regress = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Mental_Toughness, Self_Confidence, Motivation, Attention, Anxiety, Stress):   
 
    # Pre-processing user input    
    if Mental_Toughness == "Very Good":
        Mental_Toughness = 5
    elif Mental_Toughness == "Good":
        Mental_Toughness = 4
    elif Mental_Toughness == "Average":
        Mental_Toughness = 3
    elif Mental_Toughness == "Fair":
        Mental_Toughness = 2
    elif Mental_Toughness == "Poor":
        Mental_Toughness = 1
        
    if Self_Confidence == "Very Good":
        Self_Confidence = 5
    elif Self_Confidence == "Good":
        Self_Confidence = 4
    elif Self_Confidence == "Average":
        Self_Confidence = 3
    elif Self_Confidence == "Fair":
        Self_Confidence = 2
    elif Self_Confidence == "Poor":
        Self_Confidence = 1
        
    if Motivation == "Very Good":
        Motivation = 5
    elif Motivation == "Good":
        Motivation = 4
    elif Motivation == "Average":
        Motivation = 3
    elif Motivation == "Fair":
        Motivation = 2
    elif Motivation == "Poor":
        Motivation = 1

    if Attention == "Very Good":
        Attention = 5
    elif Attention == "Good":
        Attention = 4
    elif Attention == "Average":
        Attention = 3
    elif Attention == "Fair":
        Attention = 2
    elif Attention == "Poor":
        Attention = 1

    if Anxiety == "Very Low":
        Anxiety = 1
    elif Anxiety == "Low":
        Anxiety = 2
    elif Anxiety == "Average":
        Anxiety = 3
    elif Anxiety == "Above Average":
        Anxiety = 4
    elif Anxiety == "High":
        Anxiety = 5

    if Stress == "Very Low":
        Stress = 1
    elif Stress == "Low":
        Stress = 2
    elif Stress == "Average":
        Stress = 3
    elif Stress == "Above Average":
        Stress = 4
    elif Stress == "High":
        Stress = 5

    # Making predictions 
    prediction = regress.predict( 
        [[Mental_Toughness, Self_Confidence, Motivation, Attention, Anxiety, Stress]])
     
    
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:#4080bf;padding:13px">   
    <h1 style ="color:white;text-align:center;">CENTRE FOR SPORTS SCIENCE </h1>
    <h2 style ="color:white;text-align:center;">Psychological Well Being Assessment </h2> 
    </div>  
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Mental_Toughness = st.selectbox('Mental_Toughness',("Very Good","Good", "Average", "Fair", "Poor"))
    Self_Confidence = st.selectbox('Self_Confidence',("Very Good","Good", "Average", "Fair", "Poor")) 
    Motivation = st.selectbox('Motivation',("Very Good","Good", "Average", "Fair", "Poor"))
    Attention = st.selectbox('Attention',("Very Good","Good", "Average", "Fair", "Poor"))
    Anxiety = st.selectbox('Anxiety',("Very Low","Low", "Average", "Above Average", "High"))
    Stress = st.selectbox('Stress',("Very Low","Low", "Average", "Above Average", "High")) 
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Mental_Toughness, Self_Confidence, Motivation, Attention, Anxiety, Stress) 
        st.success('Your Well Being is {}'.format((result/5)*100))
        
     
if __name__=='__main__': 
    main()
