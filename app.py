import sass

compiled = sass.compile(
    filename="static/scss/styles.scss",
    output_style="compressed",
    include_paths=["node_modules", "static/scss"],
    source_comments=False,
    source_map_filename="static/css/styles.map.css",
)


with open("static/css/styles.css", "w") as f:
    f.write(compiled[0])

with open("static/css/styles.map.css", "w") as f:
    f.write(compiled[1])
