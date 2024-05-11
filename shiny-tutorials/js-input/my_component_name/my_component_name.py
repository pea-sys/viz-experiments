from pathlib import PurePath

from htmltools import HTMLDependency, Tag

from shiny.module import resolve_id

# This object is used to let Shiny know where the dependencies needed to run
# our component all live. In this case, we're just using a single javascript
# file but we could also include CSS.
my_component_name_deps = HTMLDependency(
    "my_component_name",
    "1.0.0",
    source={
        "package": "my_component_name",
        "subdir": str(PurePath(__file__).parent / "distjs"),
    },
    script={"src": "index.js", "type": "module"},
)


def my_component_name(id: str):
    """
    A shiny input.
    """
    return Tag(
        # This is the name of the custom tag we created with our webcomponent
        "my-component-name",
        my_component_name_deps,
        # Use resolve_id so that our component will work in a module
        id=resolve_id(id),
    )
