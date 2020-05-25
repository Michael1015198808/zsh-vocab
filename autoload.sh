VOCAB_DATA=~/.vocab
mkdir -p $VOCAB_DATA
if [ -f $VOCAB_DATA/data.json ]; then
    BACKUP_NAME="data.json_"$(date +"%Y_%m_%d_backup")
    echo $BACKUP_NAME
    echo 'old data.json detected! backuped it as' $BACKUP_NAME
    cp $VOCAB_DATA/data.json $VOCAB_DATA/$BACKUP_NAME
fi
mv data.json $VOCAB_DATA/
echo "Loaded file successfully!"
