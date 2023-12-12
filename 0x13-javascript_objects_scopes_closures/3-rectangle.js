#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      return new class rectangle{};
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

module.exports = Rectangle;
