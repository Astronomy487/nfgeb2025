import os
import shutil

import xml.etree.ElementTree as ET

def generate_plist_etree(keys, output_path):
	plist = ET.Element("plist", version="1.0")
	dict_el = ET.SubElement(plist, "dict")
	for key in keys:
		k = ET.SubElement(dict_el, "key")
		k.text = key
		s = ET.SubElement(dict_el, "string")
		s.text = f"{key}.glif"
	xml_bytes = ET.tostring(plist, xml_declaration=True, encoding="UTF-8")
	lines = xml_bytes.decode("UTF-8").splitlines()
	#lines.insert(1, DOCT)
	with open(output_path, "w", encoding="UTF-8") as fp:
		fp.write("\n".join(lines))

def generate_glif(save_path, name, unicode_hex, advance_width, contours):
	glyph = ET.Element("glyph", name=name, format="2")
	ET.SubElement(glyph, "unicode", hex=unicode_hex)
	ET.SubElement(glyph, "advance", width=str(advance_width))
	out = ET.SubElement(glyph, "outline")
	for contour in contours:
		cont_el = ET.SubElement(out, "contour")
		for i, (x, y) in enumerate(contour):
			pt_type = "move" if i == 0 else "line"
			ET.SubElement(cont_el, "point", x=str(int(x)), y=str(int(y)), type=pt_type)
	xml_bytes = ET.tostring(glyph, xml_declaration=True, encoding="UTF-8")
	lines = xml_bytes.decode("UTF-8").splitlines()
	#lines.insert(1, DOCT_GLYPH)
	with open(save_path, "w", encoding="UTF-8") as f:
		f.write("\n".join(lines))

def generate_layercontents_plist(path):
	xml = """<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<array>
  <array>
    <string>public.default</string>
    <string>glyphs</string>
  </array>
</array>
</plist>
"""
	with open(path, "w", encoding="UTF-8") as f:
		f.write(xml)

def generate_metainfo_plist(path):
	xml = """<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>creator</key>
  <string>astronomy487</string>
  <key>formatVersion</key>
  <integer>3</integer>
  <key>formatVersionMinor</key>
  <integer>0</integer>
</dict>
</plist>
"""
	with open(path, "w", encoding="UTF-8") as f:
		f.write(xml)

