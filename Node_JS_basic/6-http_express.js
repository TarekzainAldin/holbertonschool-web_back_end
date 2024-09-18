/* eslint-disable no-undef */
//import the experss moudle 
const experss = require('express');


// intialize the Experss application 
const app = experss();


//Define a reout for the root URL 

app.get ('/',(req, res)=> {
    res.send('Hello Holberton Shcool');
});


//make the app listen on port 12345
const port = 12345;
app.listen (port,() => {
    console.log('server is runing on port ${port}');
});

// export the app for use in other modules 
module.exports = app ;
