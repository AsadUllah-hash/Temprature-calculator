import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15
    
    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    
    return value  # If target is Celsius

# Streamlit UI
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️", layout="centered")
st.title("🌡️ Temperature Converter")

# Sidebar for input
st.sidebar.header("Temperature Conversion")
temp_value = st.sidebar.number_input("Enter Temperature:", value=0.0, step=0.1)
from_unit = st.sidebar.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.sidebar.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Perform conversion
if st.sidebar.button("Convert"):
    converted_temp = convert_temperature(temp_value, from_unit, to_unit)
    st.success(f"🌡️ {temp_value}° {from_unit} is {converted_temp:.2f}° {to_unit}")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #36d1dc, #5b86e5);
            color: white;
        }
        .stButton>button {
            background-color: #ff6f61;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff4a3d;
        }
    </style>
    """,
    unsafe_allow_html=True
)