import pandas as pd

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

# 데이터 확인
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
