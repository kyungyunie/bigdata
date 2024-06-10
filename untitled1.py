import pandas as pd

# 데이터 로드
file_path_population = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/자치구 단위 서울 생활인구(내국인).csv'
file_path_wifi_locations = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울시 공공와이파이 서비스 위치 정보.csv'
file_path_wifi_usage_fixed = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_고정형(20210501_20211013).csv'
file_path_wifi_usage_city_bus = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_시내버스(20210501_20211013).csv'
file_path_wifi_usage_village_bus = 'C:/Users/yky03/OneDrive/바탕 화면/새 폴더/서울특별시 공공와이파이 AP별 사용량_마을버스(20210501_20211013).csv'

df_population = pd.read_csv(file_path_population, encoding='euc-kr')
df_wifi_locations = pd.read_csv(file_path_wifi_locations, encoding='euc-kr')
df_wifi_usage_fixed = pd.read_csv(file_path_wifi_usage_fixed, encoding='euc-kr')
df_wifi_usage_city_bus = pd.read_csv(file_path_wifi_usage_city_bus, encoding='euc-kr')
df_wifi_usage_village_bus = pd.read_csv(file_path_wifi_usage_village_bus, encoding='euc-kr')

# 필요 없는 컬럼 제거 (필요시)
df_population = df_population[['자치구코드', '총생활인구수']]
df_wifi_usage_fixed = df_wifi_usage_fixed[['자치구', 'AP별 이용량(GB)']]
df_wifi_usage_city_bus = df_wifi_usage_city_bus[['구분', 'AP별 이용량(단위 : GB)']]
df_wifi_usage_village_bus = df_wifi_usage_village_bus[['구분', 'AP별 이용량(GB)']]

# 자치구코드를 정수형으로 변환 (필요시)
df_population['자치구코드'] = df_population['자치구코드'].astype(str)

# 각 WiFi 사용량 데이터 합계 구하기
fixed_usage_summary = df_wifi_usage_fixed.groupby('자치구')['AP별 이용량(GB)'].sum().reset_index()
city_bus_usage_summary = df_wifi_usage_city_bus.groupby('구분')['AP별 이용량(단위 : GB)'].sum().reset_index()
village_bus_usage_summary = df_wifi_usage_village_bus.groupby('구분')['AP별 이용량(GB)'].sum().reset_index()

# 자치구 이름을 자치구코드로 변환 (예제: 서울시 자치구 데이터프레임을 통해 변환)
# 여기서는 가상 데이터프레임으로 예시
seoul_districts = pd.DataFrame({
    '자치구': ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'],
    '자치구코드': ['11110', '11140', '11170', '11200', '11215', '11230', '11260', '11290', '11305', '11320', '11350', '11380', '11410', '11440', '11470', '11500', '11530', '11545', '11560', '11590', '11620', '11650', '11680', '11710', '11740']
})

fixed_usage_summary = pd.merge(fixed_usage_summary, seoul_districts, on='자치구', how='left')

# 데이터 병합
merged_data = pd.merge(df_population, fixed_usage_summary, left_on='자치구코드', right_on='자치구코드', how='left')

print("Merged Data:")
print(merged_data.head())
