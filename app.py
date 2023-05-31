import pynecone as pc


options = ["데이터 엔지니어", "백앤드", "MLops", "데이터 분석가"]


class SetterState1(pc.State):
    selected: str = "데이터 엔지니어"

    def change(self, value):
        self.selected = value


def index():
    return pc.vstack(
        pc.badge(
            SetterState1.selected, 
            color_scheme="green",
            font_size = '2em'
        ),
        pc.select(
            options,
            on_change=lambda value: SetterState1.change(
                value
            ),
        ),
    )


app = pc.App(state=SetterState1)
app.add_page(index)
app.compile()