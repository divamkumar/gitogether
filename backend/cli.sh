#Running this file will (1)
# (1) Add the Root Certificate File required to connect to the database
# (2) Enter SQL console mode

# Remember to "refresh" this project every time you add the certificate
#Sean: Added this in because replit will 'forget' certification after a period of inactivity
curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/5b64991a-b651-484a-b504-fab4543ade90/cert

if [ ! -f "cockroach" ]; then
    curl https://binaries.cockroachdb.com/cockroach-v22.1.6.linux-amd64.tgz | tar -xz
    mv ./cockroach-v22.1.6.linux-amd64/cockroach ./cockroach
fi

#This line won't work because I moved $PG_CONN_STRING to be a file variable under DBfunctions.py
./cockroach sql --url $PG_CONN_STRING