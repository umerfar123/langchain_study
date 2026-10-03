st.markdown(
    """
    <style>
        /* 1. Flip the entire message row (Avatar to the right) */
        [data-testid="stChatMessage"]:has(div[aria-label="Chat message from user"]) {
            flex-direction: row-reverse;
            text-align: right;
        }

        /* 2. Fix the alignment of the text container itself */
        [data-testid="stChatMessage"]:has(div[aria-label="Chat message from user"]) [data-testid="stChatMessageContent"] {
            display: flex;
            flex-direction: column;
            align-items: flex-end; /* This pushes the text block to the right */
            width: 100%;
        }

        /* 3. Ensure the actual text inside the markdown behaves */
        [data-testid="stChatMessage"]:has(div[aria-label="Chat message from user"]) [data-testid="stChatMessageContent"] div {
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)