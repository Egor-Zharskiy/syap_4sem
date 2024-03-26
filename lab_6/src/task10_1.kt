fun octalToBinary(octalNumber: String): String {
    var binaryResult = ""

    for (i in octalNumber.indices) {
        val octalDigit = octalNumber[i].toString().toInt()
        val binaryDigit = StringBuilder()

        // Перевод каждой цифры восьмеричного числа в двоичное число
        for (j in 2 downTo 0) {
            binaryDigit.append((octalDigit shr j) and 1)
        }

        binaryResult += binaryDigit.toString()
    }

    // Убираем ведущие нули
    return binaryResult.trimStart('0')
}

fun main() {
    val octalNumber = "325" // Вводимое восьмеричное число
    val binaryResult = octalToBinary(octalNumber)

    println("Восьмеричное число $octalNumber в двоичной системе: $binaryResult")
}
