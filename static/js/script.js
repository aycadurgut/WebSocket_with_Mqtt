var mqtt = require("mqtt");
const express = require('express')
const http = require('http')
const socketIo = require('socket.io')
const cors = require('cors')

const app = express();
app.use(express.json()); 
// app.use(cors({
//   origin: '*', 
//   methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
//   allowedHeaders: ['Content-Type', 'Access-Control-Allow-Headers'],
// }));
app.use(cors());
app.use(function (req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Headers');
  next();
});

const server = http.createServer(app);

const io = socketIo(server);

io.on('connection', (socket) => {
  console.log(`${Date(Date.now()).toLocaleString()}: yeni bir istemci bağlandı`);
})

var options = {
  protocol: "mqtt/tcp",
  username: "ayca",
  password: "kiviseverim",
  keepalive: 20,
  clientId: "mqttjs_" + Math.random().toString(16).substring(2, 8),
};

var client = mqtt.connect("mqtt://95.70.201.96:39039", options);

client.on('connect', () => {
  client.subscribe("test/topic");
  console.log("Client subscribed mqtt://95.70.201.96:39039");
})

client.on('message', async (topic, message) => {
  const payload = message.toString();
  console.log('Received message:', payload);

  try{
    const parsedData = JSON.parse(payload);
    io.emit('mqttData', parsedData); 
  }
  catch(err){
    console.error('hata mesajı:', err);
  }
})

server.listen(3000, () => {
  console.log("running on port 3000")
})