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

# 데이터 요약 확인
print("Population Data:")
print(df_population.head())
print(df_population.info())

print("WiFi Locations Data:")
print(df_wifi_locations.head())
print(df_wifi_locations.info())

print("Fixed WiFi Usage Data:")
print(df_wifi_usage_fixed.head())
print(df_wifi_usage_fixed.info())

print("City Bus WiFi Usage Data:")
print(df_wifi_usage_city_bus.head())
print(df_wifi_usage_city_bus.info())

print("Village Bus WiFi Usage Data:")
print(df_wifi_usage_village_bus.head())
print(df_wifi_usage_village_bus.info())

# 자치구 이름과 자치구코드 매핑을 위한 데이터프레임 생성
gu_code_name = df_population[['자치구코드']].drop_duplicates().reset_index(drop=True)
gu_code_name['자치구'] = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']

# 인구수 데이터 요약
df_population_summary = df_population.groupby('자치구코드')['총생활인구수'].sum().reset_index()

# 와이파이 이용량 데이터 요약
df_wifi_usage_summary = df_wifi_usage_fixed.groupby('자치구')['AP별 이용량(GB)'].sum().reset_index()

# 자치구 이름을 자치구 코드로 병합
merged_data = pd.merge(df_population_summary, gu_code_name, on='자치구코드')
merged_data = pd.merge(merged_data, df_wifi_usage_summary, on='자치구', how='inner')

print("Merged Data:")
print(merged_data.head())

# 상관관계 계산 및 시각화
correlation = merged_data[['총생활인구수', 'AP별 이용량(GB)']].corr()
print("Correlation Matrix:")
print(correlation)

# 상관관계 히트맵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

# 산포도 그리기
plt.figure(figsize=(10, 8))
plt.scatter(merged_data['총생활인구수'], merged_data['AP별 이용량(GB)'])
plt.xlabel('총생활인구수')
plt.ylabel('AP별 이용량(GB)')
plt.title('Total Population vs. WiFi Usage')
plt.show()
