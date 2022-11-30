cd /Users/alanferia/Downloads/images/

mkdir Bird
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/birdPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Bird/; 
done

mkdir Empty
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/emptyPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Empty/; 
done

mkdir Fox
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/foxPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Fox/; 
done

mkdir Human
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/humanPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Human/; 
done

mkdir Other
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/otherPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Other/; 
done

mkdir Rodent
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/rodentPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Rodent/; 
done

mkdir Skunk
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/skunkPath.txt); 
do 
    mv "$file" /Users/alanferia/Downloads/images/Skunk/; 
done
