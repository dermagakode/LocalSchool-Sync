# Ref https://cloud.google.com/storage/docs/gsutil/commands/rsync

# source = google storage
# destination = relative to current directory
# -d = it will delete all files that not in source
# -r = recursive

dest='teaching-materials'
mkdir -p $dest
gsutil rsync -d -r gs://teaching-materials/ $dest/

# We need some variable to make sure specific path is sync, not all