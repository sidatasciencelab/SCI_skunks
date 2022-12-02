cd /Users/alanferia/Downloads/images/

mkdir Bird
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/birdPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/birdID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Bird/"${name}".jpg; 
    done
done

mkdir Empty
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/emptyPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/emptyID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Empty/"${name}".jpg; 
    done
done

mkdir Fox
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/foxPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/foxID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Fox/"${name}".jpg; 
    done
done

mkdir Human
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/humanPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/humanID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Human/"${name}".jpg; 
    done
done

mkdir Other
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/otherPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/otherID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Other/"${name}".jpg; 
    done
done

mkdir Rodent
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/rodentPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/rodentID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Rodent/"${name}".jpg; 
    done
done

mkdir Skunk
for file in $(cat /Users/alanferia/Downloads/content/fileByCat/skunkPath.txt);
do
    path="${file%/*}";
    for name in $(cat /Users/alanferia/Downloads/content/fileByCat/skunkID.txt);
    do
        echo mv "${file}" /Users/alanferia/Downloads/images/Skunk/"${name}".jpg; 
    done
done