# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from IPython.display import YouTubeVideo

st.header('병역처분결과서의 결과를 확인하세요')

if st.button('현역입영대상'):
     st.write('1-3급은 현역입영대상입니다')
if st.button('사회복무요원소집대상'):
     st.write('4급은 사회복무요원 소집 대상입니다')
if st.button('전시근로역'):
     st.write('5급은 전시근로역대상입니다')
if st.button('병역면제'):
     st.write('6급은 병역이 면제됩니다')
if st.button('재검대상'):
     st.write('7급 치유기간 이후에 다시 검사받으세요')
     
     
     
#video_SD = YouTubeVideo("jWQx2f-CErU?si=qycwg5gnqN0caB0_", width=500) # https://youtu.be/POe9SOEKotk
#display(video_SD)
