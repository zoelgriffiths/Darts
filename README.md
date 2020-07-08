# Darts
An analysis of where to aim in darts.

There are two scripts here. 

'dartboard.py'draws a dart board with the correct proportions. You'll need to change the font location used in line 71.

'darts_analysis.py' is a visual analysis of where it is best for darts players of different ability levels to aim. 

If you run the program, you'll end up with a set of images saved in your folder. You'll have two images per player skill level (aim level) that you test. The first image will show the best places for players with that skill level to target, and the second image will show what 10,000 (or however many trials you do) shots looks like when a player with that skill level is aiming at the very best place for them to aim at. 

For example, a player with a 'professional' skill level (aim = 2) will be told to aim at triple 20. So the first image will be a yellow dot on triple twenty, and the second image will be a very tight cluster of 10,000 dots around triple 20. Whereas, a very bad player will be told to aim at the bullseye (the closer to the centre they aim the higher the chance they hit the board). The second image for the very bad player will be a scattering of yellow dots all over the board, not a tight cluster, because their aim is very bad. 

I have run my program and taken the first of each of these images for a range of skill levels and turned them into an animation that shows the best places for players to aim at, starting with a professional player and ending with a truly awful player. You can find the animation here: https://www.dropbox.com/s/zr6m9vgwdnt5ikh/darts%20animation.mp4?dl=0
