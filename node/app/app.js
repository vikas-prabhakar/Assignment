var http = require('http');
var redis = require("redis");
var redisHost = process.env.REDIS_HOST ||"redis" ;
var redisPort = process.env.REDIS_PORT ||6379;
 
var redisClient = redis.createClient({ "host": redisHost, "port": redisPort }); 
 
var PORT = process.env.APP_PORT || 3000;
 
var redisKeyRequestCounter = "visit-count";
 
var server = http.createServer(function handleRequest(req, res) {
    var visitcount = 1;
 
    redisClient.get(redisKeyRequestCounter, function (err, reply) {
        if (err) {
            res.write('Hello World ERROR ' + err);
            res.end();
        } else {
            if (!reply || reply == null) {
                console.log("no value found yet");
                redisClient.set(redisKeyRequestCounter, visitcount);
            } else {
                visitcount = Number(reply) + 1;
                redisClient.set(redisKeyRequestCounter, visitcount);
            }
            res.write('Hello World ');
            res.end();
        }
    })
}).listen(PORT);
 
console.log('Node.JS Server running on port ' + PORT );
