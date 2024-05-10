from manim import *

class Interpretation(Scene):
    def construct(self):
        heading = Text("Interpretation").set_color(YELLOW)
        self.play(Write(heading))
        self.wait()
        self.play(
            heading.animate.shift(UP*2)
        )

        point1 = Text("Builds passion")
        point2 = Text("Observations <==> Questions")
        point3 = Text("Questions <==> Observations")
        
        points = VGroup(point1, point2, point3)


        # points aesthetics
        points.scale(0.5).set_color_by_gradient(BLUE, GOLD)

        # points position 
        points.arrange(DOWN, buff=0.3) #, center=False, aligned_edge=LEFT)

        for point in points:
            self.play(FadeIn(point))
            self.wait()
        
        self.wait()
        self.play(FadeOut(*self.mobjects))

class Conceptualisation(Scene):
    def construct(self):
        heading = Text("Conceptualisation").set_color(YELLOW)
        self.play(Write(heading))
        self.wait()
        self.play(
            heading.animate.shift(UP*2)
        )

        hunger = Text("Hunger").scale(0.7).set_color(GREEN_C)
        self.play(Create(hunger))
        self.play(Circumscribe(hunger))
        self.wait()
        self.play(FadeOut(hunger))

        point1 = Text("Think Scientifically")
        point2 = Text("Research")
        point3 = Text("New Ideas")
        point4 = Text("Abstraction of Problem")
        
        points = VGroup(point1, point2, point3, point4)


        # points aesthetics
        points.scale(0.5).set_color_by_gradient(BLUE, GOLD)

        # points position 
        points.arrange(DOWN, buff=0.3) #, center=False, aligned_edge=LEFT)

        for point in points:
            self.play(FadeIn(point))
            self.wait()
        
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

class Optimization(Scene):
    def construct(self):
        heading = Text("Optimization").set_color(YELLOW)
        self.play(Write(heading))
        self.wait()
        self.play(
            heading.animate.shift(UP*2)
        )

        dots = VGroup()
        for i in range(0,5):
            dot = Circle(0.3, color=random_color(), fill_opacity=0.3)
            dots.add(dot)

        dots.arrange(RIGHT, buff=0.5)

        self.play(
            DrawBorderThenFill(dots)
        )

        self.wait()

        main_dot = Circle(0.3, color=PURPLE, fill_opacity=0.4)

        self.play(
            ReplacementTransform(dots, main_dot)
        )

        self.wait(1)

        self.play(
            FadeOut(main_dot)
        )

        point1 = Text("Narrow Down Options")
        point2 = Text("Maximize Utility")
        point3 = Text("Saves Time in Long Run")
        
        points = VGroup(point1, point2, point3)


        # points aesthetics
        points.scale(0.5).set_color_by_gradient(BLUE, GOLD)

        # points position 
        points.arrange(DOWN, buff=0.3) #, center=False, aligned_edge=LEFT)

        for point in points:
            self.play(FadeIn(point))
            self.wait()
        
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

class Prototyping(Scene):
    def construct(self):
        heading = Text("Prototyping").set_color(YELLOW)
        self.play(Write(heading))
        self.wait()
        self.play(
            heading.animate.shift(UP*2)
        )

        point1 = Text("Verify the Solutions")
        point2 = Text("Simple Models")
        point3 = Text("Hypothesis Testing")
        point4 = Text("Controlled Environment")
        
        points = VGroup(point1, point2, point3, point4)


        # points aesthetics
        points.scale(0.5).set_color_by_gradient(BLUE, GOLD)

        # points position 
        points.arrange(DOWN, buff=0.3) #, center=False, aligned_edge=LEFT)
        points.shift(LEFT * 3)

        for point in points:
            self.play(FadeIn(point))
            self.wait()
        
        self.wait()
        self.play(FadeOut(*self.mobjects))

class Testing(Scene):
    def construct(self):
        heading = Text("Testing").set_color(YELLOW)
        self.play(Write(heading))
        self.wait()
        self.play(
            heading.animate.shift(UP*2)
        )

        point1 = Text("Prototype - Closer to Final Product")
        point2 = Text("Test Unaccounted Variables")
        point3 = Text("User Experience")
        
        points = VGroup(point1, point2, point3)


        # points aesthetics
        points.scale(0.5).set_color_by_gradient(BLUE, GOLD)

        # points position 
        points.arrange(DOWN, buff=0.3) #, center=False, aligned_edge=LEFT)

        for point in points:
            self.play(FadeIn(point))
            self.wait()
        
        self.wait()
        self.play(FadeOut(*self.mobjects))

class Innovation(Scene):
    def construct(self):
        innovation = Text("Innovation").set_color(YELLOW)
        self.play(Write(innovation))

        self.wait()

        self.play(innovation.animate.shift(UP * 2))

        solution = Text("Solution", color=LIGHT_BROWN).scale(0.8).shift(DOWN * 1)
        arrow = Arrow(solution.get_top(), innovation.get_bottom(),
                      max_tip_length_to_length_ratio=0.15,
                      max_stroke_width_to_length_ratio=1)
        
        solution_caption = Text("More Efficient\nFulfills Needs", font='Monaco', slant=ITALIC).next_to(solution, DOWN * 0.5).set_color(BLUE).scale(0.4)

        self.play(
            Create(solution),
            DrawBorderThenFill(arrow),
            FadeIn(solution_caption)
        )

        self.wait(2)

        self.play(
            FadeOut(VGroup(solution, arrow, solution_caption))
        )
        self.play(
            innovation.animate.shift(DOWN * 2 + LEFT * 3.5)
        )

        inter = Text("Interpretation")
        concept = Text("Conceptualisation")
        opti = Text("Optimization")
        proto = Text("Prototyping")
        test = Text("Testing")
        levels = VGroup(inter, concept, opti, proto, test).scale(0.6)
        levels.set_color_by_gradient(BLUE, LIGHT_BROWN)

        pos = [
            [2.3, 2, 0], # inter
            [5.3, 0, 0], # concept
            [4.5, -2, 0], # opti
            [1, -2, 0], # proto
            [0, 0, 0] # test
        ]

        for i in range(len(pos)):
            levels[i].move_to(pos[i])

        a1 = Arrow(inter.get_right(), concept.get_top(), max_tip_length_to_length_ratio=0.1, stroke_width=3)
        a2 = Arrow(concept.get_bottom(), opti.get_top(), max_tip_length_to_length_ratio=0.1, stroke_width=3)
        a3 = Arrow(opti.get_left(), proto.get_right(), max_tip_length_to_length_ratio=0.1, stroke_width=3)
        a4 = Arrow(proto.get_top(), test.get_bottom(), max_tip_length_to_length_ratio=0.1, stroke_width=3)
        a7 = Arrow(test.get_left(), innovation.get_right(), max_tip_length_to_length_ratio=0.2, stroke_width=3)
        a5 = Arrow(test.get_top(), inter.get_left(), max_tip_length_to_length_ratio=0.1, stroke_width=3)
        a6 = Arrow(proto.get_top(), inter.get_bottom(), max_tip_length_to_length_ratio=0.05, stroke_width=3)

        arrs = VGroup(a1,a2,a3,a4,a5,a6,a7).set_color_by_gradient(BLUE, LIGHT_BROWN)


        self.play(
            FadeIn(levels)
        )
        for i in range(len(arrs)):
            self.play(Create(arrs[i]), run_time=.6)

        self.wait(2)

        self.play(FadeOut(*self.mobjects))