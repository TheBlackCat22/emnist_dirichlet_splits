if [ -d "splits/alpha_$1" ] 
then
    rm -r "splits/alpha_$1"
fi

mkdir "splits/alpha_$1"
cd "splits/alpha_$1"

for ((i=0; i<=($3 - 1); i++))
do
    mkdir "class_${i}"
    cd "class_${i}"
    for ((j=0; j<=($2 - 1); j++))
    do 
    	mkdir "client_${j}"
    done
    cd ..
done
