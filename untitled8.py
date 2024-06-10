import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 파일 경로 설정
file_path_population = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/자치구 단위 서울 생활인구(내국인).csv'
file_path_wifi_locations = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울시 공공와이파이 서비스 위치 정보.csv'
file_path_wifi_usage_fixed = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_고정형(20210501_20211013).csv'
file_path_wifi_usage_city_bus = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_시내버스(20210501_20211013).csv'
file_path_wifi_usage_village_bus = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_마을버스(20210501_20211013).csv'

# 데이터 로드
df_population = pd.read_csv(file_path_population, encoding='euc-kr')
df_wifi_locations = pd.read_csv(file_path_wifi_locations, encoding='euc-kr')
df_wifi_usage_fixed = pd.read_csv(file_path_wifi_usage_fixed, encoding='euc-kr')
df_wifi_usage_city_bus = pd.read_csv(file_path_wifi_usage_city_bus, encoding='euc-kr')
df_wifi_usage_village_bus = pd.read_csv(file_path_wifi_usage_village_bus, encoding='euc-kr')

# 인구 데이터 요약
population_summary = df_population.groupby('자치구코드')['총생활인구수'].sum().reset_index()

# 고정형 WiFi 사용량 요약
wifi_usage_summary = df_wifi_usage_fixed.groupby('자치구')['AP별 이용량(GB)'].sum().reset_index()

# 자치구코드를 문자형으로 변환
population_summary['자치구코드'] = population_summary['자치구코드'].astype(str)

# 자치구 이름을 매칭할 수 있는 데이터프레임 생성
code_to_name = {
    '11110': '종로구', '11140': '중구', '11170': '용산구', '11200': '성동구', '11215': '광진구',
    '11230': '동대문구', '11245': '중랑구', '11260': '성북구', '11290': '강북구', '11305': '도봉구',
    '11320': '노원구', '11350': '은평구', '11380': '서대문구', '11410': '마포구', '11440': '양천구',
    '11470': '강서구', '11500': '구로구', '11530': '금천구', '11545': '영등포구', '11560': '동작구',
    '11590': '관악구', '11620': '서초구', '11650': '강남구', '11680': '송파구', '11710': '강동구'
}
population_summary['자치구'] = population_summary['자치구코드'].map(code_to_name)

# 병합
merged_data = pd.merge(population_summary, wifi_usage_summary, on='자치구')

print("Merged Data:")
print(merged_data.head())

# 상관관계 분석
correlation = merged_data[['총생활인구수', 'AP별 이용량(GB)']].corr()
print("Correlation Matrix:")
print(correlation)

# 상관관계 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
