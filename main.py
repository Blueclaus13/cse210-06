from constants import FONT_SIZE, GREEN, RED
from game.services.keyboardService import KeyboardService
from game.services.VideoService import VideoService
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.shared.color import Color
from game.shared.point import Point
from game.directing.director import Director
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.actor import Actor

def main():

    # create the cast
    cast = Cast()
    cast.add_actor("scores", Score())


    # create paddle1
    x1 = int()
    y1 = int()
    position1 = Point(x1, y1)

    paddle1 = Actor()
    paddle1.set_text('|')
    paddle1.set_font_size(FONT_SIZE)
    paddle1.set_color(RED)
    paddle1.set_position(position1)
    cast.add_actor("paddles1", paddle1)


    # create paddle2
    x2 = int()
    y2 = int()
    position2 = Point(x2, y2)

    paddle2 = Actor()
    paddle2.set_text('|')
    paddle2.set_font_size(FONT_SIZE)
    paddle2.set_color(GREEN)
    paddle2.set_position(position2)
    cast.add_actor("paddles2", paddle2)



     # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    #script.add_action("update", MoveActorsAction())
    #script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()