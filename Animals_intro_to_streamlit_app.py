import streamlit as st
st.title("Streamlit Tutorial App")
st.write("This is my new app")
button1 = st.button("Click Me")
if button1:
    st.write("This is some text.")

st.header("Start of the Checkbox Section")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
    if like:
        st.write("Thanks. I like it too.")
    else:
        st.write("I'm sorry. You have bad tastes.")

st.header("Start of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")

st.header("Start of the Selectbox Section")
animal2 = st.selectbox("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button4 = st.button("Submit Animal 2")
if button4:
    st.write(animal2)
    if animal2 == "Lion":
        st.write("ROAR!")


st.header("Start of the Multiselect Section")
options = st.multiselect("What animals do you like?",
["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animals")
if button5:
    st.write(options)


st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?", 1,100, 10)
if st.button("Slider Button"):
    st.write(epochs_num)

st.header("Start of the Text Input Section")
user_text = st.text_input("What's your favorite movie?", "Star Wars Ep. IV")
if st.button("Text Button"):
    st.write(int(user_text))

user_num = st.number_input("What's your favorite number?")
if st.button("Number Button"):
    st.write(user_num)

def run_sentiment_analysis(txt):
    st.write(f"Analysis Done. {txt}")

txt = st.text_area('Text to analyze', '''It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair''')
st.write('Sentiment:', run_sentiment_analysis(txt))



#








# Load the pickled file
with open('RF_model_data.pkl', 'rb') as file:
    model_data = pickle.load(file)

# Retrieve the model
RF_model = model_data['RF_model']

# Create a Streamlit web app
st.title("Pore Pressure Predictor")

# Input features from the user
st.sidebar.header("Input Features")

# Example input features
# You should customize this based on your model's input features
feature1 = st.sidebar.slider("Feature 1", min_value=0.0, max_value=10.0, step=0.1)
feature2 = st.sidebar.slider("Feature 2", min_value=0.0, max_value=10.0, step=0.1)

# Create a button to make predictions
if st.sidebar.button("Make Prediction"):
    # Prepare the input data as a NumPy array
    input_data = np.array([[feature1, feature2]])

    # Make predictions using the RF model
    prediction = RF_model.predict(input_data)

    # Display the prediction
    st.write(f"Predicted Class: {prediction[0]}")

# Add some additional information or instructions
st.sidebar.text("Adjust the input features on the sidebar and click 'Make Prediction'.")

# Optionally, you can provide some information about the model
st.sidebar.header("Model Information")
st.sidebar.text("This is a Random Forest model.")

# Optionally, you can add other sections, charts, or explanations as needed