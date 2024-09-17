const { read } = require('fs');
const http = require ('http');
// create the http server and assign it to the 'app' vriable 
const app = http.createServer((req, res ) => {
    // set the response header for plain text 
    res.writeHead(200, {'content-type':'test/plain'});
    

    //wtrite the response message 
     read.end('Hello Holberton School!');

});

// the server should listen on port 12345
app.listen(12345,() => {
    console.log('server is runing on port 12345')
});
// Export the 'app' variable (the server ) to be used elswhere 
module.exports= app;
