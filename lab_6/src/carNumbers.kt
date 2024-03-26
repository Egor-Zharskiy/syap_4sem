fun countCarNumbersWithSameDigits(): Int {
    var count = 0

    for (number in 1000..9999) {
        val digits = number.toString().toCharArray()

        // Проверяем, содержит ли номер машины только две или более одинаковых цифры
        if (digits.distinct().size <= 3) {
//            println(digits)
            count++
        }
    }

    return count
}
