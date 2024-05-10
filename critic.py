from manim import *

class HermeneuticTaxono(Scene):
    def construct(self):

        heading = Text("Hermeneutic Revision\nof Bloom's Taxonomy").scale(0.7).to_edge(LEFT, buff=2).set_color(YELLOW)

        self.play(Write(heading))

        self.wait()

        words = []
        with open("herm.txt", "r") as f:
            words = f.readlines()

        text = VGroup(
            *[Text(word).scale(0.4) for word in words]
            ).arrange(DOWN, buff=0.5).set_color_by_gradient(BLUE, LIGHT_BROWN)
        
        text.shift(RIGHT * 2)
        
        boxes = VGroup()
        for word in text:
            boxes.add(SurroundingRectangle(word))
        boxes.set_color_by_gradient(BLUE, LIGHT_BROWN)
        self.play(Write(text), Write(boxes))

        arrow = Arrow(boxes.get_top(), 
                      boxes.get_bottom(),
                      max_tip_length_to_length_ratio=0.2,
                      max_stroke_width_to_length_ratio=1
                    ).shift(RIGHT * 2)
        self.play(DrawBorderThenFill(arrow))

        self.wait(2)


class engDef(Scene):
    def construct(self):
        heading = Text("engineering").set_color(YELLOW)
        self.play(Write(heading))

        type = Text("noun", slant=ITALIC, should_center=False).scale(0.3).next_to(heading.get_left(), DOWN*1.3 + RIGHT*0.1)
        self.play(Write(type))

        word = VGroup(heading, type)

        self.wait()

        self.play(
            word.animate.shift(UP*2)
        )

        definition = Text(
            "the work of an engineer (= a person who designs or builds \nmachines, engines, electrical systems, or large structures\nsuch as roads or bridges using scientific principles), \nor the study of this work.",
            should_center=True,
            color=BLUE,
            slant=ITALIC
        ).scale(0.4)

        self.play(FadeIn(definition))

        self.wait(2)

        self.play(FadeOut(*self.mobjects))


class taxoReq(Scene):
    def construct(self):
        fexible = Text("Flexible")
        open_ = Text("Open")
        caters = Text("Caters to YOU")

        text = VGroup(fexible, open_, caters).scale(0.7).set_color_by_gradient(PINK, YELLOW).arrange(DOWN, buff=0.7)

        self.play(
            Write(text)
        )

        self.wait(2)

        self.play(FadeOut(text))
