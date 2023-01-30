from manim import *
from math import *


class Test(Scene):
    def construct(self):
        right_tri1 = Polygon([-1,0,0],[1,0,0],[1,1,0],fill_opacity=0.5,color=YELLOW)


        startText1 = Tex("a").next_to(right_tri1,DOWN)
        startText2 = Tex("b").next_to(right_tri1,RIGHT)
        startText3 = Tex("c").next_to(right_tri1,UP,buff=-0.3).shift(0.1*LEFT)

        self.play(DrawBorderThenFill(right_tri1))
        self.play(Write(startText1), run_time=1)
        self.play(Write(startText2), run_time=1)
        self.play(Write(startText3), run_time=1)
        self.wait()

        self.play(FadeOut(startText1,startText2,startText3))

        self.play(right_tri1.animate.rotate(DEGREES*90))
        self.play(right_tri1.animate.scale(1.5).move_to([1.5,0,0]))

        right_tri2 = right_tri1.copy()
        right_tri3 = right_tri1.copy()
        right_tri4 = right_tri1.copy()


        right_tri2.generate_target()
        right_tri2.target.rotate(DEGREES*(-90),about_point=right_tri1.get_corner(UR)).shift(DOWN*4.5)

        right_tri3.generate_target()
        right_tri3.target.rotate(DEGREES*(-180),about_point=right_tri1.get_corner(UR)).shift(DOWN*4.5).shift(LEFT*4.5)

        right_tri4.generate_target()
        right_tri4.target.rotate(DEGREES*(-270),about_point=right_tri1.get_corner(UR)).shift(LEFT*4.5)

        self.wait(0.5)

        self.play(
            MoveToTarget(right_tri2),
            MoveToTarget(right_tri3),
            MoveToTarget(right_tri4)
            )

        self.wait(1)

        BoxSquare = Square(4.5,stroke_width=8,z_index=100).move_to([0,-0.75,0])

        self.play(Create(BoxSquare),runtime=1)

        self.wait(1.5)
        
        texta = MathTex("a").set_color(BLUE)
        textb = MathTex("b").set_color(GREEN)
        textc = MathTex("c").set_color(RED)

        texta1 = texta.copy().next_to(right_tri2,DOWN)
        texta2 = texta.copy().next_to(right_tri1,RIGHT)
        texta3 = texta.copy().next_to(right_tri3,LEFT)
        texta4 = texta.copy().next_to(right_tri4,UP)

        textb1 = textb.copy().next_to(right_tri1,UP)
        textb2 = textb.copy().next_to(right_tri2,RIGHT)
        textb3 = textb.copy().next_to(right_tri3,DOWN)
        textb4 = textb.copy().next_to(right_tri4,LEFT)

        textc1 = textc.copy().next_to(right_tri1,LEFT,buff=-0.45).shift(0.1*DOWN)
        textc2 = textc.copy().next_to(right_tri2,UP,buff=-0.45).shift(0.1*LEFT)
        textc3 = textc.copy().next_to(right_tri3,RIGHT,buff=-0.45).shift(0.1*UP)
        textc4 = textc.copy().next_to(right_tri4,DOWN,buff=-0.45).shift(0.1*RIGHT)

        self.play(
            Write(texta1),
            Write(texta2),
            Write(texta3),
            Write(texta4),
            run_time=1.2
        )

        self.wait(0.5)

        self.play(
            Write(textb1),
            Write(textb2),
            Write(textb3),
            Write(textb4),
            run_time=1.2
        )

        self.play(
            Write(textc1),
            Write(textc2),
            Write(textc3),
            Write(textc4),
            run_time=0.8
        )

        explanationArealEquation = Tex("Arealet af hele firkanten =").scale(0.7).shift(UP*3.5+LEFT*4.5)

        Del1ArealEquation = MathTex(
            r"\left(",r"a",r"+",r"b",r"\right)\cdot"
            ).next_to(explanationArealEquation,RIGHT,buff=0.05).scale(0.7)
        
        Del2ArealEquation = MathTex(
            r"\left(",r"a",r"+",r"b",r"\right)"
            ).next_to(Del1ArealEquation,RIGHT,buff=-0.05).scale(0.7)

        Del1ArealEquation[1].set_color(BLUE)
        Del1ArealEquation[3].set_color(GREEN)

        Del2ArealEquation[1].set_color(BLUE)
        Del2ArealEquation[3].set_color(GREEN)

        #Laver Tekst På Siden
        MovingTexta1 = texta.copy().next_to(right_tri3,LEFT).scale(0.7)
        MovingTextb1 = textb.copy().next_to(right_tri4,LEFT).scale(0.7)

        #Laver Tekst På Toppen
        MovingTexta2 = texta.copy().next_to(right_tri4,UP).scale(0.7)
        MovingTextb2 = textb.copy().next_to(right_tri1,UP).scale(0.7)

        #Generere target for tekst fra Siden
        MovingTexta1.generate_target()
        MovingTextb1.generate_target()

        #Generere target for tekst fra toppen
        MovingTexta2.generate_target()
        MovingTextb2.generate_target()


        MovingTexta1.target.move_to(Del1ArealEquation[1])
        MovingTextb1.target.move_to(Del1ArealEquation[3])

        MovingTexta2.target.move_to(Del2ArealEquation[1])
        MovingTextb2.target.move_to(Del2ArealEquation[3])

        self.wait(1)

        self.play(Write(explanationArealEquation),runtime=0.1)
        self.play(
            Write(Del1ArealEquation),
            MoveToTarget(MovingTexta1),
            MoveToTarget(MovingTextb1)
            )
        self.remove(MovingTexta1)
        self.remove(MovingTextb1)

        self.wait(0.5)

        self.play(
            Write(Del2ArealEquation),
            MoveToTarget(MovingTexta2),
            MoveToTarget(MovingTextb2),
            )
        self.remove(MovingTexta2)
        self.remove(MovingTextb2)

        self.wait(1)

        explanationArealTilOvers = Tex("Arealet der er til overs = ").scale(0.7).shift(UP*3+LEFT*4.6)

        self.play(Write(explanationArealTilOvers))

        TilOversEquation = MathTex(r"c",r"\cdot ",r"c",r"=").next_to(explanationArealTilOvers,RIGHT,buff=-0.05).scale(0.7).shift(DOWN*0.05)
        TilOversEquation[0].set_color(RED)
        TilOversEquation[2].set_color(RED)

        TilOversEquationCSquared = MathTex(
            r"c",r"^2"
            ).next_to(TilOversEquation,buff=0.1).scale(0.7).shift(UP*0.075)
        
        TilOversEquationCSquared[0].set_color(RED)


        MovingTextc1 = textc.copy().next_to(right_tri3,RIGHT,buff=-0.45).shift(0.1*UP).scale(0.7)
        MovingTextc2 = textc.copy().next_to(right_tri4,DOWN,buff=-0.45).shift(0.1*RIGHT).scale(0.7)

        MovingTextCC = TilOversEquationCSquared.copy().move_to([0,0,0])

        MovingTextc1.generate_target()
        MovingTextc2.generate_target()

        MovingTextCC.generate_target()

        MovingTextc1.target.move_to(TilOversEquation[0])
        MovingTextc2.target.move_to(TilOversEquation[2])
        MovingTextCC.target.move_to(TilOversEquationCSquared)

        self.wait(0.5)

        self.play(
            Write(TilOversEquation),
            MoveToTarget(MovingTextc1),
            MoveToTarget(MovingTextc2),
            )

        CSquare = Square(sqrt(9+2.25),color=RED,fill_opacity=0.2).next_to(right_tri2,UP,buff=0).shift(LEFT*0.17705).rotate(atan(1/2),about_point=right_tri2.get_corner(UR))

        self.wait(1.5)

        self.play(
            MoveToTarget(MovingTextCC),
            Write(TilOversEquationCSquared),
            Create(CSquare),
            runtime=2
        )

        self.remove(MovingTextc1)
        self.remove(MovingTextc2)
        self.remove(MovingTextCC)

        self.wait(3)

        PreChange = VGroup(
            right_tri1.copy(), right_tri2.copy(), right_tri3.copy(), right_tri4.copy(),
            texta1, texta2, texta3, texta4,
            textb1, textb2, textb3, textb4, 
            textc1, textc2, textc3, textc4, 
            CSquare, BoxSquare.copy()
            )
        
        PreChangeText = VGroup(
            explanationArealTilOvers.copy(),
            TilOversEquation,
            TilOversEquationCSquared
        )
        
        self.play(
            PreChange.animate.scale(0.5).shift(LEFT*5.3),
            PreChangeText.animate.scale(0.6).shift(LEFT+DOWN*2),
            )


        self.wait(2)

        self.play(
            right_tri3.animate.shift(RIGHT*3+UP*1.5),
            right_tri2.animate.shift(LEFT*1.5),
            right_tri4.animate.shift(DOWN*3)
        )

        self.wait(2)

        POSTtexta1 = texta.copy().next_to(right_tri3,LEFT,buff=0.3)
        POSTtexta2 = texta.copy().next_to(right_tri4,UP,buff=0.3)

        POSTtextb1 = textb.copy().next_to(right_tri2,RIGHT,buff=0.15)
        POSTtextb2 = textb.copy().next_to(right_tri3,DOWN,buff=0.15)


        self.play(
            Write(POSTtexta1),
            Write(POSTtexta2),
            Write(POSTtextb1),
            Write(POSTtextb2),
            run_time=1.2
        )

        self.wait(1)

        ASquare = Square(3,color=BLUE,fill_opacity=0.2,z_index=0).next_to(right_tri3,LEFT,buff=0)
        BSquare = Square(1.5,color=GREEN,fill_opacity=0.2,z_index=0).next_to(right_tri3,DOWN,buff=0)

        self.play(
            Create(ASquare),
            Create(BSquare)
        )

        self.wait(2)

        POSTTilOversEquationDel1 = MathTex(r"a",r"\cdot ",r"a",r"+").next_to(explanationArealTilOvers,RIGHT,buff=-0.05).scale(0.7).shift(0)
        POSTTilOversEquationDel1[0].set_color(BLUE)
        POSTTilOversEquationDel1[2].set_color(BLUE)

        POSTTilOversEquationDel2 = MathTex(r"b",r"\cdot ",r"b",r"=").next_to(POSTTilOversEquationDel1,RIGHT,buff=-0.05).scale(0.7).shift(UP*0.01)
        POSTTilOversEquationDel2[0].set_color(GREEN)
        POSTTilOversEquationDel2[2].set_color(GREEN)

        TilOversEquationABSquared = MathTex(
            r"a",r"^2",r"+",r"b",r"^2"
            ).next_to(POSTTilOversEquationDel2,buff=-0.05).scale(0.7).shift(0.05)
        
        TilOversEquationABSquared[0].set_color(BLUE)
        TilOversEquationABSquared[3].set_color(GREEN)


        POSTMovingTexta1 = POSTtexta1.copy().scale(0.7)
        POSTMovingTexta2 = POSTtexta2.copy().scale(0.7)

        POSTMovingTextb1 = POSTtextb1.copy().scale(0.7)
        POSTMovingTextb2 = POSTtextb2.copy().scale(0.7)

        POSTMovingTexta1.generate_target()
        POSTMovingTexta2.generate_target()
        POSTMovingTextb1.generate_target()
        POSTMovingTextb2.generate_target()

        POSTMovingTexta1.target.move_to(POSTTilOversEquationDel1[0])
        POSTMovingTexta2.target.move_to(POSTTilOversEquationDel1[2])
        POSTMovingTextb1.target.move_to(POSTTilOversEquationDel2[0])
        POSTMovingTextb2.target.move_to(POSTTilOversEquationDel2[2])

        self.wait(0.5)

        self.play(
            Write(POSTTilOversEquationDel1),
            MoveToTarget(POSTMovingTexta1),
            MoveToTarget(POSTMovingTexta2)
            )

        self.remove(
            POSTMovingTexta1,
            POSTMovingTexta2
            )

        self.play(
            Write(POSTTilOversEquationDel2),
            MoveToTarget(POSTMovingTextb1),
            MoveToTarget(POSTMovingTextb2)
            )

        self.remove(
            POSTMovingTextb1,
            POSTMovingTextb2,
            )


        MovingPOSTTilOversEquationDel11 = POSTTilOversEquationDel1[0].copy()
        MovingPOSTTilOversEquationDel12 = POSTTilOversEquationDel1[2].copy()
        MovingPOSTTilOversEquationDel21 = POSTTilOversEquationDel2[0].copy()
        MovingPOSTTilOversEquationDel22 = POSTTilOversEquationDel2[2].copy()

        MovingPOSTTilOversEquationDel11.generate_target()
        MovingPOSTTilOversEquationDel12.generate_target()
        MovingPOSTTilOversEquationDel21.generate_target()
        MovingPOSTTilOversEquationDel22.generate_target()

        MovingPOSTTilOversEquationDel11.target.move_to(TilOversEquationABSquared[0])
        MovingPOSTTilOversEquationDel12.target.move_to(TilOversEquationABSquared[0])
        MovingPOSTTilOversEquationDel21.target.move_to(TilOversEquationABSquared[3])
        MovingPOSTTilOversEquationDel22.target.move_to(TilOversEquationABSquared[3])

        self.play(
            Write(TilOversEquationABSquared),
            MoveToTarget(MovingPOSTTilOversEquationDel11),
            MoveToTarget(MovingPOSTTilOversEquationDel12),
            MoveToTarget(MovingPOSTTilOversEquationDel21),
            MoveToTarget(MovingPOSTTilOversEquationDel22)
            )

        self.remove(
            MovingPOSTTilOversEquationDel11,
            MovingPOSTTilOversEquationDel12,
            MovingPOSTTilOversEquationDel21,
            MovingPOSTTilOversEquationDel22
        )


        PostChange = VGroup(
            BoxSquare,
            ASquare.copy(),
            BSquare.copy(),
            right_tri1, right_tri2, right_tri3, right_tri4,
            POSTtexta1, POSTtexta2, POSTtextb1, POSTtextb2

        )

        ABOX=VGroup(ASquare,POSTtexta1,POSTtexta2)
        BBOX=VGroup(BSquare,POSTtextb1,POSTtextb2)

        self.play(
            PostChange.animate.scale(0.5).shift(RIGHT*5.3),
            )
        
        self.play(
            ABOX.animate.shift(LEFT*1.5).scale(0.5),
            BBOX.animate.shift(UP*2.2+LEFT*1.7).scale(0.5)
        )

        PLUS = MathTex(r"+").next_to(ABOX,RIGHT,buff=0.3)

        EQUAL = MathTex(r"=").next_to(BBOX,RIGHT,buff=0.5)

        

        CEqual = VGroup(CSquare, textc3, textc4).copy()
        
        CEqual.generate_target() 
        
        CEqual.target.rotate(-atan(1/2)).next_to(EQUAL,RIGHT,buff=0.5)

        self.play(
            MoveToTarget(CEqual),
            Write(PLUS),
            Write(EQUAL)
        )




        self.wait()
