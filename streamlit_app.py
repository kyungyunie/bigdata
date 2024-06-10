import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import quote

# URL 인코딩
file_url_population = 'https://raw.githubusercontent.com/kyungyunie/bigdata/master/' + quote('자치구 단위 서울 생활인구(내국인).csv')
file_url_wifi_usage_fixed = 'https://raw.githubusercontent.com/kyungyunie/bigdata/master/' + quote('서울특별시 공공와이파이 AP별 사용량_고정형(20210501_20211013).csv')

# 데이터 불러오기
df_population = pd.read_csv(file_url_population, encoding='euc-kr')
df_wifi_usage_fixed = pd.read_csv(file_url_wifi_usage_fixed, encoding='euc-kr')

# 자치구 이름 매핑
gu_code_name = {
    11110: '종로구', 11140: '중구', 11170: '용산구', 11200: '성동구', 11215: '광진구',
    11230: '동대문구', 11245: '중랑구', 11260: '성북구', 11290: '강북구', 11305: '도봉구',
    11320: '노원구', 11350: '은평구', 11380: '서대문구', 11410: '마포구', 11440: '양천구',
    11470: '강서구', 11500: '구로구', 11530: '금천구', 11545: '영등포구', 11560: '동작구',
    11590: '관악구', 11620: '서초구', 11650: '강남구', 11680: '송파구', 11710: '강동구'
}
df_population['자치구'] = df_population['자치구코드'].map(gu_code_name)

# 데이터 전처리
population_summary = df_population.groupby('자치구코드')['총생활인구수'].sum().reset_index()
wifi_usage_summary = df_wifi_usage_fixed.groupby('자치구')['AP별 이용량(GB)'].sum().reset_index()

# 자치구코드와 자치구 이름 매핑
gu_code_name_df = pd.DataFrame(list(gu_code_name.items()), columns=['자치구코드', '자치구'])
merged_data = pd.merge(population_summary, gu_code_name_df, on='자치구코드')
merged_data = pd.merge(merged_data, wifi_usage_summary, on='자치구', how='inner')

# Streamlit 대시보드 설정
st.set_page_config(layout="wide")

# 사이드바 메뉴
with st.sidebar:
    st.title("대시보드 메뉴")
    page = st.radio("페이지 선택", ["홈", "인구 데이터", "와이파이 사용량", "상관 관계 분석", "데이터 탐색"])

# 페이지에 따른 콘텐츠 표시
if page == "홈":
    st.title("서울시 공공와이파이 대시보드")
    st.write("사이드바에서 다른 페이지를 선택하세요.")
elif page == "인구 데이터":
    st.title("자치구별 인구 데이터")
    st.write(population_summary)
    st.bar_chart(population_summary.set_index('자치구코드'))
elif page == "와이파이 사용량":
    st.title("자치구별 와이파이 사용량 데이터")
    st.write(wifi_usage_summary)
    st.bar_chart(wifi_usage_summary.set_index('자치구'))
elif page == "상관 관계 분석":
    st.title("인구수와 와이파이 사용량 상관 관계 분석")
    correlation = merged_data[['총생활인구수', 'AP별 이용량(GB)']].corr()
    st.write("상관 관계 매트릭스:")
    st.write(correlation)
    fig, ax = plt.subplots()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
elif page == "데이터 탐색":
    st.title("데이터 탐색")
    selected_gu = st.selectbox("자치구 선택", df_population['자치구'].unique(), key='gu_select')
    filtered_data = df_population[df_population['자치구'] == selected_gu]
    st.write(filtered_data)
    st.line_chart(filtered_data.set_index('기준일ID')['총생활인구수'])
