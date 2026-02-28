from turtle import Turtle

ALIGNMENT: str = "center"
FONT: tuple[str, int, str] = ("Arial", 24, "normal")
SCORE_POSITION: tuple[int, int] = (0, 260)


class Scoreboard(Turtle):
    """Represents the scoreboard in the Pong game."""

    def __init__(self) -> None:
        """Initialize the scoreboard with default scores."""
        super().__init__()
        self.left_score: int = 0
        self.right_score: int = 0

        self._configure()
        self._render()

    def _configure(self) -> None:
        """Configure visual appearance and initial position."""
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(SCORE_POSITION)

    def _render(self) -> None:
        """Render the current score on the screen."""
        self.clear()
        self.write(
            f"{self.left_score} : {self.right_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_left_score(self) -> None:
        """Increase the left player's score by one and update display."""
        self.left_score += 1
        self._render()

    def increase_right_score(self) -> None:
        """Increase the right player's score by one and update display."""
        self.right_score += 1
        self._render()

    def game_over(self) -> None:
        """Display a centered 'GAME OVER' message."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)