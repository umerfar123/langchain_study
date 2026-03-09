import streamlit as st

from pydantic import BaseModel, Field
from typing import Annotated,Optional,Literal,TypedDict,List,Dict
import numpy as np
import time
from streamlit_agraph import agraph, Node, Edge, Config

from langchain_core.output_parsers import PydanticOutputParser
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

ROBOTS = [
    {
        'name' : ['arm_1'],
        'type' : 'ARM',
        'description' : 'ARM is capable of picking and placing objects but is static at Delivery Zone and cannot navigate to other locations'
    },
    {
        'name' : ['agv_1','agv_2'],
        'type' : 'AGV',
        'description' : 'AGV is capable of navigating to Delivery Zone, Drop Zone 1, Drop Zone 2, but is not capable of picking or placing objects'
    }
    ]

OBJECTS = ['ball', 'pen', 'glass', 'mouse']
LOCATIONS = ['Delivery Zone','Drop Zone 1', 'Drop Zone 2']

LOCATION_INFO = [
    {
        'name' : 'Delivery Zone',
        'description' : 'All objects from object list are located here for pickup and only the arm_1 is located here'
    },
    {
        'name' : 'Drop Zone 1',
        'description' : 'Location for agv_1 or agv_2 to drop the objects, separate from other locations.'
    },
    {
        'name' : 'Drop Zone 2',
        'description' : 'Location for agv_1 or agv_2 to drop the objects, separate from other locations.'
    },
    ]

avatar = {'user':'./img/icons8-user-48.png',
          'ai' : './img/icons8-ai-48.png'}


# Layouts And Configs
st.set_page_config(page_title='-Lars',layout='wide')

with st.sidebar:
    
    reset = st.button('Reset Chat History',type='primary' )
    
    if reset:
        st.session_state['chat_history'] = []
    
    st.divider()
    
    planner_models = ['gpt-oss','gemma','deepseek-r1']
    master_models = ['gpt-oss','gemma','deepseek-r1']
    agent_models = ['functionGemma','Granite']
    
    st.selectbox('Planner Model :',options=planner_models)
    st.selectbox('Master Model  :',options=master_models)
    st.selectbox('Agent Model   :',options=agent_models)
    
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars",)
    if selected is not None:
        st.markdown(f"Thank You For {sentiment_mapping[selected]} Star Feedback .")

st.title('-- LARS --',text_alignment='center',width='stretch')
st.divider()

col1, col2 = st.columns([0.55,0.45],width='stretch',border=True)

# Callables
def status_callable(node:str):
    with col2:
        with st.spinner(f"Calling {node}...", show_time=True):
            time.sleep(1)
        st.success(f"{node} Is Up .....")

def arm_status_callable():
    
    with st.spinner("Checking Arm Controllers....",show_time=True):
        time.sleep(1)
    st.success("Arm Controller Is Ready")

# Session State
# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    st.session_state['plan_generated'] = False

# Display chat messages from history on app rerun
with col1:
    with st.expander('Chat History'):
        for msg in st.session_state['chat_history']:
                with st.chat_message(msg['role'],avatar=avatar[msg['role']]):
                    st.write(msg['content'],unsafe_allow_html=True)

planner_model = init_chat_model(
    model="gemma3:4b",
    model_provider="ollama",
    temperature = 0
    )

class PlannerStepSchema(BaseModel):
    step_no : int = Field(description='Denotes the current step number')
    robot_type : Literal["ARM","AGV"] = Field(description='Robot needed for executing the action')
    action : str = Field(description='The action to perform')
    dependencies : Optional[List[int]] = Field(description='Any dependency with previous step')
    
class PlannerSchema(BaseModel):
    plan : List[PlannerStepSchema]

def get_planner_prompt():
    prompt = """
    System Role: You are a Robotic Mission Planner. Your task is to decompose a complex mission into a sequence of "action"able primitives for a heterogeneous fleet of robots.
    
    The Mission: {task}

    The Robot Fleet: {robots}

    Environment Context: {locations_info}
    
    When Generating Plan :
        - Make sure that you plan does not conflict with any information you have.
        - Always keep in mind robots locations and capabilities.
        - Multi-Parent Logic: If an "action" involves two entities (e.g., an Arm placing an item on an "AGV", the step MUST depend on BOTH the Arm's previous step AND the"AGV"s previous step.
        - Gripper State: A 'place' "action" MUST depend on the 'pick' "action" for that specific object.
        - Location State: An "action" at a location MUST depend on the 'navigate' "action" to that location.
        - Understand the dependency concept from the below example.
    
    Example:
        task = 'move ball and pen to drop zone 1'
        
        {{
            "plan" : [
                        [
                            "step_no" : 1,
                            "robot_type" : "AGV",
                            "action" : "agv_1 navigates to Delivery Zone",
                            "dependencies" : []
                        ],
                        [
                            "step_no" : 2,
                            "robot_type" : "ARM",
                            "action" : "arm_1 picks ball",
                            "dependencies" : []
                        ],
                        [
                            "step_no" : 3,
                            "robot_type" : "ARM",
                            "action" : "arm_1 place ball on agv_1",
                            "dependencies" : [1,2]
                        ],
                        [
                            "step_no" : 4,
                            "robot_type" : "AGV",
                            "action" : "agv_1 navigates to Drop Zone 1",
                            "dependencies" : [3]
                        ],
                        [
                            "step_no" : 5,
                            "robot_type" : "AGV",
                            "action" : "agv_2 navigates to Delivery Zone",
                            "dependencies" : []
                        ],
                        [
                            "step_no" : 6,
                            "robot_type" : "ARM",
                            "action" : "arm_1 picks pen"
                            "dependencies" : [3]
                        ],
                        [
                            "step_no" : 7,
                            "robot_type" : "ARM",
                            "action" : "arm_1 place pen on agv_2",
                            "dependencies" : [5,6]
                        ],
                        [
                            "step_no" : 8,
                            "robot_type" : "AGV",
                            "action" : "agv_2 navigates to Drop Zone 1",
                            "dependencies" : [7]
                        ]
                    ]
        }}
        
        IMPORTANT: Return ONLY valid JSON. Do not include any variable assignments (like 'plan =') or single quotes, don't use unwanted spacing.
    """
    return prompt

def plannerLLM(task) -> PlannerSchema:
    
    model = planner_model
    
    parser = PydanticOutputParser(pydantic_object=PlannerSchema)
    
    template = PromptTemplate(
        template=get_planner_prompt(),
        input_variables=['task','robots','objects','locations','locations_info']
    )
    
    prompt = template.invoke(
        {
            'task' : task,
            'robots' : ROBOTS,
            'locations_info' : LOCATION_INFO,
        }
    )
    
    with st.chat_message('ai',avatar=avatar['ai'] ):
        ai_message = st.write_stream((chunk.content for chunk in model.stream(prompt)),cursor='..')
        st.session_state['chat_history'].append({'role':'ai','content':ai_message})
    
    plan_parsed = parser.parse(ai_message)
    return plan_parsed

def main():
    
    user_input = st.chat_input("What do you want me do",on_submit=status_callable,args=['Planner'])
    if user_input:
        st.session_state['chat_history'].append({'role':'user','content':user_input})
        
        with col1:
            with st.chat_message('user',avatar=avatar['user']):
                st.write(user_input)
            
            plan = plannerLLM(user_input)
            if isinstance(plan, PlannerSchema):
                st.session_state['plan_generated'] = True
        
        if st.session_state['plan_generated']:
            with col2:
                st.info(body='Executing Plan')
                st.divider()
                arm_status_callable()



if __name__ == '__main__':
    main()