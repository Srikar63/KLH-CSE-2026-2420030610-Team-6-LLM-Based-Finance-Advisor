import streamlit as st
import pandas as pd
import hashlib
import os
import re

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FinancePro - Create Account",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# USER DATABASE
# =========================================================

USERS_FILE = "data/users.csv"


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def load_users():

    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)

    return pd.DataFrame(
        columns=[
            "full_name",
            "username",
            "email",
            "password"
        ]
    )


def save_user(full_name, username, email, password):

    users = load_users()

    new_user = pd.DataFrame([{
        "full_name": full_name,
        "username": username,
        "email": email,
        "password": hash_password(password)
    }])

    users = pd.concat(
        [users, new_user],
        ignore_index=True
    )

    users.to_csv(
        USERS_FILE,
        index=False
    )


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* Remove Streamlit UI */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 20% 25%,
            rgba(93, 63, 211, 0.35),
            transparent 35%
        ),

        radial-gradient(
            circle at 80% 20%,
            rgba(190, 60, 150, 0.28),
            transparent 35%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(40, 80, 200, 0.30),
            transparent 40%
        ),

        linear-gradient(
            135deg,
            #15152b 0%,
            #252044 45%,
            #101827 100%
        );
}


/* =====================================================
   FINANCEPRO
   ===================================================== */

.brand {

    position: fixed;

    top: 25px;
    left: 35px;

    color: white;

    font-size: 27px;

    font-weight: 700;

    letter-spacing: 0.3px;

    z-index: 9999;
}


/* =====================================================
   CONTENT WIDTH
   ===================================================== */

.block-container {

    max-width: 460px !important;

    margin: auto !important;

    padding-top: 85px !important;

    padding-bottom: 40px !important;
}


/* =====================================================
   TITLE
   ===================================================== */

.title {

    text-align: center;

    color: white;

    font-size: 30px;

    font-weight: 300;

    letter-spacing: 3px;

    margin-bottom: 8px;
}


.subtitle {

    text-align: center;

    color: rgba(255,255,255,0.60);

    font-size: 13px;

    margin-bottom: 22px;
}


.title-line {

    width: 100%;

    height: 1px;

    background: rgba(255,255,255,0.22);

    margin-bottom: 22px;
}


/* =====================================================
   INPUT LABELS
   ===================================================== */

.stTextInput label {

    color: rgba(255,255,255,0.80) !important;

    font-size: 13px !important;

    font-weight: 500 !important;
}


/* =====================================================
   INPUT BOXES
   ===================================================== */

.stTextInput input {

    background: rgba(255,255,255,0.10) !important;

    color: white !important;

    border: 1px solid rgba(255,255,255,0.18) !important;

    border-radius: 7px !important;

    height: 43px !important;

    font-size: 13px !important;

    padding-left: 13px !important;
}


.stTextInput input::placeholder {

    color: rgba(255,255,255,0.40) !important;
}


.stTextInput input:focus {

    border: 1px solid rgba(255,255,255,0.45) !important;

    box-shadow:
        0 0 8px rgba(120,100,220,0.25) !important;
}


/* =====================================================
   CREATE ACCOUNT BUTTON
   ===================================================== */

.create-btn button {

    background: #f45151 !important;

    color: white !important;

    border: none !important;

    border-radius: 9px !important;

    height: 44px !important;

    font-size: 14px !important;

    font-weight: 600 !important;

    letter-spacing: 0.8px !important;

    box-shadow:
        0 5px 15px rgba(244,81,81,0.25) !important;
}


.create-btn button:hover {

    background: #ff5c5c !important;

    transform: translateY(-1px);
}


/* =====================================================
   LOGIN TEXT
   ===================================================== */

.login-text {

    text-align: center;

    color: rgba(255,255,255,0.60);

    font-size: 12px;

    margin-top: 18px;

    margin-bottom: 5px;
}


/* =====================================================
   LOGIN BUTTON
   ===================================================== */

.login-btn button {

    background: rgba(255,255,255,0.08) !important;

    color: #fca5a5 !important;

    border: 1px solid rgba(255,255,255,0.15) !important;

    border-radius: 8px !important;

    height: 42px !important;

    font-size: 13px !important;
}


.login-btn button:hover {

    background: rgba(255,255,255,0.13) !important;
}


/* =====================================================
   ALERTS
   ===================================================== */

.stAlert {

    border-radius: 8px !important;

    font-size: 13px !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FINANCEPRO TITLE
# =========================================================

st.markdown(
    '<div class="brand">FinancePro</div>',
    unsafe_allow_html=True
)


# =========================================================
# PAGE TITLE
# =========================================================

st.markdown(
    '<div class="title">CREATE ACCOUNT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create your FinancePro account'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title-line"></div>',
    unsafe_allow_html=True
)


# =========================================================
# FULL NAME
# =========================================================

full_name = st.text_input(
    "Full Name",
    placeholder="Enter your full name"
)


# =========================================================
# USERNAME
# =========================================================

username = st.text_input(
    "Username",
    placeholder="Choose a username"
)


# =========================================================
# EMAIL
# =========================================================

email = st.text_input(
    "Email",
    placeholder="Enter your email address"
)


# =========================================================
# PASSWORD
# =========================================================

password = st.text_input(
    "Password",
    type="password",
    placeholder="Create a password"
)


# =========================================================
# CONFIRM PASSWORD
# =========================================================

confirm_password = st.text_input(
    "Confirm Password",
    type="password",
    placeholder="Confirm your password"
)


st.write("")


# =========================================================
# CREATE ACCOUNT BUTTON
# =========================================================

st.markdown(
    '<div class="create-btn">',
    unsafe_allow_html=True
)

create = st.button(
    "CREATE ACCOUNT",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# CREATE ACCOUNT LOGIC
# =========================================================

if create:

    # Empty fields

    if (
        not full_name
        or not username
        or not email
        or not password
        or not confirm_password
    ):

        st.warning(
            "Please fill in all fields."
        )

    # Email validation

    elif not re.match(
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        email
    ):

        st.error(
            "Please enter a valid email address."
        )

    # Password length

    elif len(password) < 6:

        st.error(
            "Password must contain at least 6 characters."
        )

    # Password confirmation

    elif password != confirm_password:

        st.error(
            "Passwords do not match."
        )

    else:

        users = load_users()

        # Check username

        if username in users["username"].astype(str).values:

            st.error(
                "Username already exists."
            )

        # Check email

        elif email in users["email"].astype(str).values:

            st.error(
                "Email already registered."
            )

        else:

            save_user(
                full_name,
                username,
                email,
                password
            )

            st.success(
                "Account created successfully!"
            )

            st.info(
                "Your account has been saved. Please login."
            )


# =========================================================
# LOGIN OPTION
# =========================================================

st.markdown(
    '<div class="login-text">'
    "Already have an account?"
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="login-btn">',
    unsafe_allow_html=True
)

login = st.button(
    "LOGIN",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# GO TO LOGIN
# =========================================================

if login:

    st.switch_page("login.py")