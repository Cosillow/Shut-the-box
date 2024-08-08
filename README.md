# Shut the Box

## How to play
- shut the box to win (close all panels)
- if you chose, you may roll one die after you close all numbers above six
- you may shut any number of panels that sum to your roll

## Why Shut the Box?
My grandfather stumbled upon this game in the newspaper once and he decided to make the game for myself and other family members. Since then, it has been a beloved game in my family and a talking point about how "There could be an app for that!"

Of course, there are many apps for this.

Nonetheless, I tried my hand at making a clone at the beginning of my programming journey with visual basic. Now, with quite a bit more knowledge and far less spaghetti code, I have completed a working version of this family gathering staple.

---
## TODO:
- restart button
- automatically select the lower die when the larger panels are all closed (user can move it back if they want)
    - will I be able to do this so it only adjusts the first time?
    - if it checks after every turn to adjust selected to largest die needed, then theyll have to keep adjusting
    - check every time, keep a largestDieNeeded and only do the switch when the newly calculated newLargestDieNeeded is different
- easy mode sum
    - super easy mode difference? (too ez --> no)
- use "bots" to figure out best strategies