# Commands used with Calibre


## ePub
`ebook-convert isaw-papers-13-ereaders.xhtml isaw-papers-13.epub --cover ../cover.png --preserve-cover-aspect-ratio`

## mobi

`ebook-convert isaw-papers-13.epub isaw-papers-13.mobi  --no-inline-toc`

## All in one
This command line resizes the images, generate the epubs and the mobi file

```bash
for i in 8 9; do
    for j in $i/images/*.png; do
        printf "Resize $i\n"
        convert "$j" -resize 640x480 "$j"
    done
    ebook-convert $i/isaw-papers-$i-ereaders.xhtml $i/isaw-papers-$i.epub --cover cover.png --preserve-cover-aspect-ratio 
    ebook-convert $i/isaw-papers-$i.epub $i/isaw-papers-$i.mobi  --no-inline-toc
done
