#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (x) {
    if (x === undefined) { this.print(); } else {
      for (let i = 0; i < this.height; i++) { console.log(x.repeat(this.width)); }
    }
  }
};
