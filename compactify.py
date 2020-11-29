"""
Atomic Blender Name Compactor
(C) 2020 James Dean
Released under the MIT License

Atomic Blender adds in a bunch of extra element materials every time a new molecule is imported.
This can get kinda unwieldy when you're importing a lot of different molecules into a scene.

To fix the problem, this script finds the 'ball' objects created by Atomic Blender, and
collapses their materials down into a single one. It's saved me probably dozens of hours of
tedium in changing material names.

In effect, all your "Element", "Element.001", ..., "Element.obscenely_high_number_here"
materials all get swapped to just "Element"

Make sure you understand this code before running it. It also goes without saying that you
should *probably* back up your blender project when you run this, in case your materials
get jumbled up.

That being said, this has a high chance of screwing up your object materials if:
    1) you've already got other materials that share names with elements in your moleules
       (e.g. you've already got a material named "Gold" that you're not using for molecules)
    2) you've already got other objects with "ball" or "Stick" in their name that weren't
       created by Atomic Blender
"""

import bpy

scene = bpy.context.scene

# Get a list of meshes that have "ball" or "Sticks" in the name
meshes = [obj for obj in scene.objects if ("ball" in obj.name) or ("Sticks" in obj.name)]
elements = set()
for mesh in meshes:
    # Build up a set of element names to look for in the materials
    if "Stick" in mesh.name:
        elements.add("Stick")
    else:
        elements.add(mesh.name.split("_")[0])
elements = list(elements)

# Build up a dictionary of materials that match our elements.
# Here, we'll only store materials with an elemental name, instead of their copies.
# e.g. if "Gold," "Gold.001", and "Gold.999" were stored, this would only store "Gold"
materials = {}
for material in bpy.data.materials:
    if material.name in elements:
        materials[material.name] = material

# Now, walk through every ball/stick object we collected earlier, and set the materials
for mesh in meshes:
    if "Stick" in mesh.name:
        name = "Stick"
    else:
        name = mesh.name.split("_")[0]
    mesh.active_material = materials[name]
