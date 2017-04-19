console.log("/server/models/schema.js");

var mongoose = require("mongoose");
var bcrypt = require("bcryptjs")

var userSchema = mongoose.Schema({
    username: {
        type: String, 
        required: true,
        unique: true,
        minlength: 3,
        maxlength: 20},
    

    email: {
        type: String,
        required: true,
        unique: true,
        minlength:8,
        validate: {
            validator: function(value){
                return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(value);
            },
            message: "Email is invalid. Do better."
        },
    },
    password: {
        type: String,
        required: true,
        minlength:8,
        maxlength:1024,
        validate: {
          validator: function( value ) {
            return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,32}/.test( value );
          },
          message: "Password failed validation, you must have at least 1 number, uppercase and special character"
        },
        
    }
        
    }, {timestamps: true});

    

var postSchema = mongoose.Schema({
    _author: {
        type: String,
        ref: 'User',
        required: true
    },
    postText: {
        type: String,
        required: true,
        minlength: 1,
        maxlength: 1000,
    },
    
}, {timestamps: true});

var commentSchema = mongoose.Schema({
    _author: {
        type: String,
        ref: 'User',
        required: true
    },
    _post: {
        type: String, 
        ref: 'Post',
        required: true
    },
    commentText: {
        type: String, 
        minlength: 1,
        maxlength: 1000,
        required: true,
    }
}, {timestamps: true})

userSchema.methods.generateHash = function(password) {
  return bcrypt.hashSync(password, bcrypt.genSaltSync(8));
}

userSchema.methods.validPassword = function(password) {
  return bcrypt.compareSync(password, this.password);
}

userSchema.pre('save', function(done) {
  this.password = this.generateHash(this.password);
  done();
})


mongoose.model('User', userSchema);
mongoose.model('Post', postSchema);
mongoose.model('Comment', commentSchema);