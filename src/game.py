from turtle import Screen
import time
from .scoreboard import Scoreboard
from .paddle import Paddle
from .ball import Ball

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

LEFT_PADDLE_START_POS: tuple[float, float] = (-350.0, 0.0)
RIGHT_PADDLE_START_POS: tuple[float, float] = (350.0, 0.0)

COLLISION_DISTANCE_PADDLE: float = 50.0
WALL_LIMIT: float = 280.0
PADDLE_COLLISION_X: float = 320.0
PADDLE_MISS_X: float = 380.0

MAX_SCORE: int = 5
AI_SPEED: int = 15  # Maximum movement per tick for AI


class Game:
    """Main controller class responsible for running the Pong game with AI."""

    def __init__(self) -> None:
        """Initialize game objects, screen, and controls."""
        self.screen: Screen = self._setup_screen()

        self.left_paddle: Paddle = Paddle(LEFT_PADDLE_START_POS)
        self.right_paddle: Paddle = Paddle(RIGHT_PADDLE_START_POS)
        self.ball: Ball = Ball()
        self.scoreboard: Scoreboard = Scoreboard()

        self._setup_controls()
        self.game_is_on: bool = True

    def _setup_screen(self) -> Screen:
        """Create and configure the game window."""
        screen = Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor("black")
        screen.title("Pong Game")
        screen.tracer(0)
        return screen

    def _setup_controls(self) -> None:
        """Bind keyboard controls to left paddle movement."""
        self.screen.listen()
        self.screen.onkey(self.right_paddle.up, "Up")
        self.screen.onkey(self.right_paddle.down, "Down")

    def _check_wall_collision(self) -> None:
        """Reverse ball direction if it collides with top or bottom wall."""
        if self.ball.ycor() > WALL_LIMIT or self.ball.ycor() < -WALL_LIMIT:
            self.ball.bounce_y()

    def _check_paddle_collision(self) -> None:
        """Handle ball collision with paddles."""
        right_collision = (
            self.ball.distance(self.right_paddle) < COLLISION_DISTANCE_PADDLE
            and self.ball.xcor() > PADDLE_COLLISION_X
        )
        left_collision = (
            self.ball.distance(self.left_paddle) < COLLISION_DISTANCE_PADDLE
            and self.ball.xcor() < -PADDLE_COLLISION_X
        )
        if right_collision or left_collision:
            self.ball.bounce_x()

    def _check_score(self) -> None:
        """Update score if a paddle misses the ball."""
        if self.ball.xcor() > PADDLE_MISS_X:
            self.scoreboard.increase_left_score()
            self.ball.reset_position()
        elif self.ball.xcor() < -PADDLE_MISS_X:
            self.scoreboard.increase_right_score()
            self.ball.reset_position()

        # Check for game over
        if self.scoreboard.left_score >= MAX_SCORE or self.scoreboard.right_score >= MAX_SCORE:
            self.scoreboard.game_over()
            self.game_is_on = False

    def _move_ai(self) -> None:
        """Simple AI Bot to move the right paddle toward the ball."""
        if self.ball.ycor() > self.left_paddle.ycor():
            self.left_paddle._move(min(AI_SPEED, self.ball.ycor() - self.left_paddle.ycor()))
        elif self.ball.ycor() < self.left_paddle.ycor():
            self.left_paddle._move(-min(AI_SPEED, self.left_paddle.ycor() - self.ball.ycor()))

    def run(self) -> None:
        """Start and maintain the main game loop with AI Bot."""
        while self.game_is_on:
            self.screen.update()
            time.sleep(self.ball.move_speed)

            self.ball.move()
            self._check_wall_collision()
            self._check_paddle_collision()
            self._check_score()
            self._move_ai()

        self.screen.exitonclick()