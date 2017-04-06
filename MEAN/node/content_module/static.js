var http = require('http');
var fs = require('fs');
module.exports = function(request,response){
  if(request.url === '/'){
    fs.readFile('views/index.html', 'utf8', function (errors, contents){
      response.write(contents); 
      response.end();
    });
  } else if(request.url === '/dojo'){
    fs.readFile('views/dojo.html', 'utf8', function (errors, contents){
      response.write(contents);
      response.end();
    });
  } else if(request.url === '/stylesheet/style.css'){
    fs.readFile('stylesheet/style.css', 'utf8', function (errors, contents){
      response.write(contents);
      response.end();
    });
  } else {
      response.end('File not found!!!');
  }
}
// refactor
// split url @ '/' have switch cases for different element[1] for pages
// split url @ '.' have switch cases for different element[1] for .css or .jpg