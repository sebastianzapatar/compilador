
let suma = function(a, b) {
  a + b
}


let dobleSuma = function(x, y) {
  suma(x, y) * 2
}


dobleSuma(3, 7)

let factorial = function(n) {
  if (n == 0) {
    1
  } else {
    n * factorial(n - 1)
  }
};

factorial(5)

