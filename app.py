

import streamlit as st
import pandas as pd

st.title('청주 시외버스터미널 시간표')
# CSV 파일 불러오기
df = pd.read_csv('terminal_data.csv')  # 경로 지정

# 터미널 리스트를 가져오기 (중복 제거)
terminals = df['터미널'].unique()

# 터미널 선택
search_term = st.text_input('터미널을 검색하세요 빈칸이면 리스트를볼수있습니다.', '')
filtered_terminals = df['터미널'].unique()
if search_term:
    filtered_terminals = [terminal for terminal in filtered_terminals if search_term.lower() in terminal.lower()]

# 크롤링은 터미널 이름 출발; 시간; 요금; 소요시간;
# 크롤링한 데이터를 마이sql 에 저장하고 저장한 테이블을
# 데이터에 불러온다. 다실패
# csv 로 활용
selected_terminal = st.selectbox("터미널을 선택하세요",  filtered_terminals)

# # 선택된 터미널에 해당하는 데이터 필터링
selected_data = df[df['터미널'] == selected_terminal]
st.write(selected_data)
# # # 선택된 터미널의 출발 시간, 요금, 소요시간을 표로 표시
# st.write(f"선택한 터미널: {selected_terminal}")
# st.dataframe(filtered_df[['출발', '요금(어른)', '소요시간']])
# # for time in times:
# #     st.write(time)

# df = pd.DataFrame(data)

# options=["","감곡시외터미널","강릉시외버스터미널","고양종합터미널","고한사북공영버스터미널"] 
# # 옵션스에 마이 sql에 저장된 터미널이름


# selected_option = st.selectbox("도착지 선택:", options)
# if selected_option:  
#     df






# 데이터 베이스에 저장되어있는 df 출력

    # if st.button("출발시간 요금 소요시간"):
    #     st.button(f"'{selected_option}'다시 누르면 닫을수있습니다.")


# st.table(df)

# df = pd.DataFrame({
#     '버스 번호':[513,514,814,842-1,842-2,871,872,917],
#     '도착시간' :[1,2,3,4,5,6,7,8]
# })

# # if st.button('터미널 선택'):
# #     st.table(df)


# data = pd.read_csv("data.ipynb")


# # terminal_name 열 가져오기
# terminal_names = data["terminal_name"].tolist()














