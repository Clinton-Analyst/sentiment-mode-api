import streamlit as st
import requests

st.title("Sentiment Mode Analyzer")

api_url = "https://sentiment-mode-api.onrender.com/analyze"

user_input = st.text_area("Enter multiple sentences (one per line)")

if st.button("Analyze"):
    texts = [line for line in user_input.split("\n") if line.strip()]

    if not texts:
        st.warning("Please enter at least one sentence.")
    else:
        try:
            response = requests.post(api_url, json={"texts": texts})

            if response.status_code == 200:
                data = response.json()

                st.subheader("Results")
                for result in data["results"]:
                    st.write(result)

                st.success(f"Overall Mode: {data['mode']}")
            else:
                st.error(response.json()["detail"])

        except Exception as e:
            st.error(f"Connection error: {e}")
