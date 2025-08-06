import streamlit as st
import requests

st.set_page_config(page_title="Quantum-AI Password Generator", page_icon="🔐")
tabs = st.tabs(["🔐 Password Generator", "🧠 How Quantum Works?"])

# ---------------------- TAB 1: PASSWORD GENERATOR ----------------------
with tabs[0]:
    st.title("🔐 Quantum-AI Password Generator")
    st.caption("Powered by Qiskit + PyTorch + Flask API")

    st.sidebar.header("Customize your password")
    password_length = st.sidebar.slider("Length", 8, 24, 12)
    include_uppercase = st.sidebar.checkbox("Include Uppercase Letters", True)
    include_lowercase = st.sidebar.checkbox("Include Lowercase Letters", True)
    include_numbers = st.sidebar.checkbox("Include Numbers", True)
    include_symbols = st.sidebar.checkbox("Include Symbols", True)

    if st.button("Generate Secure Password"):
        try:
            res = requests.get("http://127.0.0.1:5000/generate_password", params={
                "length": password_length,
                "uppercase": include_uppercase,
                "lowercase": include_lowercase,
                "numbers": include_numbers,
                "symbols": include_symbols
            })

            if res.status_code == 200:
                data = res.json()
                st.success("✅ Password Generated Successfully!")
                st.code(data['generated_password'], language='text')
                with st.expander("🔍 See Quantum Entropy Info"):
                    st.json(data)
            else:
                st.error(f"❌ Error: {res.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"Connection error: {e}")
    else:
        st.info("Customize options from the sidebar and click Generate.")

# ---------------------- TAB 2: HOW QUANTUM WORKS ----------------------
with tabs[1]:
    st.title("🧠 How Quantum Randomness Works")
    st.markdown("""
    Quantum computing uses the principles of quantum mechanics to generate **true randomness**, unlike classical computers which produce pseudo-random numbers.

    ### 🔸 Step-by-Step Process:
    1. **Quantum Superposition**  
       Each qubit is placed in a state of both 0 and 1 simultaneously using the **Hadamard gate**.

    2. **Quantum Measurement**  
       When we measure the qubit, it collapses to 0 or 1 randomly — this is **true physical randomness**.

    3. **Binary to Decimal Seed**  
       The result is a binary string (like `0110101...`) converted to a numeric seed.

    4. **AI Password Generation**  
       This seed drives our AI logic to produce a unique and secure password.

    ### 💡 Why It Matters:
    - Quantum randomness is **non-deterministic** — even the computer can’t predict the outcome.
    - Adds a layer of **entropy and unpredictability** ideal for password generation.

    ### 🧪 Visualization:
    Imagine flipping a perfectly fair coin — but at the atomic level, and with thousands of them at once.
    """)
