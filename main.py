from game.services.keyboardService import KeyboardService
from game.services.VideoService import VideoService
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.shared.color import Color
from game.shared.point import Point
from game.directing.director import Director
from game.casting.cast import Cast

def main():

    # create the cast
    cast = Cast()

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