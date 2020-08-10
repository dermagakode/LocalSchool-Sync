# Add to system startup
echo "Add to system startup"
sudo cp ../service/* /etc/systemd/system

sudo systemctl start new_materials_listener.service && \
sudo systemctl enable new_materials_listener.service

sudo systemctl start new_materials_worker.service && \
sudo systemctl enable new_materials_worker.service

# Reload file configuration if changed
sudo systemctl daemon-reload

# Restart, wait for up and show status
sudo systemctl restart new_materials_listener.service && \
sudo systemctl restart new_materials_worker.service && \
echo "Wait for up in 5s" && sleep 5 && \
sudo systemctl status new_materials_listener.service | cat; \
echo "-------------------"; \
sudo systemctl status new_materials_worker.service | cat
