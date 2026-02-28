from turtle import Turtle

PADDLE_WIDTH: int = 20
PADDLE_HEIGHT: int = 100
MOVE_DISTANCE: int = 20
MOVE_LIMIT: int = 250


class Paddle(Turtle):
    """Represents a vertical paddle in the Pong game."""

    def __init__(self, position: tuple[float, float]) -> None:
        """
        Initialize the paddle at a given position.

        Args:
            position: The starting (x, y) coordinates of the paddle.
        """
        super().__init__()
        self._configure_appearance()
        self.goto(position)

    def _configure_appearance(self) -> None:
        """Configure the paddle's visual appearance and basic settings."""
        self.shape("square")
        self.color("white")
        self.shapesize(
            stretch_wid=PADDLE_HEIGHT / 20,
            stretch_len=PADDLE_WIDTH / 20,
        )
        self.penup()
        self.speed("fastest")

    def up(self) -> None:
        """Move the paddle upward within the vertical movement limit."""
        self._move(MOVE_DISTANCE)

    def down(self) -> None:
        """Move the paddle downward within the vertical movement limit."""
        self._move(-MOVE_DISTANCE)

    def _move(self, delta_y: int) -> None:
        """
        Move the paddle vertically if within bounds.

        Args:
            delta_y: The vertical distance to move (positive or negative).
        """
        new_y: float = self.ycor() + delta_y
        if -MOVE_LIMIT < new_y < MOVE_LIMIT:
            self.goto(self.xcor(), new_y)