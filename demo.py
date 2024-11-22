import streamlit as st
st.title("Thevenin's Therom-2205A21044")

def output(vth,rth,rl):
    il=vth/(rth+rl)
    pl=il*il*rl
    return il,pl

col1,col2=st.columns(2)
with col1:
    vth=st.number_input("Vth (V)", value=10)
    rth=st.number_input("Rth (ohms)", value=100)
    rl=st.number_input("Rl (omhs)", value=100)
    compute=st.button("compute")

with col2:
    with st.container(border=True): 
        if compute:
            il,pl=output(vth,rth,rl)
            st.write(f"Load current={il:.2f} A")
            st.write(f"Load power={pl:.2f} Watts")