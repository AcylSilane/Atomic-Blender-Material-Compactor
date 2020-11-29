# Atomic Blender Material Compactor
(C) 2020 James Dean

## What is this?
Atomic blender creates a lot of extra materials when importing molecules. This saves time by fixing the names for you.

## Why should I use this?
Atomic Blender adds in a bunch of extra element materials every time a new molecule is imported.
This can get kinda unwieldy when you're importing a lot of different molecules into a scene.

To fix the problem, this script finds the 'ball' objects created by Atomic Blender, and collapses their materials down into a single one. It's saved me probably dozens of hours of tedium in changing material names.

In effect, all your `Element`, `Element.001`, ..., `Element.obscenely_high_number_here` materials all get swapped to just `Element`. Which is useful if all you care about is a uniform look in your renders when it comes to molecules.

## How do I use this?
1. Run the code in `compactify.py` from the scripting window in Blender, and wait a few seconds for your materials to fix themselves.
2. Use the time saved to make yourself a cup of coffee or something.

## Known Issues
Make sure you understand this code before running it. It also goes without saying that you should *probably* back up your blender project when you run this, in case your materials get jumbled up.

That being said, this has a high chance of garbling up your object materials if:
* You've already got other materials that share names with elements in your moleules (e.g. you've already got a material named `Gold` that you're not using for molecules)
* You've already got other objects with "ball" or "Stick" in their name that weren't created by Atomic Blender
