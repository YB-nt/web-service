"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pynecone as pc
from sqlalchemy import select

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

options = ["데이터 엔지니어", "백앤드", "MLops", "데이터 분석가"]


class User(pc.Model,table=True):
    username:str
    password:str


def insert_query(_username,_password):
    with pc.session() as session:
        session.add(
            User(
                username=_username,
                password=_password,
            )
        )
    session.commit()

def select_query(_username):
    with pc.session() as session:
        stmt = session.query(User).filter_by(username=_username)
        if(len(stmt)==0):
            return False
        else:
            return True
    

class State(pc.State):
    option: str = "JOB INFO"

    id_value:str=''
    pwd_value:str=''

    id_check_opacity = "0%"
    id_check_pos = "translate(5px, 0px)"
    
    id_status=False
    pwd_status=False

    pass_check_opacity = "0%"
    pass_check_pos = "translate(5px, 0px)"

    id: str = "What's your email?"
    password: str = "Create a password."

    box_width: str = "60px"
    box_height: str = "60px"

    id_width: str = "0px"
    id_underline: str = "0px solid white"

    password_width = "0px"
    password_underline: str = "0px solid white"

    resutl_stauts ="text"
    result_sign_in = ""
    result_pos = "transform(0px, 0px)"
    result_opacity = "0%"
    result_color = ""

    def change(self, value):
        self.option = value

    def on_check_username(self, id):
        self.id = id
        self.id_underline = "2px solid green"
        self.box_height = "110px"
        self.id_status = True

    def on_check_password(self, pwd):
        self.pwd = pwd
        if len(self.pass_value) >= 6:
            self.pwd_status = True
        else:
            pass

    def clear_event():
        #input clear()
        pass
    def user_sign_in(self,username):
        try:
            if not select_query(username):
                return "Sign Up Successfull!"
            else:
                return "Sign Up Faild"
            
        except Exception as e:
            return "Sign Up Faild"
    def user_sign_up(self,username):
        try:
            if not select_query(username):
                return "Sign Up Successfull!",True
            else:
                return "Sign Up Faild",False
            
        except Exception as e:
            return "Sign Up Faild",False
        
def get_input_field(icon:str,placeholder:str,_type:str):
    return pc.container(
        pc.hstack(
            pc.icon(
                tag=icon,
                color="white",
                fontSize='11px',
            ),
            pc.input(
                placeholder=placeholder,
                border="0px",
                focus_border_color="None",
                color="white",
                fontWeight="semibold",
                fontSize='11px',
                type_=_type
            ),
        ),
        #container Settings 
        borderBottom ="0.1px solid grey",
        width="300px",
        height="45px",

    )
def input_box():
    return pc.container(
        pc.vstack(
            pc.container(
                pc.input(
                    placeholder='Enter your id',
                    border="0px",
                    focus_border_color="None",
                    color="white",
                    fontWeight="semibold",
                    fontSize='11px',
                ),
                padding="0px",
                width="300px",
                borderBottom ="0.1px solid grey",
                transition="width 0.65s ease",
            ),
            pc.checkbox(
                    color_scheme="green",
                    opacity=State.pass_check_opacity, 
                    is_checked=State.id_status,
                    transform=State.id_status,
                    transition="opacity 0.8s, transform 0.65s ease",
            ),
        ),
        pc.container(height="5px"),
        pc.vstack(
            pc.container(
                pc.input(
                    placeholder='Enter your password',
                    border="0px",
                    focus_border_color="None",
                    color="white",
                    fontWeight="semibold",
                    fontSize='11px',
                    type_ ="password",
                ),
                padding="0px",
                width="300px",
                borderBottom ="0.1px solid grey",
                transition="width 0.65s ease",
            ),
            pc.checkbox(
                    color_scheme="green",
                    opacity="0%",
                    is_checked=State.pwd_status,
                    transform=State.pwd_status,
                    transition="opacity 0.8s, transform 0.65s ease",
            ),
        ),
    )

