const { createProxyMiddleware } = require('http-proxy-middleware')
//Use this to create a proxy to the Express server port 5000 instead of specifying proxy in package.json
module.exports = app => {
    //Sends proxy request to http://localhost:5000/*
    app.use('/server/*', createProxyMiddleware({ target:     `http://localhost:5000`, changeOrigin: true }))
};