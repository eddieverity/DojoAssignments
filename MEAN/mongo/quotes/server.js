var express = require('express');
var app = express();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/quote');

var QuoteSchema = new mongoose.Schema({
 name: String,
 quote: String
}, {timestamps:true})
// next two lines could be combined to 'var Quote = mongoose.model('Quote', QuoteSchema);'
mongoose.model('Quote', QuoteSchema); 
var Quote = mongoose.model('Quote')

var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// Routes
// Root Request
app.get('/', function(req, res) {
  res.render("index");
});

app.post('/quote', function(req, res) {
  console.log("POST DATA", req.body);
  var quote = new Quote({name: req.body.name, quote: req.body.quote});
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  quote.save(function(err) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong');
    } else { // else console.log that we did well and then redirect to the root route
      console.log('successfully added a quote!');
      res.redirect('quotes');
    }
  })
})

app.get('/quotes', function(req, res){
  Quote.find({}, null, {sort:'-createdAt'}, function(err, quote){
    if(err) {
      console.log('something goofed')
    } else {
      console.log('retrieval successful')
      console.log(quote)
      res.render('quotes', {quote:quote})
    }
  })
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})