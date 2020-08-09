sudo cp ../service/* /etc/systemd/system

sudo systemctl start new_materials_listener.service
sudo systemctl start new_materials_worker.service

sudo systemctl enable new_materials_listener.service
sudo systemctl enable new_materials_worker.service
