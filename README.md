# Darts
An analysis of where to aim in darts. Read generally about what the code does in my post:https://zoelgriffiths.co.uk/index.php/2020/07/09/where-to-aim-on-a-dart-board/

Below is a more specific explanation of what running the different programs will give you.

There are two python scripts here and an mp4 file.

'draw_dartboard.py'draws a dart board with the correct proportions. You'll need to change the font location used in line 71.

'darts_v3.py' is a visual analysis of where it is best for darts players of different ability levels to aim. It uses the dart board image made in 'draw_dartboard.py'.

If you run the program 'darts_v3.py', you'll end up with a set of images saved in your folder. You'll have two images per player skill level (aim level) that you test. The first image (named 'darts_targets_aim{aim_level}.png') will show the best places for players with that skill level to target, and the second image (named 'darts_aim{aim_level}.png') will show what 10,000 (or however many trials you do) shots looks like when a player with that skill level is aiming at the very best place for them to aim at. 

For example, a player with a 'professional' skill level (aim = 2) will be told to aim at triple 20. So the first image will be a yellow circle on triple twenty to incidate this, and the second image will be a very tight cluster of 10,000 dots around triple 20. Whereas, a very bad player will be told to aim at the bullseye (the closer to the centre they aim the higher the chance they hit the board). The second image for the very bad player will be a scattering of yellow dots all over the board, not a tight cluster, because their aim is very bad. 

I have run my program 'darts_v3.py' and taken the first of each of these images for a range of skill levels and turned them into an animation that shows the best places for players to aim at, starting with a professional player and ending with a truly awful player. The animation is the mp4 file 'darts animation'. 


