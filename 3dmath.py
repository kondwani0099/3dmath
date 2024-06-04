import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_data(equation):
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    
    if equation == "Parabolic Surface":
        Z = X**2 + Y**2
    elif equation == "Hyperbolic Paraboloid":
        Z = X**2 - Y**2
    elif equation == "Elliptic Cone":
        Z = np.sqrt(X**2 + Y**2)
    elif equation == "Sine Wave Surface":
        Z = np.sin(X) + np.sin(Y)
    elif equation == "Exponential Decay":
        Z = np.exp(-(X**2 + Y**2))
    elif equation == "Logarithmic Spiral":
        Z = np.log(np.sqrt(X**2 + Y**2))
    elif equation == "Circular Wave":
        Z = np.sin(np.sqrt(X**2 + Y**2))
    elif equation == "Wave Interference (Physics)":
        Z = np.sin(X) * np.cos(Y)
    elif equation == "Cobb-Douglas Production Function (Economics)":
        Z = X**0.5 * Y**0.5
    elif equation == "Gaussian Beam (Physics)":
        Z = np.exp(-X**2 - Y**2) * np.cos(10 * np.sqrt(X**2 + Y**2))
    elif equation == "Population Growth (Biology)":
        Z = 1 / (1 + np.exp(-X)) * 1 / (1 + np.exp(-Y))
    elif equation == "Potential Energy Surface (Chemistry)":
        Z = X**4 - X**2 + Y**4 - Y**2
    else:
        Z = np.zeros_like(X)  # Default to a flat surface if none selected
    
    return X, Y, Z

def plot_3d_surface(X, Y, Z, elevation, azimuth, zoom):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.view_init(elev=elevation, azim=azimuth)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.dist = zoom
    return fig

# Streamlit app
st.title("Interactive 3D Surface Plot")

# Dropdown for equation selection
equation = st.selectbox(
    "Choose a mathematical surface to plot:",
    [
        "Parabolic Surface", 
        "Hyperbolic Paraboloid", 
        "Elliptic Cone", 
        "Sine Wave Surface", 
        "Exponential Decay", 
        "Logarithmic Spiral", 
        "Circular Wave", 
        "Wave Interference (Physics)",
        "Cobb-Douglas Production Function (Economics)",
        "Gaussian Beam (Physics)",
        "Population Growth (Biology)",
        "Potential Energy Surface (Chemistry)"
    ]
)

# Generate data based on selected equation
X, Y, Z = generate_data(equation)

# Explanation
st.write(f"""
### Explanation
This application visualizes a 3D surface plot of the {equation}. These functions are commonly used in various fields such as physics, economics, biology, chemistry, and mathematics to describe different phenomena.

The equation for the surface is given by:
""")

if equation == "Parabolic Surface":
    st.latex(r"Z = X^2 + Y^2")
elif equation == "Hyperbolic Paraboloid":
    st.latex(r"Z = X^2 - Y^2")
elif equation == "Elliptic Cone":
    st.latex(r"Z = \sqrt{X^2 + Y^2}")
elif equation == "Sine Wave Surface":
    st.latex(r"Z = \sin(X) + \sin(Y)")
elif equation == "Exponential Decay":
    st.latex(r"Z = e^{-(X^2 + Y^2)}")
elif equation == "Logarithmic Spiral":
    st.latex(r"Z = \log(\sqrt{X^2 + Y^2})")
elif equation == "Circular Wave":
    st.latex(r"Z = \sin(\sqrt{X^2 + Y^2})")
elif equation == "Wave Interference (Physics)":
    st.latex(r"Z = \sin(X) \cdot \cos(Y)")
elif equation == "Cobb-Douglas Production Function (Economics)":
    st.latex(r"Z = X^{0.5} \cdot Y^{0.5}")
elif equation == "Gaussian Beam (Physics)":
    st.latex(r"Z = e^{-X^2 - Y^2} \cdot \cos(10 \cdot \sqrt{X^2 + Y^2})")
elif equation == "Population Growth (Biology)":
    st.latex(r"Z = \frac{1}{1 + \exp(-X)} \cdot \frac{1}{1 + \exp(-Y)}")
elif equation == "Potential Energy Surface (Chemistry)":
    st.latex(r"Z = X^4 - X^2 + Y^4 - Y^2")

st.write("You can interact with the plot using the sliders below to adjust the view.")

# Sliders for user input
elevation = st.slider("Elevation", 0, 90, 30)
azimuth = st.slider("Azimuth", 0, 360, 30)
zoom = st.slider("Zoom", 5, 20, 10)

# Plot the 3D surface
fig = plot_3d_surface(X, Y, Z, elevation, azimuth, zoom)
st.pyplot(fig)
