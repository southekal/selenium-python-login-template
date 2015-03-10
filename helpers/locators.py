__author__ = 'Southekal'


class LoginPageLocators(object):

    """
        Login Page CSS Selectors, IDs and Name Holders
    """

    BASE_URL = "https://www.ziprecruiter.com/"
    LOGIN_URL = BASE_URL + "login"
    SUCCESS_LOGIN_URL = BASE_URL + "candidate/suggested-jobs"
    JOB_SEEKER_ID = "candidates_btn"
    EMAIL_NAME = "email"
    PASSWORD_NAME = "password"
    SIGN_IN_NAME = "submitted"
    EMAIL_ERROR_CSS = "label.error"
    PASSWORD_ERROR_CSS = "div.alert"
    PASSWORD_MISSING_CSS = "label.error"


class SignUpPageLocators(object):
    """
        Signup Page CSS Selectors, IDs and Name Holders
    """

    BASE_URL = "https://www.ziprecruiter.com/"
    SIGNUP_URL = BASE_URL + "contact/create"
    NAME_ID = 'contactName'
    EMAIL_CLASS = "email_hint"
    CREATE_CLASS = "w100pPhone"
    ERROR_MSG_CLASS = "error_constraint_callback"