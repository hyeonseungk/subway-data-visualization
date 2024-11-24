import streamlit as st # streamlit 임포트
from io import StringIO # StringIO 임포트
import pandas as pd # pandas 임포트

uploaded_file = st.file_uploader("지하철 데이터를 업로드하세요.") # 파일 업로드용 인풋

if uploaded_file is not None: # BytesIO 객체
    string = uploaded_file.getvalue().decode("utf-8") # BytesIO 객체를 문자열로 변환 
    result_string = string.replace(",\"\"", "") # 해당 문자열 중 이상 문자열 제거

    df = pd.read_csv(StringIO(result_string)) # 문자열을 다시 파일화해서 read_csv 파일에 넣어줌
    df["사용일자"] = pd.to_datetime(df["사용일자"], format="%Y%m%d") # 사용일자 컬럼값들을 datetime 타입으로 변경
    df["등록일자"] = pd.to_datetime(df["등록일자"], format="%Y%m%d") # 등록일자 컬럼값들을 datetime 타입으로 변경
    st.write(df)