courses = [
    ["Fondamenti di Informatica", "https://univr.zoom.us/j/89142818751?pwd=RGNmVElXNFl0NUphbTVxN01BTVh0dz09"],
    ["Elaborazione di Segnali ed Immagini", "https://applications.zoom.us/lti/rich/j/84623257111?oauth_consumer_key=AdaKUROSRAmSJqljBFvBRQ&lti_scid=1ec3ee99e350ad69e2670c4d7d70dbf280150e9647522e9743ccb5247e5c870d"],
    ["Grafica al Calcolatore", "https://univr.zoom.us/j/99731734796"],
    ["Linguaggi", "https://applications.zoom.us/lti/rich/j/96212365912?oauth_consumer_key=AdaKUROSRAmSJqljBFvBRQ&lti_scid=b63b065e499a144d0d1fbd84b7bd73eac2ec7ecc9efb1d9f01b50b740a488205"]
]

template = '<meta http-equiv="refresh" content="0; url={}">'

for name, url in courses:
    with open(name + ".html", "w") as f:
        f.write(template.format(url))
