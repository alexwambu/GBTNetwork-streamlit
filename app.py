import streamlit as st
import requests

st.set_page_config(page_title="GBTNetwork Interface", page_icon="🌐")

st.title("🌐 GBTNetwork Dashboard")
st.image("https://raw.githubusercontent.com/openai-user-assist/GBTNetworkAssets/main/logo.png", width=150)

rpc_url = "https://gbtnetwork-backend.onrender.com"

st.markdown("### Enter your wallet address to check GBT balance:")
address = st.text_input("Wallet Address")

if st.button("Get Balance"):
    if not address.startswith("0x") or len(address) != 42:
        st.error("Invalid Ethereum address.")
    else:
        try:
            res = requests.get(f"{rpc_url}/balance/{address}")
            data = res.json()
            st.success(f"Balance: {int(data['balance']) / 1e18:,.2f} GBT")
        except Exception as e:
            st.error("Failed to connect to GBTNetwork RPC")

st.markdown("------")
st.markdown("MetaMask Config: [Click to Copy]")
st.code(f"""
Network Name: GBTNetwork
RPC URL: {rpc_url}
Chain ID: 999
Symbol: GBT
""")
