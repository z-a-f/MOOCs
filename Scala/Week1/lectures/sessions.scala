

// Use :load <filename> to use the file
object session {
  // 1 + 3
  def abs(x: Double) = if (x < 0) -x else x

  def sqrt(x: Double) = {

    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess
      else sqrtIter(improve(guess))

    def isGoodEnough(guess: Double) = {
      abs(guess*guess / x - 1) < 0.001
    }

    def improve(guess: Double) =
      (guess + x/guess) / 2

    sqrtIter(1.0)
  }
  sqrt(2)
}
