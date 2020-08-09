# LocalSchool-Sync

Sync manage public-private key for rsync method and teaching materials.

NB:

This code should run in Raspberry Pi

## Run Evaluation

```bash
$ cd utility
$ sh install.sh
$ # get local-school.json 
$ # and put to this directory
$ sh register.sh
$ # Below script is to evaluate, but we should change it to async task
$ # to enable more observability and flexibility which content is downloaded
$ sh sync.sh 
$ # enable python script to run at boot
$ sh enable.sh
```