import streamlit as st
import pandas as pd
import hashlib
import os

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FinancePro - Login",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# USER DATABASE
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

USERS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.csv"
)


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


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

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
   FINANCEPRO TITLE
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
   MAIN CONTENT
   ===================================================== */

.block-container {

    max-width: 460px !important;

    margin: auto !important;

    padding-top: 120px !important;

    padding-bottom: 40px !important;
}


/* =====================================================
   WELCOME
   ===================================================== */

.welcome {

    text-align: center;

    color: white;

    font-size: 32px;

    font-weight: 300;

    letter-spacing: 4px;

    margin-bottom: 14px;
}


.welcome-line {

    width: 100%;

    height: 1px;

    background: rgba(255,255,255,0.25);

    margin-bottom: 28px;
}


/* =====================================================
   INPUT LABEL
   ===================================================== */

.stTextInput label {

    color: rgba(255,255,255,0.80) !important;

    font-size: 13px !important;

    font-weight: 500 !important;
}


/* =====================================================
   INPUT
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
   REMEMBER ME
   ===================================================== */

.stCheckbox label {

    color: rgba(255,255,255,0.70) !important;

    font-size: 12px !important;
}


/* =====================================================
   FORGOT PASSWORD
   ===================================================== */

.forgot {

    text-align: right;

    color: rgba(255,255,255,0.65);

    font-size: 12px;

    padding-top: 8px;
}


/* =====================================================
   LOGIN BUTTON
   ===================================================== */

.login-btn button {

    background: #f45151 !important;

    color: white !important;

    border: none !important;

    border-radius: 9px !important;

    height: 44px !important;

    font-size: 14px !important;

    font-weight: 600 !important;

    letter-spacing: 1px !important;

    box-shadow:
        0 5px 15px rgba(244,81,81,0.25) !important;
}


.login-btn button:hover {

    background: #ff5c5c !important;

    transform: translateY(-1px);
}


/* =====================================================
   DIVIDER
   ===================================================== */

.divider {

    display: flex;

    align-items: center;

    margin: 22px 0;

    color: rgba(255,255,255,0.40);

    font-size: 11px;
}


.divider::before,
.divider::after {

    content: "";

    flex: 1;

    height: 1px;

    background: rgba(255,255,255,0.18);
}


.divider span {

    padding: 0 12px;
}


/* =====================================================
   GMAIL BUTTON
   ===================================================== */

.gmail-btn button {

    background: rgba(255,255,255,0.08) !important;

    color: white !important;

    border: 1px solid rgba(255,255,255,0.18) !important;

    border-radius: 8px !important;

    height: 43px !important;

    font-size: 13px !important;
}


.gmail-btn button:hover {

    background: rgba(255,255,255,0.14) !important;
}


/* =====================================================
   CREATE ACCOUNT
   ===================================================== */

.create-text {

    text-align: center;

    color: rgba(255,255,255,0.60);

    font-size: 12px;

    margin-top: 20px;

    margin-bottom: 5px;
}


.create-btn button {

    background: rgba(255,255,255,0.08) !important;

    color: #fca5a5 !important;

    border: 1px solid rgba(255,255,255,0.15) !important;

    border-radius: 8px !important;

    height: 42px !important;

    font-size: 13px !important;
}


.create-btn button:hover {

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
# FINANCEPRO
# =========================================================

st.markdown(
    '<div class="brand">FinancePro</div>',
    unsafe_allow_html=True
)


# =========================================================
# WELCOME
# =========================================================

st.markdown(
    '<div class="welcome">WELCOME</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="welcome-line"></div>',
    unsafe_allow_html=True
)


# =========================================================
# USERNAME / EMAIL
# =========================================================

username = st.text_input(
    "Username",
    placeholder="Username"
)


# =========================================================
# PASSWORD
# =========================================================

password = st.text_input(
    "Password",
    placeholder="Password",
    type="password"
)


# =========================================================
# REMEMBER / FORGOT
# =========================================================

col1, col2 = st.columns([1, 1])

with col1:

    remember = st.checkbox(
        "Remember me"
    )

with col2:

    st.markdown(
        '<div class="forgot">Forgot Password?</div>',
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# LOGIN BUTTON
# =========================================================

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
# LOGIN VALIDATION
# =========================================================

if login:

    if username == "" or password == "":

        st.warning(
            "Please enter username and password."
        )

    else:

        users = load_users()

        hashed_password = hash_password(password)

        matched_user = pd.DataFrame()

        if not users.empty:

            matched_user = users[
                (
                    (
                        users["username"]
                        .astype(str)
                        == username
                    )
                    |
                    (
                        users["email"]
                        .astype(str)
                        == username
                    )
                )
                &
                (
                    users["password"]
                    .astype(str)
                    == hashed_password
                )
            ]


        # =================================================
        # REGISTERED USER
        # =================================================

        if not matched_user.empty:

            st.session_state["logged_in"] = True

            st.session_state["username"] = username

            st.session_state["full_name"] = (
                matched_user.iloc[0]["full_name"]
            )

            st.success(
                "Login successful!"
            )

            st.switch_page("pages/app.py")


        # =================================================
        # DEMO ADMIN
        # =================================================

        elif (
            username == "admin"
            and password == "admin123"
        ):

            st.session_state["logged_in"] = True

            st.session_state["username"] = "admin"

            st.session_state["full_name"] = "Administrator"

            st.success(
                "Login successful!"
            )

            st.switch_page("pages/app.py")


        # =================================================
        # INVALID LOGIN
        # =================================================

        else:

            st.error(
                "Invalid username/email or password."
            )


# =========================================================
# OR
# =========================================================

st.markdown(
    '<div class="divider"><span>OR</span></div>',
    unsafe_allow_html=True
)


# =========================================================
# GMAIL LOGIN
# =========================================================

st.markdown(
    '<div class="gmail-btn">',
    unsafe_allow_html=True
)

gmail = st.button(
    "Login with Email",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


if gmail:

    st.info(
        "Google login will be connected using Google OAuth."
    )


# =========================================================
# CREATE ACCOUNT
# =========================================================

st.markdown(
    '<div class="create-text">'
    "Don't have an account?"
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="create-btn">',
    unsafe_allow_html=True
)

create_account = st.button(
    "Create Account",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# OPEN REGISTER PAGE
# =========================================================

if create_account:

    st.switch_page("pages/register.py")