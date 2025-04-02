# -*- codi     ng: utf-8 -*-

import streamlit as st
import pandas as pd
import pyarrow as pa

st.set_page_config(layout="wide")
#.streamlit/config.toml 파일에서 maincolor 지정 : 파란색

st.subheader('병역처분결과에 대해 알려드립니다')

with st.expander('😄 알려드립니다'):
  st.write('병역판정검사(입영판정검사) 결과지 내용에 대해 궁금한 사항을 안내합니다.')
  st.image('https://mma.go.kr/download/visual/CAIS_HPIS_202412020402149250.jpg', width=250)

#사이드바 옵션
#st.sidebar.header('입력')
#user_name = st.sidebar.selectbox('병역처분 결과를 입력하세요', ['','현역입영대상','사회복무요원소집대상','전시근로역','병역면제','재검대상'])
#user_emoji = st.sidebar.selectbox('검사결과 중 어떤 항목이 궁금하신가요?', ['', '체질량지수','혈압','색각','AST','ALT','간염','Gloucoss'])
#user_food = st.sidebar.selectbox('가장 좋아하는 음식은?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

#탭메뉴의 글자크기 지정
css = ''' 
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:15px;
    }

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }
	.stTabs [data-baseweb="tab"] {
		height: 30px;
        white-space: pre-wrap;
		background-color: #ffffff;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
          padding-right: 10px;
		padding-bottom: 10px;
          padding-left: 10px;
    }
	.stTabs [aria-selected="true"] {
  		#background-color: #0000ff;
          #color: #FFFFFF;
	}
</style>
'''

tab1, tab2, tab3 = st.tabs(['병역처분','검사참고치','바로가기']) #탭메뉴 가로형

st.markdown(css, unsafe_allow_html=True)

