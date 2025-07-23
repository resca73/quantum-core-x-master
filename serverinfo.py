import app

CH1 = {
    'name' : 'InfinityMetin2 CH1',
    'ip' : '127.0.0.1',           # ? Cambia con il tuo IP LAN o pubblico se necessario
    'tcp_port' : 13000,
    'udp_port' : 13000,
    'state' : 'UP',
}

app.ServerList = [CH1]
app.ServerOrderList = [CH1]
app.ChannelName = 'CH1'
