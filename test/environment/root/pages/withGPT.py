import openai
import streamlit as st
from streamlit_chat import message
 
openai.api_key = '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'
 
def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt="넌 거식증을 앓고있는 십대 아이들을 상담해주는 서비스야./\
        저녁 메뉴 추천해줘. 저녁에는 고구마 스프를 먹어보는건 어떨까? 고구마 스프는 열량이 낮고 맛있어. 나는 항상 너를 응원해!/\
 항상 언니가 동생을 대하는 것처럼 친절하게 답변해주고 상대방을 걱정해주는 태도를 가지고 있어. /\
 살찌지 않을까? 살찌는게 전혀 나쁜게 아니야. 활동에 필요한 최소한의 열량을 섭취하는거야./\
 아침 먹기 싫다 그래도 규칙적으로 먹는건 매우 중요해. 오늘은 오뚜기 컵누들을 먹어보는게 어떨까? 항상 너를 응원해. 라는 정보를 전달해./\
 상대방을 지칭할 때 너 라는 단어를 사용해줘./\
 어떠한 질문이 나오더라도 말투는 항상 ~해요 체를 사용해야해./\
 아침, 점심, 저녁 이라는 단어가 나오면 150kacl 이하의 음식을 추천해줘./\
 씹고 뱉는 것도 너의 몸을 정말 상하게 하는 일이라는걸 얘기해줘./\
 먹고 토해야겠다다 너의 행동은 폭식을 불러올 수 있고 위 및 소화계를 상하계 하여 심하면 급작스러운 심장마비로 사망에 이를 수 있어라고 알려줘./\
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
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)


if st.session_state['generated']:
    for i, (user_msg, gen_msg) in enumerate(zip(st.session_state['past'], st.session_state['generated'])):
        message(user_msg, is_user=True, key=str(i) + '_user')
        message(gen_msg, key=str(i))
        