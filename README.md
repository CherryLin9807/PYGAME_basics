# PYTHON GAMES: use Pygame module to create own little games

1. **References**
    1. Pygame Page: http://pygame.org
    2. documentation: http://pygame.org/docs/ref/
    3. ~~XXXXXXX had forgotten~~ <br><br>
------

**_2. What is Pygame:_**
  * Pygame provides Display, Sound, Image, Text, Event help to make games
  * Pygame can make 2-D little games
  * Pygame detect users using Keyboard, joystick, mouse to control games
  * Pygame provides many built-in game objects to make games

**_3. PYGame Basics_**:
| Code | Desciption |
|:-----:|:----------:|
|_1.py_| Create my game surface, game loop and drawing.|
|_2.py_| Blit text, font, sound and image objects.     |
|_3.py_| Getting user keyboard and collision dection.  |

**_4. Code snippet_**
```python
#Create game display
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Feed the angrybird!")

```
```python
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
```
**_5. Game Assets:_**:
    * [Icon Archive:](https://iconarchive.com/) the website offers a lot of game characters to download
    * [Leshy SFMarker:](https://www.leshylabs.com/apps/sfMaker) the website can download game effects, and it can also make your own simple sound effect
