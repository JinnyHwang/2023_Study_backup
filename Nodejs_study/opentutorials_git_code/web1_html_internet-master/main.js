var http = require('http');
var fs = require('fs');
var url = require('url');

var app = http.createServer(function(request,response){
    var _url = request.url;
    //console.log(url); // query 정보를 담고 있음
    var queryData = url.parse(request.url, true).query;
    // console.log(queryData); //[Object: null prototype] { id: 'HTML' }
    console.log(queryData.id);
    if(_url == '/'){
      url = '/index.html';
    }
    if(_url == '/favicon.ico'){
      response.writeHead(404);
      response.end();
      return;
    }
    response.writeHead(200);
    console.log(__dirname + url);
    //response.end(fs.readFileSync(__dirname + url));
    //response.end(fs.readFileSync('jieun' + url));
    response.end(queryData.id);

});
app.listen(3000);
