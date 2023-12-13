#!/usr/bin/node
exports.converter = function (base) {
  return nbr => nbr.toString(base);
};
