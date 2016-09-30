package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
    * Exercise 1
    */
  def pascal(c: Int, r: Int): Int =
    if (r <= 0 || r == c || c == 0) 1
    else pascal(c, r-1) + pascal(c-1, r-1)
  
  /**
    * Exercise 2
    */
  def balance(chars: List[Char]): Boolean = {
    def balanceRec(chars: List[Char], count: Int): Boolean =
      if (chars.isEmpty) count == 0
      else
        if (chars.head == '(') balanceRec(chars.tail, count + 1)
      else if (chars.head == ')') {
        if (count == 0) false
        else balanceRec(chars.tail, count - 1)
      }
      else balanceRec(chars.tail, count)
    balanceRec(chars, 0)
  }
  
  /**
    * Exercise 3
    */
  def countChange(money: Int, coins: List[Int]): Int = {
    def count(money: Int, coins: List[Int]): Int = {
      if (money < 0 || coins.isEmpty) 0
      else if (money == 0) 1
      else count(money, coins.tail) + count(money - coins.head, coins)
    }
    count(money, coins)
  }
}
