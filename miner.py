import math

import amulet
import csv
levelpath = "/path/to/world"
level = amulet.load_level(levelpath)
x = 0
z = 0
def getChunkCords(x, z):
	X = math.floor(x/16)
	Z = math.floor(z/16)
	return [X,Z]
blocks = []
blockCols = {}
for x in range(0, 128):
	col = {str(x+1):[]}
	blockCols = blockCols | col

def newRow():
	newrow = blockCols.copy()
	return newrow
for z in range(1,128):
	row = newRow()
	for x in range(1,129):
		cords = getChunkCords(x, z)
		if not level.chunks.has_chunk("minecraft:overworld", cords[0], cords[1]):
			row[str(x)] = None
		else:
			b1 = level.get_block(x,-57,z, "minecraft:overworld").base_name
			b2 = level.get_block(x,-58,z, "minecraft:overworld").base_name
			b3 = level.get_block(x,-59,z, "minecraft:overworld").base_name
			b4 = level.get_block(x,-60,z, "minecraft:overworld").base_name
			b = [b1,b2,b3,b4]
			row[str(x)] = b
	blocks.append(row)
with open('blocks.csv', 'w', newline='') as csvfile:
		colnames = blocks[0].keys()
		writer = csv.DictWriter(csvfile, fieldnames=colnames, delimiter=':')
		writer.writeheader()
		writer.writerows(blocks)

