# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 06:21:49 2026

@author: abena
"""

import streamlit as st

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Abenathi Nqweniso | Research Profile",
    page_icon="🧬",
    layout="wide"
)


# TOP BANNER IMAGE (Molecular Biology + Proteomics)

st.image(
    "banner.png",
    use_container_width=True
)


# MAIN TITLE

st.title("🧬 Abenathi Nqweniso — Research Profile")

st.markdown(
    """
    Welcome to my Academic Research Portfolio.  
    My Research interests include: **Structural Bioinformatics, Cancer Proteostasis, Drug Discovery, and Molecular Biology**.
    """
)


# SIDEBAR NAVIGATION

st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to:",
    [
        "About Me",
        "Current MSc Project",
        "Previous Projects",
        "Lab & Computational Skills",
        "Supervisor & Institution",
        "CV & ORCID"
    ]
)


# ABOUT ME SECTION

if section == "About Me":
    st.header("👩🏽‍🔬 About Me")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "profile.jpg",
            width=200,
            caption="Profile Photo"
        )

    with col2:
        st.write(
            """
            Hi! My name is **Abenathi Nqweniso**.

            I am a MSc student in Bioinformatics at **Rhodes University** with a strong interest in:

            - Molecular Biology & Proteostasis   
            - Computational Drug Discovery  
            - Bioinformatics & Protein Interactions  
            - Antimicrobial Resistance Research  
            """
        )


# CURRENT MSC PROJECT SECTION

elif section == "Current MSc Project":
    st.header("Current MSc Research Project")

    st.subheader(
        "Identifying selective pan-inhibitors of *Klebsiella pneumoniae* and *Acinetobacter baumannii* using computational methods"
    )

    st.write(
        """
        This MSc project focuses on using **computational drug discovery approaches**
        to identify selective pan-inhibitors against two major antibiotic-resistant pathogens:

        - *Klebsiella pneumoniae*
        - *Acinetobacter baumannii*

        **Key methods include:**

        - Virtual screening  
        - Molecular docking  
        - Protein-ligand interaction analysis  
        - Bioinformatics-based target identification  
        """
    )


# PREVIOUS PROJECTS SECTION

elif section == "Previous Projects":
    st.header("📂 Previous Research Projects")

    st.markdown("###  Honours Project")
    st.success(
        "Investigating the Functional Interplay Between Different Cochaperones Cdc37 & HOP in Mammalian Cancer Cells"
    )

    st.markdown("### 3rd Year Chemistry Internship Project")
    st.info(
        "Identifying Anti-SARS CoV-2 Agents Using a Computational Approach"
    )

    st.write(
        """
        These projects strengthened my foundation in:

        - Protein folding and co-chaperone networks  
        - Computational approaches in antiviral drug discovery  
        - Structural bioinformatics and molecular interaction studies  
        """
    )


# SKILLS SECTION

elif section == "Lab & Computational Skills":
    st.header("⚙️ Lab & Computational Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔬 Laboratory Skills")
        st.markdown(
            """
            - Cell culture techniques 
            - Protein purification  
            - Western blotting  
            - Confocal Microscopy 
            - Ligation Assays 
            - Data analytics 
            """
        )

    with col2:
        st.subheader("💻 Computational Skills")
        st.markdown(
            """
            - Molecular docking  
            - Virtual screening  
            - Homology modelling  
            - Protein structure analysis  
            - Bioinformatics pipelines  
            - Python for scientific computing  
            """
        )


# SUPERVISOR & INSTITUTION SECTION

elif section == "Supervisor & Institution":
    st.header("🎓 Supervisor & Institution")

    st.markdown(
        """
        **Supervisor:** Prof Ozlem Tastan-Bishop  
        **Institution:** Rhodes University  
        **Research Area:** Computational Biology, Drug Discovery & Proteomics  
        """
    )

# CV & ORCID SECTION

elif section == "CV & ORCID":
    st.header("📄 CV & ORCID Profile")

    st.subheader("Download My CV")

    # Upload your CV into the same folder as app.py
    cv_file = "CV.pdf"

    try:
        with open(cv_file, "rb") as file:
            st.download_button(
                label="⬇️ Download CV",
                data=file,
                file_name="Abenathi_Nqweniso_CV.pdf",
                mime="application/pdf"
            )
    except:
        st.warning("Please upload a file named **CV.pdf** into your project folder.")

    st.subheader("🔗 ORCID Link")

    st.markdown(
        """

        **ORCID:** [0009-0005-8781-588X](https://orcid.org/0009-0005-8781-588X)
        """
    )


# FOOTER

st.markdown("---")
st.caption("© 2026 | Abenathi Nqweniso — Research Portfolio App built with Streamlit")
