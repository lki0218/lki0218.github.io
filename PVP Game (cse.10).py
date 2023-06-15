import arcade

# Window size
window_width = 1400
window_height = 900

# Player size
player_size = 70

# Player speed
player_speed = 30

#Intrucstions/ Starting pg
class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.PALE_PINK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_text("WELCOME TO PVPGAME!", self.window.width / 2, self.window.height / 2+110,
                         arcade.color.BARBIE_PINK, font_size=70, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text(
            "When the two players make contact, their points increase; when they separate, points stop adding ",
            self.window.width / 2,
            self.window.height / 2 + 60,
            arcade.color.WILD_STRAWBERRY, font_size=15, anchor_x="center",font_name="Silom")
        arcade.draw_text("1 player controls ZOMBIE, 1 player controls GIRL", self.window.width / 2, self.window.height / 2,
                         arcade.color.VIOLET_RED, font_size=30, anchor_x="center", font_name="Impact")
        arcade.draw_text(
            "..........  The game is over when it reaches 150  .......... ", self.window.width / 2, self.window.height / 2 - 100,
        arcade.color.STRAWBERRY, font_size=15, anchor_x="center",font_name="Skia")
        arcade.draw_text("CLICK ONCE TO CONTINUE", self.window.width / 2, self.window.height / 2 - 60,
                         arcade.color.TELEMAGENTA, font_size=20, anchor_x="center")
        arcade.draw_text("A,W,S,D & Up, Down, Right, Left",
                     self.window.width / 2, self.window.height / 2 - 170,
                     arcade.color.SHOCKING_PINK, font_size=20, anchor_x="center",font_name="Zapfino")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = PvPGame(window_width, window_height, "PvP Game")
        game_view.setup()
        self.window.show_view(game_view)
class Player(arcade.Sprite):
    def __init__(self, filename, x, y):
        super().__init__(filename)
        self.center_x = x
        self.center_y = y

class PvPGame(arcade.View):
    def __init__(self, width, height, title):
        super().__init__()

        # Window size
        self.width = width
        self.height = height
        self.title = title

        # Background
        self.background = arcade.load_texture("/Users/TheaLau/Downloads/cse.jpg")

        # Look and position
        self.player1 = Player(":resources:images/animated_characters/zombie/zombie_fall.png", 400,
                              500)
        self.player2 = Player(":resources:images/animated_characters/female_adventurer/femaleAdventurer_jump.png", 900, 500)

        # Score
        self.score = 0

        # Set the keys_pressed attribute
        self.keys_pressed = set()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        # Background
        arcade.draw_lrwh_rectangle_textured(10, 10, self.width, self.height, self.background)

        # Drawing players
        self.player1.draw()
        self.player2.draw()

        # Score
        arcade.draw_text(f"Score: {self.score}", 10, self.height - 50, arcade.color.NEON_GREEN, 30)

    # Ensuring that characters move when keys r pressed
    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)

    # Movement control
    def update(self, delta_time):

    #Player 1: Zombie
        if arcade.key.W in self.keys_pressed:
            if self.player1.center_y < self.height - player_size // 2:
                self.player1.center_y += player_speed
        if arcade.key.S in self.keys_pressed:
            if self.player1.center_y > player_size // 2:
                self.player1.center_y -= player_speed
        if arcade.key.A in self.keys_pressed:
            if self.player1.center_x > player_size // 2:
                self.player1.center_x -= player_speed
        if arcade.key.D in self.keys_pressed:
            if self.player1.center_x < self.width - player_size // 2:
                self.player1.center_x += player_speed

        #Player 2: Human
        if arcade.key.UP in self.keys_pressed:
            if self.player2.center_y < self.height - player_size // 2:
                self.player2.center_y += player_speed
        if arcade.key.DOWN in self.keys_pressed:
            if self.player2.center_y > player_size // 2:
                self.player2.center_y -= player_speed
        if arcade.key.LEFT in self.keys_pressed:
            if self.player2.center_x > player_size // 2:
                self.player2.center_x -= player_speed
        if arcade.key.RIGHT in self.keys_pressed:
            if self.player2.center_x < self.width - player_size // 2:
                self.player2.center_x += player_speed

        # Adding points
        if self.player1.collides_with_sprite(self.player2):
            self.score += 1

        # If score greater than 150 then jump to game over pg
        if self.score >= 150:
            view = GameOverView()
            view.window = self.window
            view.window.score = self.score
            self.window.show_view(view)

# Game over pg
class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2 + 30,
                         arcade.color.CADMIUM_YELLOW, font_size=100, anchor_x="center", font_name="Times New Roman")
        arcade.draw_text("Was it fun? If so, play AGAIN!", self.window.width / 2, self.window.height / 2 - 40,
                         arcade.color.CADMIUM_YELLOW, font_size=30, anchor_x="center", font_name="Herculanum")
        arcade.draw_text("CLICK HERE", self.window.width / 2, self.window.height / 2 - 130,
                         arcade.color.CADMIUM_YELLOW, font_size=40, anchor_x="center", font_name="Bodoni 72 Smallcaps Book")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = PvPGame(window_width, window_height, "PvP Game")
        game_view.setup()
        self.window.show_view(game_view)
def main():
    """ Main function """
    window = arcade.Window(1400, 900, "PvPGame")
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()