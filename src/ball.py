from turtle import Turtle

MOVE_DISTANCE: float = 10.0
STARTING_POS_X: float = 0.0
STARTING_POS_Y: float = 0.0
INITIAL_MOVE_SPEED: float = 0.1


class Ball(Turtle):
    """Represents the ball in the Pong game."""

    def __init__(self) -> None:
        """Initialize the ball with default movement settings."""
        super().__init__()
        self._configure_appearance()
        self.move_distance_x: float = MOVE_DISTANCE
        self.move_distance_y: float = MOVE_DISTANCE
        self.move_speed: float = INITIAL_MOVE_SPEED

    def _configure_appearance(self) -> None:
        """Configure the ball's visual appearance."""
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self) -> None:
        """Move the ball according to its current velocity."""
        new_x: float = self.xcor() + self.move_distance_x
        new_y: float = self.ycor() + self.move_distance_y
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        """Reverse the vertical direction of the ball."""
        self.move_distance_y *= -1

    def bounce_x(self) -> None:
        """Reverse the horizontal direction and slightly increase speed."""
        self.move_distance_x *= -1
        self.move_speed *= 0.9

    def reset_position(self) -> None:
        """Reset the ball to the center and restore initial speed."""
        self.goto(STARTING_POS_X, STARTING_POS_Y)
        self.move_speed = INITIAL_MOVE_SPEED
        self.bounce_x()