with tab1:
     st.subheader('병역처분결과를 입력하세요', divider=True)
     #st.markdown("##### 병역처분결과를 입력하세요")
     #st.divider()
     user_name = st.selectbox('',['','현역입영대상','사회복무요원소집대상','전시근로역','병역면제','재신체검사대상'], label_visibility = 'hidden')


     if user_name != '':
          #st.subheader(', divider=True)
          st.markdown(f"#### 🎯 {user_name}")
     else:
          st.markdown('')

     if user_name == '현역입영대상' :
          st.write('1-3급은 현역입영대상입니다')
     elif user_name == '사회복무요원소집대상' :
          #st.write(f'👉 4급은 사회복무요원 소집 대상입니다')
          st.write(f'➡️ 사회복무요원제도')
          st.markdown(f'- 국가기관, 지방자치단체, 공공단체 및 사회복지시설의 공익목적 수행에 필요한 사회복지, 보건의료, 교육문화, 환경안전 등의 사회서비스 업무 및 행정업무등의 지원을 위한 병역의무의 한 형태로 운영하는 제도입니다.') 
     
          with st.expander('📢 대상'):
               st.write('병역판정검사 결과 보충역으로 병역처분된 사람')
          with st.expander('🏟️ 복무분야'):
               st.write('국가기관, 지방자치단체, 공공단체 및 사회복지시설의 사회복지, 보건의료, 교육문화, 환경안전 등의 사회서비스 업무 및 행정업무 등의 지원업무')
          with st.expander('🗓️ 복무기간'):
               st.write('21개월')
          with st.expander('✍🏼 복무형태'):
               st.write('출·퇴근 근무하며 소속기관장의 지휘감독을 받음')
          with st.expander('💵 처우'):
               st.write('현역병 봉급 상당액의 보수 및 직무수행에 필요한 여비 등 지급')

          st.divider()
          st.write(f'➡️ 사회복무요원 소집일자 및 복무기관 결정')
          st.markdown(f'- 사회복무요원 소집 신청은 본인이 직접 신청하는 본인선택과 신청하지 않은 사람에 대해 주소지 관할 지방병무청장이 소집순서에 따라 일자와 기관을 결정하는 직권통지로 구분됩니다.') 
     
          with st.expander('🏅 본인선택'):
               st.markdown(':blue-background[**신청시기**]')
               st.write('다음연도 소집일자 및 복무기관 본인선택은 1차(11월 중)와 2차(12월 중)로 나누어 신청을 받으며, '+'**탈락횟수, 나이 등 선발기준에 의해 선발**')
               st.markdown(':blue-background[**신청방법(본인인증)**]')
               st.write('1차 : 병무청 누리집 → 민원신청 → 병무민원 → 사회복무 → 재학생 및 국외입영연기자 소집신청(선발)')
               st.write('2차 : 병무청 누리집 → 민원신청 → 병무민원 → 사회복무 → 소집일자 및 복무기관 본인선택(선발)')
               st.write(':blue[- _접수시기, 선발기준 등은 변동가능, 병무청 누리집 공지 참고_]')
          with st.expander('📌 지방병무청 직권통지'):
               st.write('본인선택하지 않은 별도·일반 소집대상으로 관할 지방병무청에서 연중 선발')

          st.divider()
          st.write(f'➡️ 사회복무요원 현역복무 희망 신청')
          st.markdown(f'- 사회복무요원(복무중인 경우 포함)이 현역 복무를 희망하는 경우 신청합니다.') 
     
          with st.expander('📝 신청대상'):
               st.write('사회복무요원 소집대상, 사회복무요원으로 복무 중인 사람')
               st.write('(단, 남은 복무기간이 현역의 복무기간으로 환산했을때 6개월 이상 남은 사람으로 한함)')
               st.write(':blue[- _수형사유 보충역 및 현역부적합 심사에 따른 보충역은 비대상_]')
          with st.expander('🚩 처리절차'):
               st.write('신청서 제출 → 대상여부 확인 → 신체검사 없이 병역처분 변경(현역병입영 대상자) → 현역병입영 대상자로 처분변경 후 현역병 입영신청 또는 모집병 지원')
          with st.expander('📊 신청방법'):
               st.write('병무청 누리집 → 민원신청 → 병무민원 → 병역판정검사 → 사회복무요원 현역복무희망 병역처분변경 신청')
               st.write(':blue[- _신청은 1회로 제한, 신청에 따라 현역병입영 대상자로 변경된 사람은 신청을 취소할 수 없음_]')


     elif user_name == '전시근로역' :
          st.write('병역판정검사 또는 신체검사 결과 현역 또는 보충역 복무는 할 수 없으나 전시근로소집에 의한 군사지원 업무는 감당할 수 있다고 결정된 사람')
          st.write('군복무 및 예비군도 면제되며, 민방위에 편성되어 관련 교육 등을 받게 됩니다. 추후 민방위 편성 및 교육관련 문의는 주소지 읍·면·동 주민자치센터로 문의하시면 됩니다.')
     elif user_name == '병역면제' :
          st.write('현역, 보충역, 예비군, 민방위, 전시근로역 등의 모든 병역의무가 완전히 면제되는 것으로 평시든 전시든 병역과 관련된 어떤 의무도 없습니다.')
     elif user_name == '재신체검사대상' :
          st.write('병역판정검사 시 신체등급 7급으로 질병치료 후 다시 검사를 받는 사람입니다.')
     else: 
          st.write('')

