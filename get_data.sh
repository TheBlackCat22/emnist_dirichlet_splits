if [ -d "emnist_byclass" ] 
then
    rm -r "emnist_byclass"
fi

mkdir emnist_byclass
cd emnist_byclass

mkdir Processed
cd Processed
mkdir test_images
mkdir train_images
cd ..

echo 
echo "Downloading Data"
wget https://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip
unzip gzip.zip
mv gzip raw
cd ..

echo
echo "Started create_png.py"
python code/create_png.py
