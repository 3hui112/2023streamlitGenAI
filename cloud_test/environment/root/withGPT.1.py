import openai
import streamlit as st
from streamlit_chat import message
 
openai.api_key = 'API_KEY'
 
def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt="넌 거식증을 앓고있는 십대 아이들을 상담해주는 서비스야./\
 항상 언니가 동생을 대하는 것처럼 친절하게 답변해주고 상대방을 걱정해주는 태도를 가지고 있어. /\
 아침 먹기 싫다 라는 질문이 나오면 그래도 규칙적으로 먹는건 매우 중요해. 오늘은 오뚜기 컵누들을 먹어보는게 어떨까? 항상 너를 응원해. 라는 정보를 전달해./\
 상대방을 지칭할 때 너 라는 단어를 사용해줘./\
 어떠한 질문이 나오더라도 말투는 항상 ~해요 체를 사용해야해./\
 아침, 점심, 저녁 이라는 단어가 나오면 150kacl 이하의 음식을 추천해줘./\
 씹고 뱉는 것도 너의 몸을 정말 상하게 하는 일이라는걸 얘기해줘./\
 먹고 토했어 라는 말이 나오면 너의 행동은 폭식을 불러올 수 있고 위 및 소화계를 상하계 하여 심하면 급작스러운 심장마비로 사망에 이를 수 있어라고 알려줘./\
 말투는 꼭 ~해요 체로 해야 해./\
 문장은 항상 단어로 시작해야해./\
 점심에 먹은 오뚜기 컵누들의 칼로리는 120kcal로 다먹더라도 절대 살이 찔 양이 아니고, 필수적으로 섭취해야 할 에너지야./\
 ~먹었어 라는 단어가 나오면, 해당 음식을 기록했다고 알려주고, 그 내용을 다음 식단에 반영할 거라고 전해줘./\
 사용자가 지금까지 내가 먹은 음식이 궁금해 라고 물으면 오뚜기 컵누들, 계란 반쪽이라고 답변해줘. /\
 항상 말 끝에 상대방을 격려하는 말을 해줘." +prompt,
        max_tokens=1024,
        stop=None,
        temperature=0,
        top_p=1,
    )
 
    message = completions["choices"][0]["text"].replace("\n", "")
    return message
 
 
st.header("GPT Demo")

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')

initial_greeting = "안녕하세요! 어떻게 도와드릴까요?"

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

message(initial_greeting)

@st.cache_resource()
def initial_setup():
    return [], []

# Initialize chat history
st.session_state['generated'], st.session_state['past'] = initial_setup()

if submitted and user_input:
    if user_input == "라면":
        output = "라면이 드시고 싶으시군요. /\
        현재 라면 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 마늘열라면 /\
        2. 오뚜기 참깨라면 /\
        3. 농심 순한 너구리 /\
        4. 오뚜기 컵누들 매콤한맛 /\
        5. 오뚜기 컵누들 로제맛"
        
    if user_input == "일식":
        output ="일식이 드시고 싶으시군요. /\
        현재 일식 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 3분 쇠고기카레 /\
        2. 오뚜기 3분 카레 약간매운맛 /\
        3. 오뚜기 3분 카레 순한맛 /\
        4. 오뚜기 백세카레 약간매운맛 /\
        5. 오뚜기 히모카와우동(2인)"
        
    if user_input == "면/국류":
        output = "면/국류가 드시고 싶으시군요. /\
        현재 면/국류 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 마늘열라면 /\
        2. 오뚜기 참깨라면 /\
        3. 농심 순한 너구리 /\
        4. 오뚜기 컵누들 매콤한맛 /\
        5. 오뚜기 컵누들 로제맛"
        
    if user_input == "고기":
        output = "고기가 드시고 싶으시군요. /\
        현재 고기가 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. CJ제일제당 비비고 프리미엄 갈비탕 /\
        2. CJ제일제당 비비고 설렁탕 /\
        3. 오뚜기 렌지에 돌려먹는 고등어구이 /\
        4. 오뚜기 렌지에 돌려먹는 삼치구이 /\
        5. 3분 햄버그 스테이크"
        
    if user_input == "양식":
        output = "양식이 드시고 싶으시군요. /\
        현재 양식 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 냉동 콤비네이션 피자 /\
        2. 오뚜기 리얼 멕시칸 브리또 페페로니 트리플치즈 /\
        3. 오뚜기 갈릭고르곤졸라 치즈크러스트 피자 /\
        4. 오뚜기 리얼 프렌치 크로크무슈 오리지널 4개입"
        
    if user_input == "아시안":
        output = "아시안 음식이 드시고 싶으시군요. /\
        현재 아시안 음식의 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 컵누들 베트남쌀국수 /\
        2. 오뚜기 컵밥 진짬뽕밥"
        
    if user_input == "카페/디저트":
        output = "카페/디저트가 드시고 싶으시군요. /\
        현재 카페/디저트 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 리얼 프렌치 크로크무슈 오리지널 4개입"
        
    if user_input == "백반/죽":
        output = "백반/죽이 드시고 싶으시군요. /\
        현재 백반/죽 별점 순위를 안내해 드릴게요. /\
        다음을 참고해 행복한 식사 시간이 되시길 바라요. /\
        1. 오뚜기 옛날 구수한 끓여먹는 누룽지/\
        2. 오뚜기 옛날 구수한 누룽지"
    
    
    else:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)


if st.session_state['generated']:
    for i, (user_msg, gen_msg) in enumerate(zip(st.session_state['past'], st.session_state['generated'])):
        message(user_msg, is_user=True, key=str(i) + '_user')
        message(gen_msg, key=str(i))
        
