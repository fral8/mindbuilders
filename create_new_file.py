if __name__=="__main__":
    #chiedo la data in formato YYYY-MM-DD
    date = input('Insert date in format YYYY-MM-DD:')
    title = input('Insert article title:')
    filetitle=title
    title=title.replace(":","-")
    title=title.replace(" ","-")
    print("Creating article file....")
    filename=date+"-"+title+".md"
    print("Filename:"+filename)
    
    print("Add content for article")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    content = "\n".join(lines)
    excerpt=input("Add excerpt for article")
    print("Creating header for file...")
    header='''---
layout: single
title:  {title}
categories:
  - setup
  - maker
  - raspberry pi
share: true
excerpt: "{excerpt}"
header:
    teaser: /assets/images/
    overlay_image: /assets/images/
    overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
toc: true

---
'''.format(title=filetitle, excerpt=excerpt)

with open("_posts//"+filename,"w") as f:
    f.write(header+content)


print("All done")