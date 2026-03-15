st.markdown(
    """
    <style>
        /* 1. Flip the entire row so avatar is on the right */
        [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
            flex-direction: row-reverse;
        }

        /* 2. Target the text container inside the user message to align text right */
        [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
            text-align: right;
            width: 100%;
        }

        /* 3. Ensure the markdown paragraph inside also obeys the alignment */
        [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) p {
            justify-content: flex-end;
            display: flex;
        }
    </style>
    """,
    unsafe_allow_html=True,
)