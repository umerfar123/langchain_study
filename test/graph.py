import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge

st.set_page_config(layout="wide")
st.title("LangGraph Workflow: Planner to Multi-Chain Execution")

# --- 1. Define Nodes ---
nodes = [
    # External Input
    StreamlitFlowNode('planner', (450, 0), {'content': 'Planner (Input)'}, 'input', style={'backgroundColor': '#FFC107'}),

    # Master Node
    StreamlitFlowNode('master', (450, 150), {'content': 'Master Agent'}, 'default', style={'backgroundColor': '#9C27B0', 'color': 'white'}),

    # --- PARALLEL CHAIN (Container) ---
    StreamlitFlowNode('parallel_container', (50, 250), {'content': 'Parallel Chain'}, 'default', 
                      style={'width': '350px', 'height': '250px', 'backgroundColor': 'rgba(0, 255, 0, 0.05)', 'border': '2px dashed green'}),
    
    StreamlitFlowNode('p_arm', (30, 60), {'content': 'ARM\n(Pick/Place)'}, 'default', parentId='parallel_container', style={'backgroundColor': '#2196F3', 'color': 'white'}),
    StreamlitFlowNode('p_agv', (200, 60), {'content': 'AGV\n(Navigation)'}, 'default', parentId='parallel_container', style={'backgroundColor': '#E91E63', 'color': 'white'}),

    # --- SEQUENTIAL CHAIN (Container) ---
    StreamlitFlowNode('sequential_container', (500, 250), {'content': 'Sequential Chain'}, 'default', 
                      style={'width': '350px', 'height': '250px', 'backgroundColor': 'rgba(0, 0, 255, 0.05)', 'border': '2px dashed blue'}),
    
    StreamlitFlowNode('s_arm', (100, 50), {'content': 'ARM\n(Pick/Place)'}, 'default', parentId='sequential_container', style={'backgroundColor': '#2196F3', 'color': 'white'}),
    StreamlitFlowNode('s_agv', (100, 150), {'content': 'AGV\n(Navigation)'}, 'default', parentId='sequential_container', style={'backgroundColor': '#E91E63', 'color': 'white'}),
]

# --- 2. Define Edges ---
edges = [
    # Input to Master
    StreamlitFlowEdge('planner-master', 'planner', 'master', animated=True),

    # Master to Chains
    StreamlitFlowEdge('master-parallel', 'master', 'parallel_container', label='parallel branch'),
    StreamlitFlowEdge('master-sequential', 'master', 'sequential_container', label='sequential branch'),

    # Inside Sequential (ARM goes first, then AGV)
    StreamlitFlowEdge('s-logic', 's_arm', 's_agv', animated=True),

    # Connecting back to Master
    StreamlitFlowEdge('parallel-back', 'parallel_container', 'master', label='sync', style={'strokeDasharray': '5 5'}),
    StreamlitFlowEdge('sequential-back', 'sequential_container', 'master', label='complete', style={'strokeDasharray': '5 5'})
]

# --- 3. Render ---
streamlit_flow(
    'langgraph_flow', 
    nodes, 
    edges, 
    height=700, 
    fit_view=True, 
    show_controls=True, 
    show_background=True
)