def input_field(input_width, text_value, holder, func_change, _type):
    return pc.input(
        width=input_width,
        value=text_value,
        transition="width 0.5s ease 0.65",
        placeholder=holder,
        color="white",
        border="None",
        fontSize="13px",
        letter_spacing="0.5px",
        focus_border_color="None",
        type_=_type,
        on_change=func_change,
    )

def sign_up_event(_username,_password):
    message,state = State.user_sign_up(_username)
    if(state):
        pc.alert(
            pc.alert_icon(),
            pc.alert_title(message),
            status="success",
        ),
        insert_query(_username,_password)
    else:
        pc.alert(
            pc.alert_icon(),
            pc.alert_title(message),
            status="error",
        ),
        State.clear_event()


def index()-> pc.Component:
    login_container = pc.container(
        pc.vstack(
            pc.container(height="65px"),
            pc.container(
                pc.text(
                    "Sign In",
                    fontSize='28px',
                    color="white",
                    fontWeight="bold",
                    letterSpacing='2px',
                ),
                width='250px',
                center_content=True,
            ),
            pc.container(
                pc.text(
                    "Search For Skill Information By Job",
                    fontSize='12px',
                    color="white",
                    fontWeight="#eeeeee",
                    letterSpacing='0.2px',
                ),
                width='250px',
                center_content=True,
            ),
            pc.container(height="50px"),
            get_input_field("at_sign","Username",""),
            pc.container(height="5px"),
            get_input_field("lock","Password","password"),
            pc.container(height="5px"),
            pc.container(
                pc.text(
                    pc.link("Sign Up",
                        href="/signup",
                        ),
                    color='white',
                    fontSize='11px',
                    textAlign='end',
                ),
                width="300px",
                height='45px',
            ),
            pc.container(height="45px"),
            pc.container(
                pc.button(
                    pc.text(
                        "Sign In",
                        color='white',
                        fontSize='13px',
                        weight='bold',
                    ),
                    width="300px",
                    height='45px',
                )
            ),
        ),
        # container settings
        width="400px",
        height="75vh",
        bg="#1D2330",
        center_content=True,
        boxShadow="41px -41px 82px #0d0f15,-41px 41px 82px #2d374b",
        borderRadius="15px", 
    )
    _main = pc.container(
        login_container,
        center_content=True,
        justifyContent='center',
        maxWidth='auto',
        height="100vh",
        bg="#1D2330",
        
    )
    return _main

@pc.route(route="/signup", title="Sign Up")
def signup():
    login_container = pc.container(
        pc.vstack(
            pc.container(height="65px"),
            pc.container(
                pc.text(
                    "Sign Up",
                    fontSize='28px',
                    color="white",
                    fontWeight="bold",
                    letterSpacing='2px',
                ),
                width='250px',
                center_content=True,
            ),
            pc.container(height="50px"),
            input_box(),
            pc.container(
                pc.text(
                    pc.link("Sign In",
                        href="/",
                    ),
                    color='white',
                    fontSize='11px',
                    textAlign='end',
                ),
            ),
            pc.container(
                pc.text(
                    State.result_sign_in,
                    transform=State.result_pos,
                    opacity=State.result_opacity,
                    color=State.result_color,
                    font_size="20px",
                    font_weight="extrabold",
                    transition="opacity 0.55s, transform 0.55s ease",
                ),
                min_width="auto",
                height="60px",
                display="grid",
                place_items="center",
            ),
            pc.container(height="45px"),
            pc.container(
                pc.button(
                    pc.text(
                        "Sign up",
                        color='white',
                        fontSize='13px',
                        weight='bold',
                        # on_click=lambda:,
                    ),
                    width="300px",
                    height='45px',
                    sechema_color ='grey600',
                ),
            ),
        ),
        # container settings
            width="400px",
            height="75vh",
            bg="#1D2330",
            center_content=True,
            boxShadow="41px -41px 82px #0d0f15,-41px 41px 82px #2d374b",
            borderRadius="15px",
        )
        
    _signup = pc.container(
        login_container,
        center_content=True,
        justifyContent='center',
        maxWidth='auto',
        height="100vh",
        bg="#1D2330",   
    )
    return _signup

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index,title="Login Page")
app.add_page(signup)
app.compile()
