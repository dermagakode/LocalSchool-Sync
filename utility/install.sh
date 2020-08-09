# Install Redis

sudo apt update
sudo apt install redis

# Install gcloud

echo "Downloading File, it may take a minute or two"
filename=google-cloud-sdk
sdk_link='https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-304.0.0-linux-x86.tar.gz'
wget -cO - $sdk_link > $filename.tar.gz

echo "Extracting data"
tar xvzf $filename.tar.gz

echo "Remove archive and install in system"
rm $filename.tar.gz
./$filename/install.sh
