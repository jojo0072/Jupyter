import streamlit as st
import time

st.header("Pomodoro Timer 🍅")
min_to_sec={"25:00":1500, "5:00": 300, "15:00": 900, "new":None}
sub="25:00"
timer=st.subheader(sub)
if "state" in globals() or "state" in locals():
    st.write("hey")
    if state=="Work":
        sub="25:00"
        timer=st.subheader(sub)
    elif state=="Short Break":
        sub="5:00"
        timer=st.subheader(sub)
    elif state=="Long Break":
        sub="15:00"
        timer=st.subheader(sub)

def timer_update(countdown): 
    global timer
    start_time=time.time()
    if countdown!=None:
        while countdown>0:
                minutes = countdown // 60
                seconds = countdown % 60
                timer=st.subheader(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
                countdown-=1
                if pause_button:
                    min_to_sec["new"]=current
                    break
                elif reset_button:
                    timer=st.subheader(sub)
                    min_to_sec["new"]=None

c1, c2, c3 = st.columns(3)
with c1:
    start_button=st.button("Start")
with c2:
    pause_button=st.button("Pause")
with c3:
    reset_button=st.button("Reset")
if start_button and min_to_sec["new"]==None:
    timer_update(min_to_sec[sub])
else:
    timer_update(min_to_sec["new"])
    min_to_sec["new"]=None    
state=st.radio("State: ", ("Work", "Short Break", "Long Break")) 
print("Hey")
cycles=st.write(f"Cycles completed: {2}✅")               


