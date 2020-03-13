from kwargs_constr import Tag

paragraph = Tag(
	"p",
	klass=("text-align-right", "text-nice"),
	id="heading-text",
	data_bind="not-above"
)
paragraph.text = "Some text inside tag"
print(paragraph)