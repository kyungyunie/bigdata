import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 원하는 한글 폰트 경로
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 데이터 로드
file_path_population = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/자치구 단위 서울 생활인구(내국인).csv'
file_path_wifi_usage_fixed = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_고정형(20210501_20211013).csv'

df_population = pd.read_csv(file_path_population, encoding='euc-kr')
df_wifi_usage_fixed = pd.read_csv(file_path_wifi_usage_fixed, encoding='euc-kr')

# 데이터 전처리
df_population_grouped = df_population.groupby('자치구코드')['총생활인구수'].sum().reset_index()
df_wifi_usage_grouped = df_wifi_usage_fixed.groupby('자치구')['AP별 이용량(GB)'].sum().reset_index()

# 자치구코드와 자치구 이름을 매핑
gu_code_name = {
    11110: '종로구', 11140: '중구', 11170: '용산구', 11200: '성동구', 11215: '광진구',
    # 여기에 다른 자치구 코드를 추가하세요
}

df_population_grouped['자치구'] = df_population_grouped['자치구코드'].map(gu_code_name)

# 데이터 병합
merged_data = pd.merge(df_population_grouped, df_wifi_usage_grouped, on='자치구')

# 상관 관계 분석
correlation = merged_data[['총생활인구수', 'AP별 이용량(GB)']].corr()

# Streamlit 앱 설정
st.title('인구수와 와이파이 사용량 상관 관계 분석')

st.write("상관 관계 메트릭스:")
st.write(correlation)

# 상관 관계 히트맵 시각화
fig, ax = plt.subplots()
sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
plt.title('상관 관계 히트맵')
st.pyplot(fig)
