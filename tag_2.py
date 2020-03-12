from tag_2_constr import Tag

with Tag("body", toplevel=True) as body:
	with Tag("div") as div:
		with Tag("p") as paragraph:
			paragraph.text = "Text is here"
			div.children.append(paragraph)

		body.children.append(div)