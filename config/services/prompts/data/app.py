import io

import pandas as pd
import streamlit as st

from services.gemini_service import (
    generate_outreach,
    parse_response
)


st.set_page_config(
    page_title="Cold Outreach Personaliser",
    page_icon="✉️",
    layout="wide"
)


st.title("✉️ Cold Outreach Personaliser")

st.write(
    "Generate personalised cold outreach emails using Gemini."
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Outreach Settings")


tone = st.sidebar.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Casual",
        "Bold"
    ]
)


goal = st.sidebar.selectbox(
    "Select Goal",
    [
        "Book a meeting",
        "Introduce product",
        "Follow up",
        "Partnership",
        "Networking"
    ]
)


# -----------------------------
# TABS
# -----------------------------

single_tab, batch_tab = st.tabs(
    [
        "👤 Single Prospect",
        "📊 Batch CSV"
    ]
)


# =====================================================
# SINGLE PROSPECT
# =====================================================

with single_tab:

    st.header("Single Prospect")

    profile = st.text_area(
        "Paste Prospect Profile",
        height=220,
        placeholder=(
            "Example:\n"
            "Sarah is the Head of Marketing at Acme Technologies. "
            "She recently expanded the content marketing team "
            "and is focused on improving lead generation."
        )
    )


    if st.button(
        "✨ Generate Outreach",
        type="primary"
    ):

        if not profile.strip():

            st.warning(
                "Please enter a prospect profile."
            )

        else:

            with st.spinner(
                "Gemini is generating your personalised outreach..."
            ):

                try:

                    response = generate_outreach(
                        profile,
                        tone,
                        goal
                    )

                    result = parse_response(
                        response
                    )


                    st.success(
                        "Outreach generated!"
                    )


                    st.subheader("Subject")

                    st.text_input(
                        "Copy subject",
                        value=result["subject"]
                    )


                    st.subheader("Email")

                    st.text_area(
                        "Copy-ready email",
                        value=result["email"],
                        height=250
                    )


                    st.subheader("Follow-up")

                    st.text_area(
                        "Follow-up message",
                        value=result["followup"],
                        height=150
                    )


                except Exception as e:

                    st.error(
                        f"Error: {e}"
                    )


# =====================================================
# BATCH CSV
# =====================================================

with batch_tab:

    st.header("Batch CSV")

    uploaded_file = st.file_uploader(
        "Upload your prospect CSV",
        type=["csv"]
    )


    st.info(
        "Your CSV must contain a column named 'profile'."
    )


    if uploaded_file:

        try:

            df = pd.read_csv(
                uploaded_file
            )


            st.subheader("Original Data")

            st.dataframe(
                df,
                use_container_width=True
            )


            if "profile" not in df.columns:

                st.error(
                    "Your CSV needs a 'profile' column."
                )


            else:

                if st.button(
                    "🚀 Generate Batch Outreach",
                    type="primary"
                ):

                    subjects = []
                    emails = []
                    followups = []

                    progress = st.progress(0)

                    total = len(df)


                    for index, row in df.iterrows():

                        profile = str(
                            row["profile"]
                        )


                        try:

                            response = generate_outreach(
                                profile,
                                tone,
                                goal
                            )


                            result = parse_response(
                                response
                            )


                            subjects.append(
                                result["subject"]
                            )

                            emails.append(
                                result["email"]
                            )

                            followups.append(
                                result["followup"]
                            )


                        except Exception as e:

                            subjects.append(
                                "Generation failed"
                            )

                            emails.append(
                                str(e)
                            )

                            followups.append(
                                ""
                            )


                        progress.progress(
                            (index + 1) / total
                        )


                    df["generated_subject"] = subjects

                    df["generated_email"] = emails

                    df["generated_followup"] = followups


                    st.success(
                        "Batch generation completed!"
                    )


                    st.subheader(
                        "Generated Data"
                    )


                    st.dataframe(
                        df,
                        use_container_width=True
                    )


                    csv_data = df.to_csv(
                        index=False
                    )


                    st.download_button(
                        label="⬇️ Download CSV",
                        data=csv_data,
                        file_name="personalised_outreach.csv",
                        mime="text/csv"
                    )


        except Exception as e:

            st.error(
                f"Could not read CSV: {e}"
            )