var WIDTH=700, HEIGHT=600, pi=Math.PI;
var UpArrow = 38, DownArrow  =40;
var canvas, ctx, keystate;
var player, ai, ball;
var score1 = 0;
var score2 = 0;

player = {

  x: null,
  y: null,
  score1: 0,
  width: 20,
  height: 150,

  update: function(){
      if (keystate[UpArrow]) this.y -=7;
      if (keystate[DownArrow]) this.y +=7;
      this.y = Math.max(Math.min(this.y, HEIGHT-this.height), 0);
  },
  draw: function(){
      ctx.fillRect(this.x, this.y, this.width,this.height);
  }
};
ai = {
  x: null,
  y: null,
  score2: 0,
  width: 20,
  height: 100,
  update: function(){
      var desty = ball.y - (this.height - ball.side)*0.5;
      this.y +=(desty - this.y)*0.1;
      this.y = Math.max(Math.min(this.y, HEIGHT-this.height), 0);
  },
  draw: function(){
      ctx.fillRect(this.x, this.y, this.width,this.height);
  }
};

ball = {
  x: null,
  y: null,
  vel: null,
  speed: 10,
  side: 20,
  serve: function(side){
      var r = Math.random();
      this.x = side===1 ? player.x+player.width : ai.x - this.side;
      this.y = (HEIGHT - this.side)*r;
      var utvinkel = 0.1*pi*(1-2*r);
          this.vel = {
              x: side*this.speed*Math.cos(utvinkel),
              y: this.speed*Math.sin(utvinkel),
            }

        },
  update: function(){
      this.x += this.vel.x;
      this.y += this.vel.y;

      if (0 > this.y || this.y+this.side > HEIGHT){
          var offset  =this.vel.y <0 ? 0 - this.y : HEIGHT - (this.y+this.side);
          this.y += 2*offset;
          this.vel.y *= -1;
      }
      var Omtreff = function(ax,ay,aw,ah,bx,by,bw,bh){
          return ax < bx+bw && ay<by+bh && bx<ax+aw && by< ay+ah;
      };
      var racket = this.vel.x < 0 ? player : ai;
      if (Omtreff(racket.x, racket.y, racket.width, racket.height, this.x, this.y, this.side, this.side)
         ) {
          this.x = racket===player ? player.x+player.width : ai.x - this.side;
          var normal = (this.y+this.side - racket.y)/(racket.height+this.side);
          utvinkel = 0.25*pi*(2*normal-1);
          var smash = Math.abs(utvinkel) > 0.2*pi ? 1.5 : 1 ;
          this.vel.x = smash*(racket === player ? 1 : -1)*this.speed*Math.cos(utvinkel);
          this.vel.y = smash*this.speed*Math.sin(utvinkel);
      }
      if (0 > this.x+this.side) {
          player.score1 +=1
          this.serve(racket === player ? 1 : -1);

      }
      if (this.x > WIDTH){
          ai.score2 +=1
          this.serve(racket === player ? 1 : -1);
      }
  },
  draw: function(){
      ctx.fillRect(this.x, this.y, this.side,this.side);
  }
};
function main(){
  canvas = document.createElement("canvas");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  ctx = canvas.getContext("2d");
  document.body.appendChild(canvas);

  keystate = {};
  document.addEventListener("keydown", function(evt){
      keystate[evt.keyCode] = true;
  });
  document.addEventListener("keyup", function(evt){
      delete keystate[evt.keyCode];
  })
  init();

  var loop = function(){
      update();
      draw();
      window.requestAnimationFrame(loop,canvas);
      };
  window.requestAnimationFrame(loop,canvas);
  }
function init() {
  player.x = player.width;
  player.y = (HEIGHT - player.height)/2;

  ai.x = WIDTH - (player.width + ai.width);
  ai.y = (HEIGHT - ai.height)/2;

  ball.serve(1);

}

function update() {
  ball.update();
  player.update();
  ai.update();


}

function draw() {
  ctx.fillRect(0, 0, WIDTH, HEIGHT);
  ctx.save();
  ctx.fillStyle = "#fff";

  ball.draw();
  player.draw();
  ai.draw();


  var w = 4
  var x = (WIDTH - w)*0.5
  var y = 0;
  var step = HEIGHT/25;
  while (y < HEIGHT){
      ctx.fillRect(x, y+step*0.25,w, step*0.5);
      y += step;
  }
  ctx.restore();
}
main();