characters = [
    {
        "name": "b",
        "hex": "0062",
        "contours": [
			"05 55 54 34 33 53 50 00 03 23 24 04",
			"12 11 41 42"
		]
    },
    {
        "name": "d",
        "hex": "0064",
        "contours": [
			"05 15 11 21 25 35 31 41 45 55 50 00"
		]
    },
    {
        "name": "f",
        "hex": "0066",
        "contours": [
			"05 55 54 34 31 41 43 53 50 00 01 21 24 14 12 02"
		]
    },
    {
        "name": "g",
        "hex": "0067",
        "contours": [
			"05 55 50 00",
			"14 11 41 44"
		]
    },
    {
        "name": "h",
        "hex": "0068",
        "contours": [
			"05 15 13 43 45 55 50 00",
			"12 11 41 42"
		]
    },
    {
        "name": "j",
        "hex": "006A",
        "contours": [
			"05 55 54 04",
			"03 53 52 02",
			"01 51 50 00"
		]
    },
    {
        "name": "k",
        "hex": "006B",
        "contours": [
			"05 55 50 40 44 14 10 00",
			"23 33 30 20"
		]
    },
    {
        "name": "l",
        "hex": "006C",
        "contours": [
			"05 15 13 23 25 35 33 43 45 55 52 32 31 51 50 00 01 21 22 02"
		]
    },
    {
        "name": "m",
        "hex": "006D",
        "contours": [
			"05 55 54 34 30 20 24 04",
			"03 13 10 00",
			"43 53 50 40"
		]
    },
    {
        "name": "n",
        "hex": "006E",
        "contours": [
			"05 15 11 21 25 55 50 40 44 34 30 00"
		]
    },
    {
        "name": "p",
        "hex": "0070",
        "contours": [
			"05 15 13 23 25 55 52 42 44 34 32 02",
			"01 51 50 00"
		]
    },
    {
        "name": "r",
        "hex": "0072",
        "contours": [
			"05 55 52 42 44 14 12 02",
			"01 21 23 33 31 51 50 00"
		]
    },
    {
        "name": "s",
        "hex": "0073",
        "contours": [
			"05 55 50 40 44 14 10 00"
		]
    },
    {
        "name": "t",
        "hex": "0074",
        "contours": [
			"05 15 13 23 25 55 50 40 42 32 30 00",
			"12 11 21 22",
			"34 33 43 44"
		]
    },
    {
        "name": "v",
        "hex": "0076",
        "contours": [
			"05 55 54 04",
			"03 53 52 32 30 20 22 02"
		]
    },
    {
        "name": "w",
        "hex": "0077",
        "contours": [
			"05 55 54 34 31 51 50 00 01 21 24 04"
		]
    },
    {
        "name": "z",
        "hex": "007A",
        "contours": [
			"05 55 54 14 11 51 50 00"
		]
    },
    {
        "name": "eng",
        "hex": "014B",
        "contours": [
			"05 55 50 40 42 12 10 00 03 43 44 04"
		]
    },
    {
        "name": "esh",
        "hex": "0283",
        "contours": [
			"05 55 50 00",
			"14 11 21 24",
			"34 31 41 44"
		]
    },
    {
        "name": "ezh",
        "hex": "0292",
        "contours": [
			"25 35 33 53 50 40 42 12 10 00 03 23"
		]
    },
    {
        "name": "dezh",
        "hex": "02A4",
        "contours": [
			"05 35 34 14 12 02",
			"45 55 50 00 01 21 23 43",
			"32 31 41 42"
		]
    },
    {
        "name": "tesh",
        "hex": "02A7",
        "contours": [
			"45 55 50 00 01 41 42 02 03 43"
		]
    },
    {
        "name": "theta",
        "hex": "03B8",
        "contours": [
			"05 55 50 00",
			"14 13 23 24",
			"12 11 21 22",
			"32 31 41 42",
			"34 33 43 44"
		]
    },
    {
        "name": "eth",
        "hex": "00F0",
        "contours": [
			"05 55 54 14 13 53 52 32 30 20 22 02"
		]
    },
	{
		"name": "0",
		"hex": "0030",
		"contours": [
			"03 13 10 00"
		]
	},
	{
		"name": "1",
		"hex": "0031",
		"contours": [
			"03 13 11 31 30 00"
		]
	},
	{
		"name": "2",
		"hex": "0032",
		"contours": [
			"03 33 32 12 10 00"
		]
	},
	{
		"name": "3",
		"hex": "0033",
		"contours": [
			"03 33 32 12 11 31 30 00"
		]
	},
	{
		"name": "period",
		"hex": "002E",
		"contours": [
			"01 11 10 00"
		]
	},
	{
		"vowel": True,
		"name": "a",
		"hex": "0061",
		"contours": [
			"27 57 56 26"
		]
	},
	{
		"vowel": True,
		"name": "e",
		"hex": "0065",
		"contours": [
			"07 37 36 06"
		]
	},
	{
		"vowel": True,
		"name": "i",
		"hex": "0069",
		"contours": [
			"09 39 38 08"
		]
	},
	{
		"vowel": True,
		"name": "o",
		"hex": "006F",
		"contours": [
			"09 59 58 08"
		]
	},
	{
		"vowel": True,
		"name": "u",
		"hex": "0075",
		"contours": [
			"29 59 58 28"
		]
	}
]

def lerp(a, b, amt):
	return a*(1-amt) + b*amt

def get_reindex_sequence(amt): #amt in [0, 1]
	amt = (amt-0.5)*0.9+0.5
	return [
		lerp(0, 0, amt),
		lerp(0, 800/3, amt),
		lerp(400, 800/3, amt),
		lerp(400, 1600/3, amt),
		lerp(800, 1600/3, amt),
		lerp(800, 800, amt),
		lerp(1200, 800, amt),
		lerp(1200, 3200/3, amt),
		lerp(-400, -800/3, amt),
		lerp(-400, 0, amt)
	]

axes = [
	{
		"code": "wght",
		"text": "Weight",
		"default": 0.375,
		"m": 800, "b": 100
	},
	{
		"code": "CNTR",
		"text": "Contrast",
		"default": 0.5
	},
	{
		"code": "wdth",
		"text": "Stretch",
		"default": 0.5,
		"m": 160, "b": 20
	},
	{
		"code": "DIDI",
		"text": "Diacritic distance",
		"default": 1
	},
	{
		"code": "GAPP",
		"text": "Gap",
		"default": 0.5
	}
]

for axis in axes:
	if not("m" in axis):
		axis["m"] = 1
	if not("b" in axis):
		axis["b"] = 0
	#affine transformation to apply to internal axes to get external axis 

