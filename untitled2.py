# 필요한 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 데이터 로드
file_path_population = 'C:/Users/yky03/Documents/자치구 단위 서울 생활인구(내국인).csv'
file_path_wifi_location = 'C:/Users/yky03/Documents/서울시 공공와이파이 서비스 위치 정보.csv'
file_path_fixed_wifi_usage = 'C:/Users/yky03/Documents/서울특별시 공공와이파이 AP별 사용량_고정형(20210501_20211013).csv'

# 데이터프레임 생성
df_population = pd.read_csv(file_path_population, encoding='euc-kr')
df_wifi_location = pd.read_csv(file_path_wifi_location, encoding='euc-kr')
df_fixed_wifi_usage = pd.read_csv(file_path_fixed_wifi_usage, encoding='euc-kr')

# 기본 데이터 출력 및 데이터 타입 확인
print("Population Data:")
print(df_population.head())
print(df_population.info())

print("WiFi Locations Data:")
print(df_wifi_location.head())
print(df_wifi_location.info())

print("Fixed WiFi Usage Data:")
print(df_fixed_wifi_usage.head())
print(df_fixed_wifi_usage.info())

# 데이터 전처리
# 날짜 데이터 변환 및 그룹핑 예시 (여기서는 간단한 그룹핑만 수행)
population_summary = df_population.groupby('자치구코드')['총생활인구수'].sum().reset_index()
wifi_usage_summary = df_fixed_wifi_usage.groupby('자치구')['AP별 이용량(GB)'].sum().reset_index()

print("Population Summary:")
print(population_summary.head())

print("WiFi Usage Summary:")
print(wifi_usage_summary.head())

# 자치구코드와 자치구 이름을 매핑하기 위해 데이터 정제
# 자치구 이름을 코드로 변환하는 작업 (예시, 실제 데이터에 맞게 조정 필요)
gu_mapping = {
    '종로구': 11110, '중구': 11140, '용산구': 11170, '성동구': 11200, '광진구': 11215,
    '동대문구': 11230, '중랑구': 11260, '성북구': 11290, '강북구': 11305, '도봉구': 11320,
    '노원구': 11350, '은평구': 11380, '서대문구': 11410, '마포구': 11440, '양천구': 11470,
    '강서구': 11500, '구로구': 11530, '금천구': 11545, '영등포구': 11560, '동작구': 11590,
    '관악구': 11620, '서초구': 11650, '강남구': 11680, '송파구': 11710, '강동구': 11740
}

wifi_usage_summary['자치구코드'] = wifi_usage_summary['자치구'].map(gu_mapping)

# 데이터 병합
merged_data = pd.merge(population_summary, wifi_usage_summary, on='자치구코드')

print("Merged Data:")
print(merged_data.head())

# 상관관계 분석
correlation = merged_data.corr()
print("Correlation Matrix:")
print(correlation)

# 상관관계 시각화
plt.figure(figsize=(8, 6))
plt.scatter(merged_data['총생활인구수'], merged_data['AP별 이용량(GB)'])
plt.xlabel('총생활인구수')
plt.ylabel('AP별 이용량(GB)')
plt.title('총생활인구수와 AP별 이용량(GB) 간의 상관관계')
plt.grid(True)
plt.show()

# 예측 모델 생성
X = merged_data[['총생활인구수']]
y = merged_data['AP별 이용량(GB)']
model = LinearRegression()
model.fit(X, y)

# 예측 결과 시각화
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red', linewidth=2)
plt.xlabel('총생활인구수')
plt.ylabel('AP별 이용량(GB)')
plt.title('총생활인구수와 AP별 이용량(GB)의 회귀 분석')
plt.grid(True)
plt.show()

# 예측 결과 출력
predicted_usage = model.predict(X)
merged_data['예측 AP별 이용량(GB)'] = predicted_usage
print("Merged Data with Predictions:")
print(merged_data)
