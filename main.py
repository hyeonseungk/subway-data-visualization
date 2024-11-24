import streamlit as st # streamlit 임포트
from io import StringIO # StringIO 임포트
import pandas as pd # pandas 임포트
import matplotlib.pyplot as plt # matplotlib 임포트
import matplotlib.font_manager as fm # 코드 추가

uploaded_file = st.file_uploader("지하철 데이터를 업로드하세요.") # 파일 업로드용 인풋

if uploaded_file is not None: # BytesIO 객체
    string = uploaded_file.getvalue().decode("utf-8") # BytesIO 객체를 문자열로 변환 
    result_string = string.replace(",\"\"", "") # 해당 문자열 중 이상 문자열 제거

    df = pd.read_csv(StringIO(result_string)) # 문자열을 다시 파일화해서 read_csv 파일에 넣어줌
    df["사용일자"] = pd.to_datetime(df["사용일자"], format="%Y%m%d") # 사용일자 컬럼값들을 datetime 타입으로 변경
    df["등록일자"] = pd.to_datetime(df["등록일자"], format="%Y%m%d") # 등록일자 컬럼값들을 datetime 타입으로 변경
    
   # 코드 추가
    def register_fonts():
        font_files = fm.findSystemFonts(fontpaths=['./fonts'])
        for font_file in font_files:
            fm.fontManager.addfont(font_file)
        fm._load_fontmanager(try_read_cache=False)

    register_fonts()

    plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정

    first_line = df[df["노선명"]=="1호선"].groupby("역명", as_index=False)["하차총승객수"].mean().sort_values(by="하차총승객수", ascending=False).head(10)
    second_line = df[df["노선명"]=="2호선"].groupby("역명", as_index=False)["하차총승객수"].mean().sort_values(by="하차총승객수", ascending=False).head(10)
    third_line = df[df["노선명"]=="3호선"].groupby("역명", as_index=False)["하차총승객수"].mean().sort_values(by="하차총승객수", ascending=False).head(10)
    fourth_line = df[df["노선명"]=="4호선"].groupby("역명", as_index=False)["하차총승객수"].mean().sort_values(by="하차총승객수", ascending=False).head(10)

    st.write(second_line)

    # def remove_parenthesis_data(name):
    #     return name.split("(")[0];

    # first_line_station_names = first_line['역명'].apply(remove_parenthesis_data)
    # second_line_station_names = second_line['역명'].apply(remove_parenthesis_data)
    # third_line_station_names = third_line['역명'].apply(remove_parenthesis_data)
    # fourth_line_station_names = fourth_line['역명'].apply(remove_parenthesis_data)

    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
    # fig.suptitle("주요호선별 역별 일평균 하차승객수", fontsize=20)

    # ax1.barh(first_line_station_names, first_line['하차총승객수'], height=0.5, color=['#0052A4'])
    # ax1.set_title("1호선", loc='center', pad=20, fontsize=16, color='#0052A4')
    # ax1.set_xlabel("일평균 하차총승객수", labelpad=16)
    # ax1.set_ylabel("역명", labelpad=16)
    # ax1.tick_params(axis='x', labelsize=8)
    # ax1.tick_params(axis='y', labelsize=8)
    # ax1.grid(True, axis='x', alpha=0.4)
    # ax1.invert_yaxis()

    # ax2.barh(second_line_station_names, second_line['하차총승객수'], height=0.5, color=['#00A84D'])
    # ax2.set_title("2호선", loc='center', pad=20, fontsize=16, color='#00A84D')
    # ax2.set_xlabel("일평균 하차총승객수", labelpad=16)
    # ax2.set_ylabel("역명", labelpad=16)
    # ax2.tick_params(axis='x', labelsize=8)
    # ax2.tick_params(axis='y', labelsize=8)
    # ax2.grid(True, axis='x', alpha=0.4)
    # ax2.invert_yaxis()

    # ax3.barh(third_line_station_names, third_line['하차총승객수'], height=0.5, color=['#EF7C1C'])
    # ax3.set_title("3호선", loc='center', pad=20, fontsize=16, color='#EF7C1C')
    # ax3.set_xlabel("일평균 하차총승객수", labelpad=16)
    # ax3.set_ylabel("역명", labelpad=16)
    # ax3.tick_params(axis='x', labelsize=8)
    # ax3.tick_params(axis='y', labelsize=8)
    # ax3.grid(True, axis='x', alpha=0.4)
    # ax3.invert_yaxis()

    # ax4.barh(fourth_line_station_names, fourth_line['하차총승객수'], height=0.5, color=['#00A5DE'])
    # ax4.set_title("3호선", loc='center', pad=20, fontsize=16, color='#00A5DE')
    # ax4.set_xlabel("일평균 하차총승객수", labelpad=16)
    # ax4.set_ylabel("역명", labelpad=16)
    # ax4.tick_params(axis='x', labelsize=8)
    # ax4.tick_params(axis='y', labelsize=8)
    # ax4.grid(True, axis='x', alpha=0.4)
    # ax4.invert_yaxis()

    # plt.subplots_adjust(wspace=0.5, hspace=0.5) 

    # # plt.show()
    # st.pyplot(fig) # 그래프 출력