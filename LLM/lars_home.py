import streamlit as st

import pandas as pd
from numpy.random import default_rng as rng


def main():
    
    
    col1, col2 = st.columns([0.6,0.4])
    
    with col1:
        st.image('./img/pexels-kindelmedia-8566566.jpg')
    
    with col2:
        
        st.title("Large Action Robotic System [Lars]",text_alignment='center',)
        st.divider()
        st.subheader("is an agentic robotic orchestration layer designed to bridge the gap between natural language intent and physical hardware execution.",
                 text_alignment='center')
        st.space('large')
        df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

        st.area_chart(df)

if __name__ == '__main__':
    main()