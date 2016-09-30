
object ex2 {
  /*
  def sum(f: Int => Int, a: Int, b: Int) = {
    def loop (a: Int, acc: Int): Int =
      if (a > b) acc
      else loop (a + 1, f(a) + acc)
    loop(a, 0)
  }

  def product(f: Int => Int)(a: Int, b: Int): Int = {
    if (a > b) 1
    else f(a) * product(f)(a + 1, b)
  }

  def factorial(a: Int): Int = product(x=>x)(1, a)
   */

  def mapReduce(f: Int => Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b: Int): Int =
    if (a > b) zero
    else combine(f(a), mapReduce(f, combine, zero)(a+1, b))

  def prodNew(f: Int => Int)(a: Int, b: Int): Int = mapReduce(f, (x, y) => x*y, 1)(a, b)
  def sumNew(f: Int => Int)(a: Int, b: Int): Int = mapReduce(f, (x, y) => x+y, 0)(a, b)
}


import math.abs
object ex2a {
  val tolerance = 0.0001
  def isCloseEnough(x: Double, y: Double) =
    abs((x - y) / x) / x < tolerance
  def fixedPoint(f: Double => Double)(firstGuess: Double) = {
    def iterate(guess: Double): Double = {
      val next = f(guess)
      if (isCloseEnough(guess, next)) next
      else iterate(next)
    }
    iterate(firstGuess)
  }

  def averageDamp(f: Double => Double)(x: Double) =
    (x + f(x)) / 2

  def sqrt(x: Double) =
    fixedPoint(averageDamp(y => x / y))(1.0)
}
