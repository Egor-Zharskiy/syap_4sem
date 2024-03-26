class Calculator {
    // Перегруженный метод для вычитания вещественных чисел
    fun subtract(a: Double, b: Double): Double {
        return a - b
    }

    // Перегруженный метод для вычитания комплексных чисел
    fun subtract(aReal: Double, aImaginary: Double, bReal: Double, bImaginary: Double): ComplexNumber {
        val realPart = aReal - bReal
        val imaginaryPart = aImaginary - bImaginary
        return ComplexNumber(realPart, imaginaryPart)
    }
}

data class ComplexNumber(val real: Double, val imaginary: Double)