sources = [[]]

for axis in axes:
	new_sources = []
	for source in sources:
		new_sources.append(source + [0])
		new_sources.append(source + [1])
		if (axis["default"] != 0 and axis["default"] != 1):
			new_sources.append(source + [axis["default"]])
	sources = new_sources

sources = [{"stylename": str(i+1), "axisvalues": b} for i, b in enumerate(sources)]

for d in os.listdir('sources'):
	if d.endswith('.ufo') and os.path.isdir(os.path.join('sources',d)):
		shutil.rmtree(os.path.join('sources',d))

for source in sources:
	ax01, ax02, ax03, ax04, ax05 = source["axisvalues"]
	
	dir = "sources/NFGEB2025-"+source["stylename"]+".ufo"
	os.mkdir(dir)
	os.mkdir(dir+"/glyphs")
	
	stroke_width = ax01 * min(2*ax02, 1)
	stroke_height = ax01 * min(1, 2-2*ax02)
	
	x_reindex = get_reindex_sequence(stroke_width)
	y_reindex = get_reindex_sequence(stroke_height)
	x_multiplier = [
		0.2, 1, 1.8
	][int(ax03*2)]
	
	#gap = x_reindex[2] - x_reindex[1]
	#gap *= x_multiplier
	
	#gap = 50 + 200*ax05
	
	gap_reindex_sequence = get_reindex_sequence(max(stroke_width, stroke_height))
	gap = (gap_reindex_sequence[2] - gap_reindex_sequence[1]) * x_multiplier * ((ax05-0.5)*0.9+0.5)*2
	
	generate_plist_etree((x["name"] for x in characters), dir+"/glyphs/contents.plist")
	for character in characters:
		new_contours = []
		max_x = 0
		max_y = 0
		for contour in character["contours"]:
			new_contour = []
			for pair in contour.split(" "):
				x = int(pair[0])
				x = x_reindex[x]*x_multiplier
				y = int(pair[1])
				y = y_reindex[y]
				if ax04 == 0:
					if y > 800:
						y -= (y_reindex[6] - y_reindex[5])*0.8
					if y < 0:
						y -= (y_reindex[9] - y_reindex[0])*0.8
				new_contour.append((x, y))
			max_x = max(max_x, max(point[0] for point in new_contour))
			max_y = max(max_y, max(point[1] for point in new_contour))
			new_contours.append(new_contour)
		if ("vowel" in character):
			new_contours = [
				[(x - gap/2 - 800*x_multiplier, y) for x, y in new_contour]
				for new_contour in new_contours
			]
		else:
			shift_amount = 400 - 0.5 * max_y
			new_contours = [
				[(x + gap/2, y + shift_amount) for x, y in new_contour]
				for new_contour in new_contours
			]
			
		generate_glif(dir+"/glyphs/"+character["name"]+".glif", character["name"], character["hex"], 0 if ("vowel" in character) else (max_x+gap), new_contours)
		
	generate_layercontents_plist(dir+"/layercontents.plist")
	generate_metainfo_plist(dir+"/metainfo.plist")

if os.path.isfile("NFGEB2025.designspace"):
	os.remove("NFGEB2025.designspace")
designspace = ET.Element("designspace", format="3.0")
axesxml = ET.SubElement(designspace, "axes")
for axis in axes:
	axisxml = ET.SubElement(axesxml, "axis", tag=axis["code"], name=axis["text"], minimum=str(axis["b"]), default=str(axis["m"]*axis["default"]+axis["b"]), maximum=str(axis["b"]+axis["m"]))
sourcesxml = ET.SubElement(designspace, "sources")
for source in sources:
	sourcexml = ET.SubElement(sourcesxml, "source", filename="sources/NFGEB2025-"+source["stylename"]+".ufo", familyname="NFGEB2025", stylename=source["stylename"])
	locationxml = ET.SubElement(sourcexml, "location")
	for i, axis in enumerate(axes):
		ET.SubElement(locationxml, "dimension", name=axis["text"], xvalue=str(axis["m"]*source["axisvalues"][i]+axis["b"]))
with open("NFGEB2025.designspace", "w", encoding="UTF-8") as fp:
	fp.write(ET.tostring(designspace, xml_declaration=True, encoding="UTF-8").decode("UTF-8"))

os.system("fontmake -m NFGEB2025.designspace -o variable --output-path NFGEB2025.ttf")