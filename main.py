from src.game import Game


def main() -> None:
    """Entry point of the Pong game."""
    game: Game = Game()
    game.run()


if __name__ == "__main__":
    main()