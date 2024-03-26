fun main() {
    val count = countCarNumbersWithSameDigits()

    println("Количество номеров машин с двумя или более одинаковыми цифрами: $count\n---------------------------------")


    val calculator = Calculator()

    // Вычитание вещественных чисел
    val result1 = calculator.subtract(10.5, 5.2)
    println("Результат вычитания вещественных чисел: $result1")

    // Вычитание комплексных чисел
    val complexResult = calculator.subtract(7.0, 3.0, 4.0, 2.5)
    println("Результат вычитания комплексных чисел: $complexResult")
}