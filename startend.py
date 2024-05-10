from manim import *

class intro(Scene):
    def construct(self):
        intro = Text("FM109 - Art of Thinking and Reasoning:Video Submission").scale(0.4).shift(UP*2).set_color(WHITE)
        self.play(FadeIn(intro))

        cop = Text("Our Engineering").scale(0.9).shift(UP*0.5).set_color_by_gradient(BLUE_B, LIGHT_BROWN)
        mws = Text("Taxonomy").scale(0.9).next_to(cop, DOWN * 1.2).set_color_by_gradient(LIGHT_BROWN, BLUE_B)

        self.play(Write(VGroup(cop, mws)))

        names = VGroup(
            Text("Suraj Dayma - U20230102"),
            Text("Nikunj Agarwal - U20230068"),
            Text("Jatin Sharma - U20230118"),
            Text("Mohil Ahuja - U20230121"),
            Text("Vaibhav Dabas - U20230099"),
            Text("Manan Gadesha - U20230009"),
            Text("Prasham Sheth - U20230026")

        ).arrange(DOWN).shift(DOWN*2).scale(0.3).set_color(BLUE_C)

        self.play(FadeIn(names))

        self.wait(1)

        self.play(FadeOut(VGroup(*[name for name in names], cop, mws, intro)))

        self.wait(1)