// Функция для вычитания десятичных дробей
fun subtract(a: Double, b: Double): Double {
    return a - b
}

// Функция для вычитания обыкновенных дробей
fun subtract(numeratorA: Int, denominatorA: Int, numeratorB: Int, denominatorB: Int): Fraction {
    val commonDenominator = lcm(denominatorA, denominatorB)
    val resultNumerator = numeratorA * (commonDenominator / denominatorA) - numeratorB * (commonDenominator / denominatorB)

    return Fraction(resultNumerator, commonDenominator)
}

// Функция для нахождения наименьшего общего кратного (НОК)
fun lcm(a: Int, b: Int): Int {
    return (a * b) / gcd(a, b)
}

// Функция для нахождения наибольшего общего делителя (НОД)
fun gcd(a: Int, b: Int): Int {
    return if (b == 0) a else gcd(b, a % b)
}

data class Fraction(val numerator: Int, val denominator: Int)

fun main() {
    // Вычитание десятичных дробей
    val result1 = subtract(10.5, 5.2)
    println("Результат вычитания десятичных дробей: $result1")

    // Вычитание обыкновенных дробей
    val fractionResult = subtract(3, 4, 1, 2)
    println("Результат вычитания обыкновенных дробей: $fractionResult")
}
