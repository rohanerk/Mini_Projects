import markdown
import webbrowser

with open("example.md","r",encoding = "utf-8") as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)

with open("example.html" , "w", encoding = "utf-8") as f:
    f.write(html_content)

print("Converted to html successfully")

webbrowser.open("example.html")