with tab2:
     st.subheader('검사결과 중 어떤 항목이 궁금하신가요?', divider=True)

     if 'kkk' not in st.session_state:
          st.session_state['kkk'] = '체질량지수'

     if st.button('체질량지수', use_container_width=True):
          st.session_state['kkk'] = '체질량지수'
          st.rerun()
     if '체질량지수'==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다.', divider=True)
          st.write('체질량지수(BMI : Body Mass Index)는 신장과 체중의 비율을 사용한 체중의 객관적인 지수를 말합니다.')

     if st.button('안과', use_container_width=True):
          st.session_state['kkk'] = '안과'
          st.rerun()
     if "안과"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다.', divider=True)
          st.write('맨눈(나안)시력 0.3이하인 사람은 정밀검사를 실시합니다. (정밀검사 결과는 결과지 하단에 기록됩니다.)')

     if st.button('혈압', use_container_width=True):
          st.session_state['kkk'] = '혈압'
          st.rerun()
     if "혈압"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('이완기 혈압 90, 수축기 혈압 140 미만 시 정상입니다.')
          v1, v2 = st.slider("❓ 혈압수치의 이완기와 수축기 수치를 입력하세요.", 40, 200, (90, 140))
          if v1 <= 90 and v2 <= 140:
               st.write(f"혈압  이완기({v1}), 수축기({v2}) : 🟢 정상입니다.") 
          else:
               st.write(f"혈압  이완기({v1}), 수축기({v2}) : 🔴 이상입니다.")

     if st.button('AST', use_container_width=True): #0-2304
          st.session_state['kkk'] = 'AST'
          st.rerun()
     if "AST"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.markdown('간세포 내에 존재하는 효소로 간 손상 시 혈중으로 유출되어 혈중 수치가 증가하게 됩니다.\n'
                      ' 정상범위는 0 ~ 40 IU/L 이하입니다')
          v = st.slider("❓ 검사결과지의 AST수치를 입력하세요", 0, 100, 40)
          if v <= 40:
               st.write(f"AST수치 {v} : 🟢 정상입니다") 
          elif v > 40:
               st.write(f"AST수치 {v} : 🔴 이상입니다") 


     if st.button('ALT', use_container_width=True): #0~1230
          st.session_state['kkk'] = 'ALT'
          st.rerun()
     if "ALT"==st.session_state.kkk: 
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('간세포 내에 존재하는 효소로 간 손상 시 혈중으로 유출되어 혈중 수치가 증가하게 됩니다. 주로 간에만 존재합니다. 간염을 발견하기에 가장 효과적인 검사 항목 중 하나입니다. 정상범위는 0 ~ 41 IU/L입니다.')
          v = st.slider("❓ 검사결과지의 ALT수치를 입력하세요", 0, 100, 41)
          if v <= 41:
               st.write(f"ALT수치 {v} : 🟢 정상입니다") 
          elif v > 41:
               st.write(f"ALT수치 {v} : 🔴 이상입니다") 


     if st.button('간염', use_container_width=True): 
          st.session_state['kkk'] = '간염'
          st.rerun()
     if "간염"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('B형간염과 C형간염으로 나눠집니다. 정상범위는 음성입니다')

     if st.button('단백뇨', use_container_width=True):
          st.session_state['kkk'] = '단백뇨'
          st.rerun()
     if "단백뇨"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('소변 내에 과도한 단백질이 섞여 나오는 것을 말합니다. 신장기능이 저하되면 사구체에서 여과된 단백질을 재흡수해서 혈액으로 되돌려보내지 못하고 소변으로 단백질이 나옵니다. 정상범위는 1+ 이하입니다.')
     
     if st.button('혈뇨', use_container_width=True):
          st.session_state['kkk'] = '혈뇨'
          st.rerun()
     if "혈뇨"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('혈노란 소변에 비정상적인 양의 적혈구가 섞여 나오는 질환을 말합니다. 정상범위는 적혈구 0~4개입니다.')

     if st.button('Glucose', use_container_width=True):
          st.session_state['kkk'] = 'Glucose'
          st.rerun()
     if "Glucose"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('공복 혈당은 8시간 이상의 공복상태에서 혈액, 즉 혈장 속의 포도당 농도입니다. 정상범위는 74~106 mg/dL입니다')
          v = st.slider("❓ 검사결과지의 Glucoss수치를 입력하세요", 0, 200, 100)
          if v <= 106 and v >= 74:
               st.write(f"Glucose수치 {v} : 🟢 정상입니다") 
          else:
               st.write(f"Glucose수치 {v} : 🔴 이상입니다") 

     if st.button('HbA1c', use_container_width=True):
          st.session_state['kkk'] = 'HbA1c'
          st.rerun()
     if "HbA1c"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('지난 2~3개월 동안의 혈당의 평균치를 평가하는 것으로 혈중 포도당 수치가 높을수록 더 많은 당화혈색소가 생성됩니다. 정상범위는 4~6%입니다.(혈당 126이상시 검사)')

     if st.button('WBC', use_container_width=True): #0~221.3
          st.session_state['kkk'] = 'WBC'
          st.rerun()
     if "WBC"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('백혈구수가 1,000mm³가 넘으면 백혈구증가증으로 판단합니다. 반대로 비정상적으로 백혈구가 감소한 상태는 백혈구감소증이라 부릅니다. 정상범위는 4.0~10.0 X 10³/μL입니다')
          v = st.slider("❓ 검사결과지의 WBC수치를 입력하세요", 0, 20, 10)
          if v <= 10 and v >= 4:
               st.write(f"WBC수치 {v} : 🟢 정상입니다") 
          else:
               st.write(f"WBC수치 {v} : 🔴 이상입니다")

     if st.button('RBC', use_container_width=True): #0~8.44
          st.session_state['kkk'] = 'RBC'
          st.rerun()
     if "RBC"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('혈액 내 적혈구가 감소하거나 낮으면 혈액이 운반하는 능력이 저하되어 빈혈이 발생합니다. 정상범위는 4.2~6.3 X 10⁶/μL입니다')
          v = st.slider("❓ 검사결과지의 RBC수치를 입력하세요", 0.0, 10.0, 6.3)
          if v <= 6.3 and v >= 4.2:
               st.write(f"RBC수치 {v} : 🟢 정상입니다") 
          else:
               st.write(f"RBC수치 {v} : 🔴 이상입니다")

     if st.button('Hb', use_container_width=True): #0~20
          st.session_state['kkk'] = 'Hb'
          st.rerun()
     if "Hb"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('Hb(Hemoglobin)은 혈액 속의 적혈구에 있는 단백질로, 혈색소라고도 합니다. 혈색소는 몸 전체에 산소를 운반하는 역할을 합니다. 정상범위는 13.7~17.5g/dL입니다')
          v = st.slider("❓ 검사결과지의 HB수치를 입력하세요", 0.0, 25.0, 17.5)
          if v <= 17.5 and v >= 13.7:
               st.write(f"HB수치 {v} : 🟢 정상입니다") 
          else:
               st.write(f"HB수치 {v} : 🔴 이상입니다")

     if st.button('PLT', use_container_width=True):
          st.session_state['kkk'] = 'PLT'
          st.rerun()
     if "PLT"==st.session_state.kkk:
          st.subheader(f'👉 ' + st.session_state['kkk'] + ' 안내입니다', divider=True)
          st.write('혈소판은 혈관이 손상되었을 때 혈장에서 일어나는 응고과정에 관여합니다. 정상범위는 130 ~ 400 X 10³/μL입니다')
          v = st.slider("❓ 검사결과지의 PLT수치를 입력하세요", 0, 500, 130)
          if v <= 400 and v >= 130:
               st.write(f"PLT수치 {v} : 🟢 정상입니다") 
          else:
               st.write(f"PLT수치 {v} : 🔴 이상입니다")


     if st.session_state.kkk == False:
          st.session_state.kkk=''


with tab3:
     st.write('아래 링크를 누르시면 병무청 민원포털로 연결됩니다.')
     st.write('인증이 필요한 화면입니다.')
     st.link_button("건강검진 결과서 바로가기", "https://mwpt.mma.go.kr/caisBMHS/index_mwps.jsp?menuNo=22255")

     st.link_button("현역병 본인선택안내 바로가기", "https://www.mma.go.kr/contents.do?mc=mma0000728")


     st.markdown('# 마크다운 1')
     st.markdown('## 마크다운 2')
     st.markdown('### 마크다운 3')
     st.markdown('#### 마크다운 4')
     st.markdown('**_마크다운 진하게&기울임_**')
     st.markdown('- 마크다운 글 머리\n'
			' - 마크다운')       # 이런 식으로 - 앞 뒤에 공백 추가하면, 들여쓰기도 가능함!
     st.divider()

     st.markdown("*Streamlit* is **really** ***cool***.")
     st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
     st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

     multi = '''If you end a line with two spaces,
     a soft return is used for the next line.

     Two (or more) newline characters in a row will result in a hard return.
     '''
     st.markdown(multi)
     
st.divider()

#st.write("st.session_state 객체:", st.session_state)
