import streamlit as st

def main():
    
    pages = {
        "Home" : [st.Page('lars_home.py',title='Lars')],
        "Try Me" : [st.Page('lars_ui.py',title='Execute Action')],
        "Status" : [st.Page('lars_graph.py',title='Action Status'),
                    st.Page('lars_graph2.py',title='Robot Status')]
         }

    selected_page = st.navigation(pages,position='top',expanded=False)
    selected_page.run()

if __name__ == '__main__':
    main()
