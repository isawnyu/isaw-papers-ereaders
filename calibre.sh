python cleaning_epub.py
for i in `seq 1 14`; do

    for j in $i/images/*.png; do
        printf "Resize $i\n"
        convert "$j" -resize 640x480 "$j"
    done
    
    ebook-convert $i/isaw-papers-$i-ereaders.xhtml $i/isaw-papers-$i.epub --cover cover.png --preserve-cover-aspect-ratio 
    ebook-convert $i/isaw-papers-$i.epub $i/isaw-papers-$i.mobi  --no-inline-toc
done
