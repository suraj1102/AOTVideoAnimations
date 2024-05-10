from manim import *

class FullTaxonomy(Scene):
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

        thinking = Text("Thinking")
        observation = Text("Observation")
        new_heading = VGroup(thinking, observation).scale(0.8).arrange(RIGHT, buff=2).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            FadeOut(arrow),
            Unwrite(heading, run_time=0.3),
            ReplacementTransform(VGroup(*text, *boxes), new_heading)
        )
        self.play(
            new_heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    The hermeneutic perspective views thinking as an individual, 
                    subjective exercise whereas observation is us as situated 
                    being-in-the-world. 
                       
                    Both thinking and observation are grounded in Heidegger's 
                    notion of <u>dasein</u> - the lived experience of human existence
                    as beings engaged with and immersed in the world around them."""
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )

class Reflection(Scene):
    def construct(self):
        heading = Text("Reflection").scale(0.8).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            Write(heading)
        )
        self.wait(2)
        self.play(
            heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    Reflection involves carefully examining our preconceptions
                    and what is before us through the lens of our situatedness
                    or 'dasein'. It allows us to identify meaning by adopting 
                    a deeper, more holistic perspective informed by our 
                    being-in-the-world.
                    """
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )

class Analysis(Scene):
    def construct(self):
        heading = Text("Analysis").scale(0.8).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            Write(heading)
        )
        self.wait(2)
        self.play(
            heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    Analysis deconstructs the object of study into its 
                    constituent parts. But unlike detached analytical 
                    methods, hermeneutical analysis compares and contrasts 
                    these parts through the situated observer's lifeworld 
                    involvements. Analysis thereby opens the way for richer 
                    judgments and decision-making.
                    """
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )
        
class Interpretation(Scene):
    def construct(self):
        heading = Text("Interpretation").scale(0.8).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            Write(heading)
        )
        self.wait(2)
        self.play(
            heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    Interpretation is the core hermeneutical act of translating
                    and explaining. It proceeds through multiple levels - from 
                    naive understanding, to explanation based on one's 
                    historically-effected consciousness, to an appropriated 
                    self-understanding where the interpreter's very being is remolded.
                    """
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )

class Critique(Scene):
    def construct(self):
        heading = Text("Critique").scale(0.8).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            Write(heading)
        )
        self.wait(2)
        self.play(
            heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    Critique evaluates interpretations objectively, testing 
                    internal coherence and external validity. It compares 
                    perspectives, providing reasoned arguments for a 
                    provisionally informed opinion.
                    """
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )

class Innovation(Scene):
    def construct(self):
        heading = Text("Innovation").scale(0.8).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            Write(heading)
        )
        self.wait(2)
        self.play(
            heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    Innovation involves rearranging and recombining elements
                    in new ways based on one's contextual understanding. It 
                    recognizes problems and produces novel solutions by 
                    creatively using existing knowledge.
                    """
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )

class Argumentation(Scene):
    def construct(self):
        heading = Text("Argumentation").scale(0.8).set_color_by_gradient(BLUE, LIGHT_BROWN)

        self.play(
            Write(heading)
        )
        self.wait(2)
        self.play(
            heading.animate.shift(UP*2)
        )

        self.wait(2)

        content = MarkupText("""
                    When innovative interpretations are presented as knowledge 
                    claims, argumentation comes into play. Hermeneutical 
                    argumentation grounds assertions in the researcher's 
                    perspective while remaining open to other viewpoints
                    """
                    ).scale(0.4).set_color(YELLOW)
        
        self.play(Create(content), run_time=5)

        self.wait(2)

        self.play(
            FadeOut(*self.mobjects)
        )


from random import seed, uniform

class ArrangeExample(Scene):
    def construct(self):
        seed(0xDEADBEEF)

        circle = Circle(3, BLUE, fill_opacity=0.2)

        self.play(
            DrawBorderThenFill(circle)
        )

        self.wait(2)

        circles = VGroup(
            *[
                Circle(radius=0.1, fill_opacity=0.3)
                .scale(uniform(0.5, 4))
                .shift(UP * uniform(-3, 3) + RIGHT * uniform(-5, 5))
                for _ in range(12)
            ]
        ).set_color_by_gradient(BLUE, RED)

        self.play(ReplacementTransform(circle, circles))

        self.wait(2)

        # left-to-right arrangement
        self.play(circles.animate.arrange())

        self.wait()

        # specify the direction of arrangement and spacing between the objects
        self.play(circles.animate.arrange_in_grid())
        self.wait(2)
        # self.play(Transform(circles, circle))