#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      return new class rectangle {}();
    }
  }
}

Rectangle.prototype.print = function () {
  let myArray = '';
  for (let i = 0; i < this.height; i++) {
    for (let j = 0; j < this.width; j++) {
      myArray += 'X';
    }
    console.log(myArray);
    myArray = '';
  }
};
Rectangle.prototype.rotate = function () {
  [this.width, this.height] = [this.height, this.width];
};

Rectangle.prototype.double = function () {
  this.width = this.width * 2;
  this.height = this.height * 2;
};
module.exports = Rectangle;
