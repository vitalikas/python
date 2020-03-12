from tag_constructor import Tag

with Tag("h1") as tag:
	tag.text = "Hello"
	tag.attributes["class"] = "my_amazing_class"
	tag.attributes["id"] = "my_id"

with Tag("img", is_single=True) as tag:
	tag.attributes["class"]="my_class"
	tag.attributes["src"]="/tmp/my-logo.svg"