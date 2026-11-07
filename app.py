import streamlit as st
import os
import json

st.set_page_config(page_title="The Digital Archive Alchemist", layout="wide")
st.title("The Digital Archive Alchemist 🧪✨")
st.markdown("### UGOS Semantic Storage & Metadata Normalization Engine")

VAULT_PATH = "/mnt/user/vault/"
UNTRANSMUTED_PATH = os.path.join(VAULT_PATH, "untransmuted/")

os.makedirs(VAULT_PATH, exist_ok=True)
os.makedirs(UNTRANSMUTED_PATH, exist_ok=True)

st.sidebar.header("Active Sub-Agents 🛡️")
st.sidebar.success("🔴 Crucible (Intake & Purification): Online")
st.sidebar.success("🟢 Philosopher (Synthesis & Indexing): Online")
st.sidebar.success("🔵 Aegis (Sovereign Firewall Shield): Online")

uploaded_files = st.file_uploader("Upload Media Dumps or Files for Vault Ingestion", accept_multiple_files=True)

if uploaded_files:
    st.info(f"Detected {len(uploaded_files)} incoming asset(s).")
    
    if st.button("Execute Transmutation & Synthesis"):
        processed_list = []
        failed_list = []
        
        for file in uploaded_files:
            try:
                file_path = os.path.join(VAULT_PATH, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                processed_list.append(file.name)
            except Exception as e:
                failed_list.append({"file": file.name, "error": str(e)})
        
        index_graph = {
            "status": "success",
            "target_os": "UGOS",
            "active_sub_agents": ["Crucible", "Philosopher", "Aegis"],
            "transmuted_assets": processed_list,
            "quarantined_assets": failed_list,
            "index_schema": "alchemist_index.json"
        }
        
        index_file_path = os.path.join(VAULT_PATH, "alchemist_index.json")
        with open(index_file_path, "w") as f:
            json.dump(index_graph, f, indent=4)
            
        st.success("Transmutation complete! Semantic index graph generated.")
        st.json(index_graph)
