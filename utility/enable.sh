
# Install Redis
sudo apt update
sudo apt install redis

# Install python library
sudo pip3 install -r requirements.txt

# Add to system startup
echo "Add to system startup"
sudo cp ../service/* /etc/systemd/system

sudo systemctl start new_materials_listener.service
sudo systemctl start new_materials_worker.service

sudo systemctl enable new_materials_listener.service
sudo systemctl enable new_materials_worker.service
