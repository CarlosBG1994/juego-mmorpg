import os
from typing import Any

try:
    import streamlit as st
except Exception:
    st = None


def get_secret(key: str, default: str = "") -> str:
    if st is not None:
        try:
            if key in st.secrets:
                val = st.secrets[key]
                if isinstance(val, str) and val.strip():
                    return val.strip()
        except Exception:
            pass
    env_val = os.getenv(key, default)
    return env_val.strip() if isinstance(env_val, str) else default


def get_firebase_config() -> dict[str, Any] | None:
    if st is not None:
        try:
            if "firebase" in st.secrets:
                data = dict(st.secrets["firebase"])
                if data.get("project_id") and data.get("private_key"):
                    if isinstance(data["private_key"], str):
                        data["private_key"] = data["private_key"].replace("\\n", "\n")
                    return data
        except Exception:
            pass
    return None