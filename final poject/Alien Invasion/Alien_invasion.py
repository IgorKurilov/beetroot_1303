import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from results import save_results, get_top_results

class AlienInvasion:
    """Class that manages the resources and behavior of the game."""
    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        
        # Initialize the mixer
        pygame.mixer.init()

        # Create an instance to store game statistics and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Create Play button
        self.play_button = Button(self, "Play")
        
        # Manually create the results button at a different position
        self.results_button = Button(self, "Results")
        self.results_button.rect.top = self.play_button.rect.bottom + 20
        self.results_button.prep_msg("Results")

        # Game title and author
        self.title_font = pygame.font.SysFont(None, 100)
        self.author_font = pygame.font.SysFont(None, 50)

        # Player name
        self.player_name = ""

    def run_game(self):
        """Start the main game loop."""
        self._show_title_screen()
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()

    def _show_title_screen(self):
        """Display the title screen with the game name and author."""
        title_surface = self.title_font.render("BEETROOT ACADEMY PRESENT", True, (255, 255, 255))
        author_surface = self.author_font.render("Alien Invasion by Igor Kurilov", True, (255, 255, 255))
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(title_surface, (self.settings.screen_width // 2 - title_surface.get_width() // 2, self.settings.screen_height // 3))
        self.screen.blit(author_surface, (self.settings.screen_width // 2 - author_surface.get_width() // 2, self.settings.screen_height // 2))

        pygame.display.flip()
        sleep(3)

        self._show_opening_crawl()

    def _show_opening_crawl(self):
        """Display the opening crawl text similar to Star Wars."""
        # Load and play the Star Wars theme music
        pygame.mixer.music.load('star_wars_theme.mp3')
        pygame.mixer.music.play(-1)  # Play the music indefinitely

        crawl_text = [
            "In a distant galaxy, far, far away...",
            "",
            "The peaceful planet of Ukraine has been",
            "invaded by the evil Alien Putin fleet.",
            "",
            "You, the brave Ukrainian pilot, must defend the planet",
            "and save its inhabitants from destruction.",
            "",
            "",
            "",
            "for move left - arrow left, for move right - arrow right",
            "for fire - space, quit the game - q",
            "",
            "Prepare for battle..."
        ]

        font = pygame.font.SysFont(None, 50)
        rendered_text = [font.render(line, True, (255, 255, 255)) for line in crawl_text]
        
        scroll_speed = 4
        scroll_pos = self.settings.screen_height

        while scroll_pos > -len(rendered_text) * 50:
            self.screen.fill((0, 0, 0))
            for i, line in enumerate(rendered_text):
                self.screen.blit(line, (self.settings.screen_width // 2 - line.get_width() // 2, scroll_pos + i * 50))

            pygame.display.flip()
            scroll_pos -= scroll_speed
            sleep(0.05)
        
        # Stop the music after the crawl
        pygame.mixer.music.stop()

        self._main_menu()

    def _main_menu(self):
        """Display the main menu with options to view results or start the game."""
        menu_font = pygame.font.SysFont(None, 50)
        menu_options = ["1. View Top Results", "2. Start Game"]
        
        self.screen.fill((0, 0, 0))
        for i, option in enumerate(menu_options):
            option_surface = menu_font.render(option, True, (255, 255, 255))
            self.screen.blit(option_surface, (self.settings.screen_width // 2 - option_surface.get_width() // 2, self.settings.screen_height // 2 + i * 60))

        pygame.display.flip()
        
        selected = False
        while not selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self._show_top_results()
                        selected = True
                    elif event.key == pygame.K_2:
                        self._get_player_name()
                        selected = True

    def _show_top_results(self):
        """Display the top results from the results file."""
        top_results = get_top_results()
        self.screen.fill((0, 0, 0))
        results_font = pygame.font.SysFont(None, 50)
        title_surface = results_font.render("Top Results:", True, (255, 255, 255))
        self.screen.blit(title_surface, (self.settings.screen_width // 2 - title_surface.get_width() // 2, self.settings.screen_height // 4))
        
        for i, result in enumerate(top_results):
            result_surface = results_font.render(f"{i + 1}. {result}", True, (255, 255, 255))
            self.screen.blit(result_surface, (self.settings.screen_width // 2 - result_surface.get_width() // 2, self.settings.screen_height // 4 + 60 * (i + 1)))

        pygame.display.flip()
        sleep(5)
        self._show_title_screen()

    def _get_player_name(self):
        """Prompt the player to enter their name."""
        self.screen.fill((0, 0, 0))
        prompt_font = pygame.font.SysFont(None, 50)
        prompt_surface = prompt_font.render("Enter your name and press Enter:", True, (255, 255, 255))

        input_box = pygame.Rect(self.settings.screen_width // 4, self.settings.screen_height // 2, 400, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            self.player_name = text
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill((0, 0, 0))
            self.screen.blit(prompt_surface, (self.settings.screen_width // 4, self.settings.screen_height // 3))
            txt_surface = prompt_font.render(text, True, color)
            width = max(400, txt_surface.get_width() + 10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.screen, color, input_box, 2)

            pygame.display.flip()
        
        self._start_game()

    def _check_events(self):
        """Monitor mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when the player clicks on the Play button."""
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        results_button_clicked = self.results_button.rect.collidepoint(mouse_pos)

        if play_button_clicked and not self.stats.game_active:
            self._get_player_name()
        
        if results_button_clicked:
            self._show_top_results()

    def _start_game(self):
        """Start a new game."""
        # Reset the game settings
        self.settings.initialize_dynamic_settings()
        
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        
        # Get rid of any remaining aliens or bullets
        self.aliens.empty()
        self.bullets.empty()
        
        # Create new fleet and put the ship in the center
        self._create_fleet()
        self.ship.center_ship()
        
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keyreleases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any alien has reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Check if the fleet is at the edge, then, update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.ship.center_ship()
        
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self._show_game_over_screen()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        self.sb.show_score()
        
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.results_button.draw_button()
        
        pygame.display.flip()

    def _show_game_over_screen(self):
        """Show the game over screen and the top scores."""
        save_results(self.player_name, self.stats.score)
        top_results = get_top_results()
        
        print("Game Over!")
        print("Top Scores:")
        for result in top_results:
            print(result)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

