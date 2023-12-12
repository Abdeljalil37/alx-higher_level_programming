#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      return (new class Rectangle {}());
    }
  }
}
module.exports = Rectangle;
