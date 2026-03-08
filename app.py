import streamlit as st
import time

from modules.gear_geometry import generate_gear, gear_ratio
from modules.gear_plot import plot_gears


st.set_page_config(page_title="Gear Meshing Simulator", layout="wide")


# LOAD CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("⚙ Spur Gear Meshing Learning Simulator")


# SESSION STATE
if "running" not in st.session_state:
    st.session_state.running = False


# SIDEBAR CONTROLS
st.sidebar.header("Gear Parameters")

rpm = st.sidebar.slider("Input RPM",10,200,60)

teeth1 = st.sidebar.slider("Gear 1 Teeth",10,40,20)

teeth2 = st.sidebar.slider("Gear 2 Teeth",10,40,30)

module = st.sidebar.slider("Module",1,10,2)


ratio = gear_ratio(teeth1,teeth2)


# CALCULATIONS
d1 = module * teeth1
d2 = module * teeth2
center_distance = (d1+d2)/2


# METRICS
colA,colB,colC = st.columns(3)

colA.metric("Gear Ratio",round(ratio,2))
colB.metric("Pitch Diameter G1",d1)
colC.metric("Pitch Diameter G2",d2)

st.write("Center Distance:",round(center_distance,2))


# CONTROL BUTTONS
col1,col2 = st.columns(2)

with col1:
    if st.button("▶ Start Animation"):
        st.session_state.running = True

with col2:
    if st.button("⏹ Stop Animation"):
        st.session_state.running = False


plot_area = st.empty()


r1 = teeth1*0.04*module
r2 = teeth2*0.04*module


angle1 = 0
angle2 = 0


while st.session_state.running:

    angle1 += rpm*0.002
    angle2 -= (rpm/ratio)*0.002

    x1,y1,teeth1_shapes = generate_gear(r1,teeth1,(0,0),angle1)

    x2,y2,teeth2_shapes = generate_gear(r2,teeth2,(r1+r2,0),angle2)

    fig = plot_gears(x1,y1,teeth1_shapes,x2,y2,teeth2_shapes)

    plot_area.plotly_chart(fig,use_container_width=True)

    time.sleep(0.03)